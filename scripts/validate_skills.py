#!/usr/bin/env python3
"""Validate project-scoped skills under .agents/skills."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUICK_VALIDATE = (
    Path.home()
    / ".codex"
    / "skills"
    / ".system"
    / "skill-creator"
    / "scripts"
    / "quick_validate.py"
)
JS_EXTENSIONS = {".cjs", ".js", ".jsx", ".mjs", ".ts", ".tsx"}


def has_command(name: str) -> bool:
    return shutil.which(name) is not None


def run(command: list[str]) -> None:
    print("$ " + " ".join(command))
    subprocess.run(command, cwd=ROOT, check=True)


def skill_dirs() -> list[Path]:
    _ignore = {".git", "node_modules", ".ruff_cache", ".venv", "reference", "references", "__pycache__"}
    return sorted(
        p.parent
        for p in ROOT.rglob("SKILL.md")
        if not _ignore.intersection(p.parts)
    )


def has_files(paths: list[Path], suffixes: set[str]) -> bool:
    return any(path.suffix in suffixes for path in paths)


def all_files() -> list[Path]:
    ignored_parts = {".ruff_cache", ".venv", "node_modules", ".git", "reference", "references"}
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if ignored_parts.intersection(path.parts):
            continue
        files.append(path)
    return files


def validate_evals(skills: list[Path]) -> None:
    for skill in skills:
        evals_path = skill / "evals" / "evals.json"
        if not evals_path.exists():
            continue
        with evals_path.open() as file:
            json.load(file)


def validate_promptfoo_configs() -> None:
    run(["uv", "run", "scripts/promptfoo_skill_evals.py", "--check"])


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate project-scoped skills")
    parser.add_argument(
        "--skip-quick-validate",
        action="store_true",
        help="Skip Codex system quick_validate.py even when it exists",
    )
    args = parser.parse_args()

    skills = skill_dirs()
    if not skills:
        print("No skills found under .agents/skills")
        return 0

    missing = [command for command in ("uv", "uvx", "pnpm") if not has_command(command)]
    if missing:
        print(f"Missing required command(s): {', '.join(missing)}", file=sys.stderr)
        return 1

    validate_evals(skills)
    validate_promptfoo_configs()

    run(
        [
            "pnpm",
            "dlx",
            "markdownlint-cli2",
            "**/SKILL.md",
            "**/references/**/*.md",
            "**/research-sources/**/*.md",
        ]
    )

    files = all_files()
    if has_files(files, {".py"}):
        run(["uvx", "ruff", "check", "--no-cache", "."])
        run(["uvx", "ruff", "format", "--check", "--no-cache", "."])

    if has_files(files, JS_EXTENSIONS):
        run(["pnpm", "dlx", "@biomejs/biome", "check", "."])

    for skill in skills:
        checker = skill / "scripts" / "check_skill.py"
        if checker.exists():
            run(
                [
                    "uv",
                    "run",
                    str(checker.relative_to(ROOT)),
                    str(skill.relative_to(ROOT)),
                ]
            )

        if QUICK_VALIDATE.exists() and not args.skip_quick_validate:
            run(["uv", "run", "--with", "pyyaml", str(QUICK_VALIDATE), str(skill)])

    print(f"OK: validated {len(skills)} skill(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
