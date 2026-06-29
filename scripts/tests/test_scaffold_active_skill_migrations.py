from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "scaffold_active_skill_migrations.py"


def load_module():
    spec = importlib.util.spec_from_file_location(
        "scaffold_active_skill_migrations", SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load scaffold_active_skill_migrations.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ScaffoldActiveSkillMigrationsTest(unittest.TestCase):
    def test_scaffolds_active_skill_artifacts_from_ledger_entry(self) -> None:
        module = load_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            ledger = {
                "schema_version": 1,
                "entries": [
                    {
                        "source_path": "references/skills/demo/skills/foo/SKILL.md",
                        "upstream_path": "references/source-repos/demo/skills/foo/SKILL.md",
                        "name": "foo",
                        "repo": "demo",
                        "commit": "abc123",
                        "license": "MIT",
                        "status": "migrated active local skill",
                        "local_skill": "gestel-foo",
                        "reason": "Safe deterministic source skill migration.",
                    }
                ],
            }
            (root / "docs").mkdir()
            ledger_path = root / "docs" / "skill-migration-ledger.json"
            ledger_path.write_text(json.dumps(ledger))

            created = module.scaffold_from_ledger(root, ledger_path)

            self.assertEqual(created, ["gestel-foo"])
            skill_dir = root / ".agents" / "skills" / "gestel-foo"
            self.assertTrue((skill_dir / "SKILL.md").exists())
            self.assertTrue((skill_dir / "references" / "source-usage.md").exists())
            self.assertTrue((skill_dir / "references" / "provenance.md").exists())
            self.assertTrue((skill_dir / "evals" / "evals.json").exists())
            provenance = (skill_dir / "references" / "provenance.md").read_text()
            self.assertIn(
                "references/source-repos/demo/skills/foo/SKILL.md", provenance
            )
            self.assertIn("abc123", provenance)
            self.assertIn("MIT", provenance)
            evals = json.loads((skill_dir / "evals" / "evals.json").read_text())
            self.assertEqual(evals["skill_name"], "gestel-foo")
            self.assertGreaterEqual(len(evals["evals"]), 6)


if __name__ == "__main__":
    unittest.main()
