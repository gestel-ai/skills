from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "render_skill_migration_research_needs.py"


def load_module():
    spec = importlib.util.spec_from_file_location(
        "render_skill_migration_research_needs", SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load render_skill_migration_research_needs.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class RenderSkillMigrationResearchNeedsTest(unittest.TestCase):
    def test_renders_waiting_entries_with_platform_prompts(self) -> None:
        module = load_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            ledger_path = root / "docs" / "skill-migration-ledger.json"
            ledger_path.parent.mkdir()
            ledger_path.write_text(
                json.dumps(
                    {
                        "entries": [
                            {
                                "source_path": "references/skills/demo/skills/seo-demo/SKILL.md",
                                "upstream_path": "references/source-repos/demo/skills/seo-demo/SKILL.md",
                                "name": "seo-demo",
                                "status": "waiting on user-provided Deep Research",
                                "reason": "Needs platform rules.",
                            }
                        ]
                    }
                )
            )

            rendered = module.render_report(root, ledger_path)

            self.assertIn("seo-demo", rendered)
            self.assertIn(".agents/skills/gestel-seo-demo/research-sources/", rendered)
            self.assertIn("ChatGPT Deep Research", rendered)
            self.assertIn("Gemini Deep Research", rendered)
            self.assertIn("Claude Research", rendered)
            self.assertIn("Perplexity Deep Research", rendered)


if __name__ == "__main__":
    unittest.main()
