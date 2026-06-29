#!/usr/bin/env python3
"""Audit the skill migration ledger against source trees and local artifacts."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any, NamedTuple


ALLOWED_STATUSES = {
    "migrated active local skill",
    "merged into named local skill",
    "archived/reference-only with reason",
    "blocked by license",
    "blocked by missing runtime dependency",
    "blocked by provider/auth/cost adapter",
    "duplicate superseded",
    "waiting on user-provided Deep Research",
}

LOCAL_ARTIFACT_STATUSES = {
    "migrated active local skill",
    "merged into named local skill",
}
MISSING_RUNTIME_STATUS = "blocked by missing runtime dependency"
PROVIDER_ADAPTER_STATUS = "blocked by provider/auth/cost adapter"


class AuditReport(NamedTuple):
    ok: bool
    errors: list[str]
    source_count: int
    upstream_count: int
    unique_name_count: int
    status_counts: Counter[str]


def relative_skill_paths(root: Path, base: str) -> list[str]:
    return sorted(
        path.relative_to(root).as_posix() for path in (root / base).rglob("SKILL.md")
    )


def source_name(path: str) -> str:
    return Path(path).parent.name


def load_ledger(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def expected_upstream_path(source_path: str) -> str:
    return source_path.replace("references/skills/", "references/source-repos/", 1)


def validate_local_skill(root: Path, entry: dict[str, Any], errors: list[str]) -> None:
    local_skill = entry.get("local_skill")
    if not isinstance(local_skill, str) or not local_skill:
        errors.append(
            f"{entry['source_path']} missing local_skill for {entry['status']}"
        )
        return

    skill_dir = root / ".agents" / "skills" / local_skill
    required_paths = [
        skill_dir / "SKILL.md",
        skill_dir / "evals" / "evals.json",
        skill_dir / "evals" / "promptfooconfig.yaml",
        skill_dir / "references" / "provenance.md",
    ]
    for required_path in required_paths:
        if not required_path.exists():
            errors.append(
                f"{local_skill} missing {required_path.relative_to(root).as_posix()}"
            )

    provenance_path = skill_dir / "references" / "provenance.md"
    if provenance_path.exists():
        provenance = provenance_path.read_text()
        upstream_path = entry["upstream_path"]
        if upstream_path not in provenance:
            errors.append(f"{local_skill} provenance does not mention {upstream_path}")
        commit = str(entry.get("commit", ""))
        if commit and commit not in provenance:
            errors.append(f"{local_skill} provenance does not mention commit {commit}")
        license_name = str(entry.get("license", ""))
        if license_name and license_name not in provenance:
            errors.append(
                f"{local_skill} provenance does not mention license {license_name}"
            )


def require_nonempty_string(
    entry: dict[str, Any], key: str, source_path: str, errors: list[str]
) -> None:
    value = entry.get(key)
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{source_path} missing {key}")


def require_nonempty_string_list(
    entry: dict[str, Any], key: str, source_path: str, errors: list[str]
) -> None:
    value = entry.get(key)
    if not isinstance(value, list) or not value:
        errors.append(f"{source_path} missing {key}")
        return
    if not all(isinstance(item, str) and item.strip() for item in value):
        errors.append(f"{source_path} {key} must be a list of non-empty strings")


def validate_blocker_details(entry: dict[str, Any], errors: list[str]) -> None:
    source_path = entry["source_path"]
    status = entry.get("status")
    if status == MISSING_RUNTIME_STATUS:
        require_nonempty_string_list(entry, "missing_runtime_refs", source_path, errors)
        require_nonempty_string(entry, "next_input_needed", source_path, errors)
    elif status == PROVIDER_ADAPTER_STATUS:
        require_nonempty_string(entry, "adapter_contract", source_path, errors)
        require_nonempty_string_list(entry, "required_credentials", source_path, errors)
        require_nonempty_string_list(entry, "cost_or_quota_risk", source_path, errors)
        require_nonempty_string(entry, "next_input_needed", source_path, errors)


def audit_ledger(root: Path, ledger_path: Path) -> AuditReport:
    errors: list[str] = []
    sources = relative_skill_paths(root, "references/skills")
    upstreams = relative_skill_paths(root, "references/source-repos")
    source_set = set(sources)
    upstream_set = set(upstreams)

    ledger = load_ledger(ledger_path)
    entries = ledger.get("entries")
    if not isinstance(entries, list):
        raise ValueError(f"{ledger_path} must contain an entries array")

    entry_by_source: dict[str, dict[str, Any]] = {}
    for index, entry in enumerate(entries, start=1):
        if not isinstance(entry, dict):
            errors.append(f"ledger entry {index} is not an object")
            continue
        source_path = entry.get("source_path")
        if not isinstance(source_path, str) or not source_path:
            errors.append(f"ledger entry {index} missing source_path")
            continue
        if source_path in entry_by_source:
            errors.append(f"duplicate ledger entry for {source_path}")
        entry_by_source[source_path] = entry

    for source_path in sources:
        if source_path not in entry_by_source:
            errors.append(f"missing ledger entry for {source_path}")

    for source_path in sorted(set(entry_by_source) - source_set):
        errors.append(f"ledger entry has no source file: {source_path}")

    for source_path, entry in entry_by_source.items():
        upstream_path = entry.get("upstream_path")
        expected_upstream = expected_upstream_path(source_path)
        if upstream_path != expected_upstream:
            errors.append(f"{source_path} upstream_path must be {expected_upstream}")
        if isinstance(upstream_path, str) and upstream_path not in upstream_set:
            errors.append(f"{source_path} upstream file missing: {upstream_path}")

        name = entry.get("name")
        if name != source_name(source_path):
            errors.append(f"{source_path} name must be {source_name(source_path)}")

        status = entry.get("status")
        if status not in ALLOWED_STATUSES:
            errors.append(f"{source_path} invalid status: {status}")

        reason = entry.get("reason")
        if not isinstance(reason, str) or not reason.strip():
            errors.append(f"{source_path} missing reason")

        commit = entry.get("commit")
        if not isinstance(commit, str) or not commit.strip():
            errors.append(f"{source_path} missing commit")

        license_name = entry.get("license")
        if not isinstance(license_name, str) or not license_name.strip():
            errors.append(f"{source_path} missing license")

        if status in LOCAL_ARTIFACT_STATUSES:
            validate_local_skill(root, entry, errors)
        validate_blocker_details(entry, errors)

    upstream_count_for_sources = sum(
        1 for path in upstreams if path.startswith("references/source-repos/")
    )
    status_counts = Counter(
        str(entry.get("status")) for entry in entry_by_source.values()
    )
    return AuditReport(
        ok=not errors,
        errors=errors,
        source_count=len(sources),
        upstream_count=upstream_count_for_sources,
        unique_name_count=len({source_name(path) for path in sources}),
        status_counts=status_counts,
    )


def print_report(report: AuditReport) -> None:
    print(f"source_count: {report.source_count}")
    print(f"upstream_count: {report.upstream_count}")
    print(f"unique_name_count: {report.unique_name_count}")
    for status, count in sorted(report.status_counts.items()):
        print(f"status.{status}: {count}")
    if report.errors:
        print("errors:")
        for error in report.errors:
            print(f"- {error}")
    else:
        print("OK: migration ledger accounts for all source skills")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Audit docs/skill-migration-ledger.json"
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[3],
        help="Repository root, defaulting to this script's project root",
    )
    parser.add_argument(
        "--ledger",
        type=Path,
        default=Path("docs/skill-migration-ledger.json"),
        help="Migration ledger path relative to root unless absolute",
    )
    args = parser.parse_args(argv)

    root = args.root.resolve()
    ledger_path = args.ledger if args.ledger.is_absolute() else root / args.ledger
    report = audit_ledger(root, ledger_path)
    print_report(report)
    return 0 if report.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
