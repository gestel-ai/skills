#!/usr/bin/env python3
"""Tests for validate_review_result.py."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "validate_review_result.py"


def passing_review() -> dict[str, object]:
    gate = {"status": "pass", "notes": "Checked against source.", "evidence": ["ev_1"]}
    return {
        "variant_id": "v_pkg_test_1",
        "review_status": "launch-ready",
        "gates": {
            "product_fidelity": gate,
            "claim_price_evidence": gate,
            "platform_fit": gate,
        },
        "failure_type": "none",
        "credit_policy": "charge",
        "regeneration_available": False,
        "required_fixes": [],
    }


class ValidateReviewResultTest(unittest.TestCase):
    def run_validator(
        self, review: dict[str, object]
    ) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "review.json"
            path.write_text(json.dumps(review))
            return subprocess.run(
                [sys.executable, str(SCRIPT), str(path)],
                check=False,
                text=True,
                capture_output=True,
            )

    def test_accepts_launch_ready_when_all_gates_pass(self) -> None:
        result = self.run_validator(passing_review())

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("OK:", result.stdout)

    def test_rejects_launch_ready_with_warning_gate(self) -> None:
        review = passing_review()
        gates = review["gates"]
        assert isinstance(gates, dict)
        platform_fit = gates["platform_fit"]
        assert isinstance(platform_fit, dict)
        platform_fit["status"] = "warning"

        result = self.run_validator(review)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("launch-ready requires all gates to pass", result.stderr)

    def test_non_launch_ready_requires_failure_type_and_fix(self) -> None:
        review = passing_review()
        review["review_status"] = "needs_revision"

        result = self.run_validator(review)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("require a failure_type", result.stderr)
        self.assertIn("at least one fix", result.stderr)


if __name__ == "__main__":
    unittest.main()
