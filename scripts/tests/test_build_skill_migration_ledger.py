from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "build_skill_migration_ledger.py"


def load_module():
    spec = importlib.util.spec_from_file_location(
        "build_skill_migration_ledger", SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load build_skill_migration_ledger.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class BuildSkillMigrationLedgerTest(unittest.TestCase):
    def test_classifies_existing_gestel_distillations_as_merged(self) -> None:
        module = load_module()

        entry = module.build_entry(
            "references/skills/marketingskills/skills/product-marketing/SKILL.md"
        )

        self.assertEqual(entry["status"], "merged into named local skill")
        self.assertEqual(entry["local_skill"], "gestel-brand-snapshot")
        self.assertEqual(entry["commit"], "8bfcdffb655f16e713940cd04fb08891899c47db")
        self.assertEqual(entry["license"], "MIT")

    def test_blocks_provider_adapter_skills(self) -> None:
        module = load_module()

        entry = module.build_entry(
            "references/skills/claude-seo/extensions/ahrefs/skills/seo-ahrefs/SKILL.md"
        )

        self.assertEqual(entry["status"], "blocked by provider/auth/cost adapter")
        self.assertNotIn("local_skill", entry)
        self.assertEqual(
            entry["adapter_contract"],
            "docs/skill-migration-adapter-contracts.md#seo-ahrefs",
        )
        self.assertIn("Ahrefs API token", entry["required_credentials"])
        self.assertIn("cost gate", entry["next_input_needed"])

    def test_blocks_missing_runtime_dependency_skills(self) -> None:
        module = load_module()

        entry = module.build_entry(
            "references/skills/claude-blog/skills/blog-write/SKILL.md"
        )

        self.assertEqual(entry["status"], "blocked by missing runtime dependency")
        self.assertIn("root helper scripts", entry["reason"])
        self.assertEqual(
            entry["missing_runtime_refs"],
            [
                "scripts/blog_preflight.py",
                "scripts/blog_render.py",
                "scripts/generate_hero.py",
                "specialist agent: blog-reviewer",
            ],
        )
        self.assertIn("minimal local runtime", entry["next_input_needed"])

    def test_marks_duplicate_superseded_paths(self) -> None:
        module = load_module()

        entry = module.build_entry(
            "references/skills/claude-seo/skills/seo-image-gen/SKILL.md"
        )

        self.assertEqual(entry["status"], "duplicate superseded")
        self.assertIn("extensions/banana", entry["reason"])

    def test_waits_for_deep_research_for_freshness_sensitive_skills(self) -> None:
        module = load_module()

        entry = module.build_entry(
            "references/skills/claude-ads/skills/ads-google/SKILL.md"
        )

        self.assertEqual(entry["status"], "waiting on user-provided Deep Research")
        self.assertIn("platform rules", entry["reason"])

    def test_classifies_duplicate_names_by_source_path_not_name_only(self) -> None:
        module = load_module()

        entry = module.build_entry(
            "references/skills/marketingskills/skills/seo-audit/SKILL.md"
        )

        self.assertEqual(entry["status"], "waiting on user-provided Deep Research")

    def test_marks_safe_standardizable_skills_for_active_migration(self) -> None:
        module = load_module()

        entry = module.build_entry(
            "references/skills/marketingskills/skills/copywriting/SKILL.md"
        )

        self.assertEqual(entry["status"], "migrated active local skill")
        self.assertEqual(entry["local_skill"], "gestel-copywriting")


if __name__ == "__main__":
    unittest.main()
