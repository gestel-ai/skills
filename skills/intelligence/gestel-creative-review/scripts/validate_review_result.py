#!/usr/bin/env python3
"""Validate a GESTEL Creative Review Gate result."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


GATES = ("product_fidelity", "claim_price_evidence", "platform_fit")
GATE_STATUSES = {"pass", "warning", "fail"}
REVIEW_STATUSES = {"launch-ready", "needs_revision", "blocked"}
FAILURE_TYPES = {
    "none",
    "product_fidelity",
    "claim_price_evidence",
    "platform_fit",
    "system",
    "user_input",
}
CREDIT_POLICIES = {"charge", "refund", "no_charge", "regeneration_credit"}


def _is_nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _load_json(path: Path) -> tuple[dict[str, Any] | None, list[str]]:
    try:
        data = json.loads(path.read_text())
    except FileNotFoundError:
        return None, [f"{path}: file not found"]
    except json.JSONDecodeError as exc:
        return None, [f"{path}: invalid JSON: {exc}"]
    if not isinstance(data, dict):
        return None, ["review result must be a JSON object"]
    return data, []


def _validate_gate(name: str, value: object) -> list[str]:
    if not isinstance(value, dict):
        return [f"gates.{name} must be an object"]
    errors: list[str] = []
    if value.get("status") not in GATE_STATUSES:
        errors.append(f"gates.{name}.status is not allowed")
    if not _is_nonempty_string(value.get("notes")):
        errors.append(f"gates.{name}.notes must be a non-empty string")
    evidence = value.get("evidence", [])
    if not isinstance(evidence, list) or not all(
        _is_nonempty_string(item) for item in evidence
    ):
        errors.append(f"gates.{name}.evidence must be a list of strings")
    return errors


def validate_review(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if not _is_nonempty_string(data.get("variant_id")):
        errors.append("variant_id must be a non-empty string")

    review_status = data.get("review_status")
    failure_type = data.get("failure_type")
    if review_status not in REVIEW_STATUSES:
        errors.append("review_status is not allowed")
    if failure_type not in FAILURE_TYPES:
        errors.append("failure_type is not allowed")
    if data.get("credit_policy") not in CREDIT_POLICIES:
        errors.append("credit_policy is not allowed")
    if not isinstance(data.get("regeneration_available"), bool):
        errors.append("regeneration_available must be a boolean")

    gates = data.get("gates")
    if not isinstance(gates, dict):
        errors.append("gates must be an object")
        gates = {}

    gate_statuses: list[str] = []
    for gate in GATES:
        if gate not in gates:
            errors.append(f"gates.{gate} is required")
            continue
        gate_value = gates[gate]
        if isinstance(gate_value, dict) and isinstance(gate_value.get("status"), str):
            gate_statuses.append(gate_value["status"])
        errors.extend(_validate_gate(gate, gate_value))

    required_fixes = data.get("required_fixes")
    if not isinstance(required_fixes, list) or not all(
        _is_nonempty_string(item) for item in required_fixes
    ):
        errors.append("required_fixes must be a list of strings")

    has_failure = "fail" in gate_statuses
    has_warning = "warning" in gate_statuses
    if review_status == "launch-ready":
        if has_failure or has_warning:
            errors.append("launch-ready requires all gates to pass")
        if failure_type != "none":
            errors.append("launch-ready requires failure_type `none`")
        if required_fixes:
            errors.append("launch-ready requires no required_fixes")
    else:
        if failure_type == "none":
            errors.append("non-launch-ready results require a failure_type")
        if not required_fixes:
            errors.append("non-launch-ready results require at least one fix")

    if has_failure and review_status == "launch-ready":
        errors.append("failed gates cannot be launch-ready")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate a GESTEL Creative Review Gate result JSON file"
    )
    parser.add_argument("review_result", type=Path)
    args = parser.parse_args()

    data, errors = _load_json(args.review_result)
    if data is not None:
        errors.extend(validate_review(data))

    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1

    print(f"OK: {args.review_result} is a valid GESTEL review result")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
