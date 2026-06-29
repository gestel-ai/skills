#!/usr/bin/env python3
"""Render Deep Research needs for skill migration waiting entries."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
WAITING_STATUS = "waiting on user-provided Deep Research"
DATE = "2026-06-26"


def load_waiting_entries(ledger_path: Path) -> list[dict[str, Any]]:
    ledger = json.loads(ledger_path.read_text())
    entries = ledger.get("entries")
    if not isinstance(entries, list):
        raise ValueError(f"{ledger_path} must contain an entries array")
    return [entry for entry in entries if entry.get("status") == WAITING_STATUS]


def local_skill_name(entry: dict[str, Any]) -> str:
    return str(entry.get("local_skill") or f"gestel-{entry['name']}")


def target_path(entry: dict[str, Any]) -> str:
    return f".agents/skills/{local_skill_name(entry)}/research-sources/"


def cadence(entry: dict[str, Any]) -> str:
    name = entry["name"]
    if name.startswith("seo-") or name in {"ai-seo", "programmatic-seo", "schema"}:
        return (
            "Monthly, and whenever official search or platform documentation changes."
        )
    if name.startswith("ads-") or name == "aso":
        return "Monthly, and whenever ad platform product, placement, policy, or reporting behavior changes."
    if name.startswith("blog-"):
        return "Quarterly, and whenever search, schema, localization, or fact-checking standards change."
    return "Quarterly, or when the source domain changes materially."


def source_types(entry: dict[str, Any]) -> str:
    name = entry["name"]
    if name.startswith("ads-") or name == "aso":
        return "Official platform docs, policy docs, placement/spec docs, reporting/export docs, reputable practitioner change logs."
    if name.startswith("seo-") or name in {"ai-seo", "programmatic-seo", "schema"}:
        return "Official search engine docs, schema.org docs, webmaster docs, platform API docs, primary benchmark reports."
    if name.startswith("blog-"):
        return "Official search/content docs, schema docs, localization guidance, fact-checking standards, credible editorial examples."
    return "Official docs, primary source reports, credible implementation examples, and dated practitioner notes."


def refresh_trigger(entry: dict[str, Any]) -> str:
    name = entry["name"]
    if name.startswith("ads-"):
        return "New ad format, policy update, attribution/reporting change, or platform UI/export change."
    if name.startswith("seo-") or name in {"ai-seo", "programmatic-seo", "schema"}:
        return "Official search guidance update, schema deprecation, ranking/AI-search behavior change, or failed freshness eval."
    if name.startswith("blog-"):
        return "Search/content guidance update, schema/content standard change, localization requirement change, or failed freshness eval."
    return "Material domain change or failed freshness eval."


def core_prompt(entry: dict[str, Any]) -> str:
    skill_name = local_skill_name(entry)
    domain = entry["name"].replace("-", " ")
    return f"""Research topic: Build or refresh an agent skill named {skill_name} for {domain}.
Target user: an AI coding agent maintaining project-scoped local skills.
Core jobs the skill must support:
- Decide whether the source skill can become an active local skill.
- Separate stable workflow rules from freshness-sensitive claims.
- Recommend references, evals, scripts, and validation gates.

Near-miss tasks the skill should not trigger on:
- Live account mutation or publishing.
- Paid provider/API use without an explicit adapter and credentials.
- Copying third-party prompt bodies without license and provenance review.

Freshness mode: current
- Verify official documentation and current platform behavior as of {DATE}.
- Mark each current claim with date checked and refresh trigger.

Known sources to include:
- {entry["upstream_path"]}
- {entry["source_path"]}

Non-goals:
- Do not create runnable provider adapters.
- Do not assume hidden API keys or upstream root scripts.

Research goals:
1. Identify stable best practices for this skill domain.
2. Identify current or freshness-sensitive claims and their refresh triggers.
3. Find concrete examples, anti-patterns, edge cases, and failure modes.
4. Recommend trigger wording and near-miss boundaries.
5. Recommend references, scripts, assets, and eval cases.
6. Flag source conflicts, weak evidence, and open questions.

Output format:
1. Executive summary
2. Stable principles
3. Current or freshness-sensitive claims
4. Recommended SKILL.md workflow
5. Recommended reference files
6. Recommended scripts or lint/format gates
7. Recommended eval cases, including should-not-trigger cases
8. Risks, anti-patterns, and safety concerns
9. Source table with title, URL, publisher, date checked, and why it matters
10. Open questions

Return the report as Markdown that can be saved under {target_path(entry)}.
"""


def platform_prompts(entry: dict[str, Any]) -> str:
    prompt = core_prompt(entry)
    skill_name = local_skill_name(entry)
    wrappers = [
        (
            f"ChatGPT Deep Research for {skill_name}",
            "Use ChatGPT Deep Research for a multi-step, source-backed investigation. Prefer official and primary sources, separate evidence from inference, and include a complete bibliography.",
        ),
        (
            f"Gemini Deep Research for {skill_name}",
            "Use Gemini Deep Research. Preserve the research plan if Gemini creates one, use current web sources, and return the final report with citations and bibliography in Markdown.",
        ),
        (
            f"Claude Research for {skill_name}",
            "Use Claude Research. Investigate multiple angles systematically, include easy-to-check citations, call out uncertainty and source conflicts, and do not use tools that write to external systems.",
        ),
        (
            f"Perplexity Deep Research for {skill_name}",
            "Use Perplexity Deep Research or Advanced Deep Research. Prefer exhaustive source discovery, compare conflicting sources, cite every major claim, and include a low-confidence or not-used source section.",
        ),
    ]
    sections = []
    for title, wrapper in wrappers:
        sections.append(f"### {title}\n\n```text\n{wrapper}\n\n{prompt}```")
    return "\n\n".join(sections)


def render_report(root: Path, ledger_path: Path) -> str:
    entries = load_waiting_entries(ledger_path)
    lines = [
        "# Skill Migration Research Needs",
        "",
        f"Generated: {DATE}",
        "",
        "This report lists source skills that are intentionally not active local skills yet because they need user-provided Deep Research before safe standardization. Agents must not synthesize files under `research-sources/`; the user should run the prompts below in external research tools and provide Markdown exports.",
        "",
        "## Summary",
        "",
        f"- Waiting source skills: {len(entries)}",
        "- Source of truth: `docs/skill-migration-ledger.json`",
        "- Target convention: `.agents/skills/<local-skill>/research-sources/`",
        "",
        "## Needs Table",
        "",
        "| Source skill | Source path | Target path | Reason | Cadence | Refresh trigger | Source types |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for entry in entries:
        lines.append(
            f"| `{entry['name']}` | `{entry['source_path']}` | `{target_path(entry)}` | {entry['reason']} | {cadence(entry)} | {refresh_trigger(entry)} | {source_types(entry)} |"
        )

    lines.extend(["", "## Platform Prompts", ""])
    for entry in entries:
        lines.extend(
            [
                f"## {local_skill_name(entry)}",
                "",
                f"- Source path: `{entry['source_path']}`",
                f"- Target path: `{target_path(entry)}`",
                f"- Cadence: {cadence(entry)}",
                f"- Trigger: {refresh_trigger(entry)}",
                f"- Source types: {source_types(entry)}",
                "",
                platform_prompts(entry),
                "",
            ]
        )

    return "\n".join(lines).rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Render docs/skill-migration-research-needs.md"
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=ROOT,
        help="Repository root, defaulting to this script's project root",
    )
    parser.add_argument(
        "--ledger",
        type=Path,
        default=Path("docs/skill-migration-ledger.json"),
        help="Migration ledger path relative to root unless absolute",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("docs/skill-migration-research-needs.md"),
        help="Output path relative to root unless absolute",
    )
    parser.add_argument("--write", action="store_true", help="Write the report")
    args = parser.parse_args(argv)

    root = args.root.resolve()
    ledger = args.ledger if args.ledger.is_absolute() else root / args.ledger
    output = args.output if args.output.is_absolute() else root / args.output
    rendered = render_report(root, ledger)
    if args.write:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered)
        print(f"Wrote {output.relative_to(root)}")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
