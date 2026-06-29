#!/usr/bin/env python3
"""Validate a GESTEL Creative Package manifest."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ALLOWED_CHANNELS = {"meta", "instagram"}
ALLOWED_SURFACES = {
    "smartstore",
    "own-store",
    "coupang",
    "kakao-gift",
    "marketplace",
    "vertical",
}
ALLOWED_FAMILIES = {
    "review_proof",
    "problem_solution",
    "limited_offer",
    "comparison_grid",
    "ingredient_callout",
    "marketplace_thumbnail",
}
ALLOWED_RATIOS = {"4:5", "1:1", "9:16"}
ALLOWED_REVIEW_STATUSES = {"draft", "needs_review", "launch-ready", "blocked"}
REQUIRED_ITEM_FIELDS = {
    "variant_id",
    "template_family",
    "layout_id",
    "ratio",
    "asset_path",
    "angle",
    "experiment_hypothesis",
    "slots",
    "review_status",
    "utm",
}
REQUIRED_SLOT_FIELDS = {"product_visual", "headline", "cta"}


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
        return None, ["manifest must be a JSON object"]
    return data, []


def _validate_utm(item: dict[str, Any], index: int) -> list[str]:
    errors: list[str] = []
    utm = item.get("utm")
    if not isinstance(utm, dict):
        return [f"items[{index}].utm must be an object"]
    for key in ("utm_campaign", "utm_content"):
        if not _is_nonempty_string(utm.get(key)):
            errors.append(f"items[{index}].utm.{key} must be a non-empty string")
    if utm.get("utm_content") != item.get("variant_id"):
        errors.append(f"items[{index}].utm.utm_content must match variant_id")
    return errors


def _validate_slots(item: dict[str, Any], index: int) -> list[str]:
    errors: list[str] = []
    slots = item.get("slots")
    if not isinstance(slots, dict):
        return [f"items[{index}].slots must be an object"]
    for key in REQUIRED_SLOT_FIELDS:
        if not _is_nonempty_string(slots.get(key)):
            errors.append(f"items[{index}].slots.{key} must be a non-empty string")
    for key, value in slots.items():
        if not isinstance(key, str) or not isinstance(value, str):
            errors.append(f"items[{index}].slots entries must be string-to-string")
    return errors


def _validate_item(item: object, index: int, variant_ids: set[str]) -> list[str]:
    if not isinstance(item, dict):
        return [f"items[{index}] must be an object"]

    errors: list[str] = []
    missing = sorted(REQUIRED_ITEM_FIELDS - set(item))
    if missing:
        errors.append(f"items[{index}] missing required fields: {', '.join(missing)}")

    variant_id = item.get("variant_id")
    if not _is_nonempty_string(variant_id):
        errors.append(f"items[{index}].variant_id must be a non-empty string")
    elif variant_id in variant_ids:
        errors.append(f"items[{index}].variant_id is duplicated: {variant_id}")
    else:
        variant_ids.add(variant_id)

    if item.get("template_family") not in ALLOWED_FAMILIES:
        errors.append(f"items[{index}].template_family is not allowed")
    if item.get("ratio") not in ALLOWED_RATIOS:
        errors.append(f"items[{index}].ratio is not allowed")
    if item.get("review_status") not in ALLOWED_REVIEW_STATUSES:
        errors.append(f"items[{index}].review_status is not allowed")

    for key in ("layout_id", "asset_path", "angle", "experiment_hypothesis"):
        if not _is_nonempty_string(item.get(key)):
            errors.append(f"items[{index}].{key} must be a non-empty string")

    evidence_ids = item.get("product_claim_evidence_ids", [])
    if not isinstance(evidence_ids, list) or not all(
        _is_nonempty_string(value) for value in evidence_ids
    ):
        errors.append(
            f"items[{index}].product_claim_evidence_ids must be a list of strings"
        )

    errors.extend(_validate_slots(item, index))
    errors.extend(_validate_utm(item, index))
    return errors


def validate_manifest(data: dict[str, Any], *, mode: str) -> list[str]:
    errors: list[str] = []
    for key in ("package_id", "brand_snapshot_ref"):
        if not _is_nonempty_string(data.get(key)):
            errors.append(f"{key} must be a non-empty string")

    if data.get("channel") not in ALLOWED_CHANNELS:
        errors.append("channel must be one of: " + ", ".join(sorted(ALLOWED_CHANNELS)))
    if data.get("commerce_surface") not in ALLOWED_SURFACES:
        errors.append(
            "commerce_surface must be one of: " + ", ".join(sorted(ALLOWED_SURFACES))
        )

    items = data.get("items")
    if not isinstance(items, list) or not items:
        errors.append("items must be a non-empty array")
        items = []

    variant_ids: set[str] = set()
    families: set[str] = set()
    for index, item in enumerate(items):
        if isinstance(item, dict) and isinstance(item.get("template_family"), str):
            families.add(item["template_family"])
        errors.extend(_validate_item(item, index, variant_ids))

    export = data.get("export")
    if not isinstance(export, dict):
        errors.append("export must be an object")
    else:
        for key in ("package_name", "naming_pattern"):
            if not _is_nonempty_string(export.get(key)):
                errors.append(f"export.{key} must be a non-empty string")

    if mode == "first-pack":
        if len(items) != 3:
            errors.append("first-pack mode requires exactly 3 items")
        if any(isinstance(item, dict) and item.get("ratio") != "4:5" for item in items):
            errors.append("first-pack mode requires every item ratio to be 4:5")
        if len(families) != 3:
            errors.append("first-pack mode requires 3 distinct template families")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate a GESTEL Creative Package manifest JSON file"
    )
    parser.add_argument(
        "--mode",
        choices=("package", "first-pack"),
        default="package",
        help="Validation mode. Use first-pack for the MVP three-image 4:5 pack.",
    )
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()

    data, errors = _load_json(args.manifest)
    if data is not None:
        errors.extend(validate_manifest(data, mode=args.mode))

    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1

    print(f"OK: {args.manifest} is a valid GESTEL Creative Package manifest")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
