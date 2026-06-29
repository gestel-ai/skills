#!/usr/bin/env python3
"""Tests for validate_pack_schema.py."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "validate_pack_schema.py"


def base_manifest() -> dict[str, object]:
    families = ["review_proof", "problem_solution", "limited_offer"]
    return {
        "package_id": "pkg_test",
        "brand_snapshot_ref": ".agents/gestel/brand-snapshot.md",
        "channel": "meta",
        "commerce_surface": "smartstore",
        "items": [
            {
                "variant_id": f"v_pkg_test_{index}",
                "template_family": family,
                "layout_id": f"{family}.focus.v1",
                "ratio": "4:5",
                "asset_path": f"exports/v_pkg_test_{index}.png",
                "angle": family.replace("_", " "),
                "experiment_hypothesis": "This angle will improve CTR.",
                "slots": {
                    "product_visual": "product-photo-1",
                    "headline": "제품 장점 확인",
                    "cta": "자세히 보기",
                },
                "product_claim_evidence_ids": [],
                "review_status": "needs_review",
                "utm": {
                    "utm_campaign": "gestel_pkg_test",
                    "utm_content": f"v_pkg_test_{index}",
                },
            }
            for index, family in enumerate(families, start=1)
        ],
        "export": {
            "package_name": "gestel_pkg_test",
            "naming_pattern": "{package_id}_{variant_id}_{ratio}",
        },
    }


class ValidatePackSchemaTest(unittest.TestCase):
    def run_validator(
        self, manifest: dict[str, object], *args: str
    ) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "manifest.json"
            path.write_text(json.dumps(manifest))
            return subprocess.run(
                [sys.executable, str(SCRIPT), *args, str(path)],
                check=False,
                text=True,
                capture_output=True,
            )

    def test_accepts_valid_first_pack(self) -> None:
        result = self.run_validator(base_manifest(), "--mode", "first-pack")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("OK:", result.stdout)

    def test_rejects_duplicate_variant_ids(self) -> None:
        manifest = base_manifest()
        items = manifest["items"]
        assert isinstance(items, list)
        items[1]["variant_id"] = items[0]["variant_id"]  # type: ignore[index]

        result = self.run_validator(manifest)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("duplicated", result.stderr)

    def test_rejects_first_pack_without_three_distinct_families(self) -> None:
        manifest = base_manifest()
        items = manifest["items"]
        assert isinstance(items, list)
        items[2]["template_family"] = "review_proof"  # type: ignore[index]

        result = self.run_validator(manifest, "--mode", "first-pack")

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("3 distinct template families", result.stderr)


if __name__ == "__main__":
    unittest.main()
