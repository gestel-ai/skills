#!/usr/bin/env python3
"""Check that a Goal prompt has the minimum durable-work contract shape."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


DEFAULT_MAX_CHARS = 4000

CHECKS = {
    "verification": (
        "verified",
        "verify",
        "verification",
        "test",
        "tests",
        "build",
        "lint",
        "benchmark",
        "evidence",
        "검증",
        "테스트",
        "증거",
    ),
    "constraints": (
        "preserve",
        "preserving",
        "constraint",
        "constraints",
        "without changing",
        "do not",
        "non-goal",
        "while keeping",
        "유지",
        "보존",
        "제약",
        "건드리지",
    ),
    "iteration": (
        "checkpoint",
        "checkpoints",
        "iteration",
        "iterate",
        "after each",
        "progress",
        "log",
        "체크포인트",
        "반복",
        "진행",
        "로그",
    ),
    "blocked_stop": (
        "blocked",
        "blocker",
        "stop with",
        "stop and report",
        "next input",
        "unable",
        "cannot",
        "멈추",
        "차단",
        "막히",
        "필요한 입력",
    ),
}

DELEGATION_CHECKS = {
    "delegation": (
        "subagent",
        "subagents",
        "worker",
        "workers",
        "delegate",
        "delegation",
        "parallel",
        "fan-out",
        "role",
        "roles",
        "agent team",
        "multi-agent",
        "병렬",
        "위임",
        "작업자",
        "역할",
    ),
    "integration": (
        "integrate",
        "integration",
        "merge",
        "aggregate",
        "aggregation",
        "synthesize",
        "handoff",
        "final verification",
        "controller",
        "main agent",
        "통합",
        "취합",
        "최종 검증",
    ),
}


def read_prompt(args: argparse.Namespace) -> str:
    if args.text is not None:
        return args.text
    if args.file is not None:
        return Path(args.file).read_text()
    return sys.stdin.read()


def contains_any(text: str, needles: tuple[str, ...]) -> bool:
    lowered = text.lower()
    return any(needle.lower() in lowered for needle in needles)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", help="Read the Goal prompt from a file")
    parser.add_argument("--text", help="Read the Goal prompt from this argument")
    parser.add_argument(
        "--max-chars",
        type=int,
        default=DEFAULT_MAX_CHARS,
        help=f"Maximum prompt length, default {DEFAULT_MAX_CHARS}",
    )
    parser.add_argument(
        "--allow-no-slash",
        action="store_true",
        help="Allow a Goal objective that does not start with /goal",
    )
    parser.add_argument(
        "--require-delegation",
        action="store_true",
        help="Require subagent/worker delegation and integration signals",
    )
    args = parser.parse_args()

    prompt = read_prompt(args).strip()
    issues: list[str] = []

    if not prompt:
        issues.append("Prompt is empty")
    if len(prompt) > args.max_chars:
        issues.append(f"Prompt is {len(prompt)} chars, above {args.max_chars}")
    if not args.allow_no_slash and not prompt.startswith("/goal"):
        issues.append("Prompt should start with /goal")

    for name, needles in CHECKS.items():
        if not contains_any(prompt, needles):
            issues.append(f"Missing {name} signal")

    if args.require_delegation:
        for name, needles in DELEGATION_CHECKS.items():
            if not contains_any(prompt, needles):
                issues.append(f"Missing {name} signal")

    if issues:
        for issue in issues:
            print(f"FAIL: {issue}")
        return 1

    if args.require_delegation:
        print("OK: Goal prompt has contract and delegation signals")
    else:
        print("OK: Goal prompt has the required contract signals")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
