#!/usr/bin/env python3
"""Lightweight structural checks for an agent skill directory."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9-]{1,64}$")
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
LINK_RE = re.compile(
    r"\((references/[^)]+\.md|research-sources/[^)]+\.md|scripts/[^)]+|assets/[^)]+)\)"
)
DELEGATION_RE = re.compile(
    r"\b(subagents?|multi-agent|parallel|fan-out|fan-in|specialists?|"
    r"delegat(?:e|ion)|workers?|roles?|team|aggregation|fallback)\b",
    re.IGNORECASE,
)


def parse_frontmatter(text: str) -> dict[str, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError("SKILL.md must start with YAML frontmatter")

    values: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip().strip('"').strip("'")
        values[key.strip()] = value
    return values


def check_evals(skill_dir: Path) -> list[str]:
    issues: list[str] = []
    evals_path = skill_dir / "evals" / "evals.json"
    if not evals_path.exists():
        issues.append("WARN: evals/evals.json is missing")
        return issues

    try:
        data = json.loads(evals_path.read_text())
    except json.JSONDecodeError as exc:
        return [f"FAIL: evals/evals.json is invalid JSON: {exc}"]

    if data.get("skill_name") != skill_dir.name:
        issues.append("FAIL: evals/evals.json skill_name must match directory name")

    evals = data.get("evals")
    if not isinstance(evals, list) or not evals:
        issues.append("FAIL: evals/evals.json must contain a non-empty evals array")
        return issues

    has_negative = False
    has_delegation = False
    for index, item in enumerate(evals, start=1):
        if not isinstance(item, dict):
            issues.append(f"FAIL: eval #{index} must be an object")
            continue
        for key in ("id", "prompt", "expected_output", "assertions", "files"):
            if key not in item:
                issues.append(f"FAIL: eval #{index} missing {key}")
        expected = str(item.get("expected_output", "")).lower()
        if (
            "should not trigger" in expected
            or "should defer" in expected
            or "near-miss" in expected
        ):
            has_negative = True
        text_fields = [
            str(item.get("prompt", "")),
            str(item.get("expected_output", "")),
        ]
        assertions = item.get("assertions", [])
        if isinstance(assertions, list):
            text_fields.extend(str(assertion) for assertion in assertions)
        if DELEGATION_RE.search("\n".join(text_fields)):
            has_delegation = True

    if not has_negative:
        issues.append("WARN: evals should include at least one should-not-trigger case")
    if not has_delegation:
        issues.append(
            "WARN: evals should include at least one delegation or fallback case"
        )

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Check a skill directory")
    parser.add_argument("skill_dir", type=Path)
    args = parser.parse_args()

    skill_dir = args.skill_dir.resolve()
    skill_md = skill_dir / "SKILL.md"
    issues: list[str] = []

    if not skill_dir.is_dir():
        print(f"FAIL: {skill_dir} is not a directory")
        return 1
    if not skill_md.exists():
        print("FAIL: SKILL.md is missing")
        return 1

    text = skill_md.read_text()
    try:
        frontmatter = parse_frontmatter(text)
    except ValueError as exc:
        print(f"FAIL: {exc}")
        return 1

    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")

    if name != skill_dir.name:
        issues.append("FAIL: frontmatter name must match directory name")
    if not NAME_RE.fullmatch(name):
        issues.append("FAIL: name must use lowercase letters, digits, and hyphens only")
    if not description:
        issues.append("FAIL: description is required")
    if len(description) > 1024:
        issues.append("FAIL: description exceeds 1024 characters")
    if not description.lower().startswith("use when"):
        issues.append("WARN: description should start with 'Use when'")
    if "[todo" in text.lower() or "todo:" in text.lower():
        issues.append("FAIL: SKILL.md still contains TODO placeholders")

    body = FRONTMATTER_RE.sub("", text, count=1)
    body_lines = len(body.splitlines())
    if body_lines > 500:
        issues.append(
            f"WARN: SKILL.md body is {body_lines} lines; consider moving details to references"
        )

    for target in LINK_RE.findall(text):
        if not (skill_dir / target).exists():
            issues.append(f"FAIL: linked resource does not exist: {target}")

    issues.extend(check_evals(skill_dir))

    failures = [issue for issue in issues if issue.startswith("FAIL")]
    for issue in issues:
        print(issue)
    if failures:
        return 1
    print(f"OK: {skill_dir.name} passed structural checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
