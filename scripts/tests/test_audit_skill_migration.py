from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "audit_skill_migration.py"


def load_module():
    spec = importlib.util.spec_from_file_location("audit_skill_migration", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load audit_skill_migration.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_source_skill(repo_root: Path, relative_path: str, name: str) -> None:
    primary = repo_root / relative_path
    upstream = repo_root / relative_path.replace(
        "references/skills/", "references/source-repos/", 1
    )
    for path in (primary, upstream):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            "---\n"
            f"name: {name}\n"
            f"description: Use when testing {name}\n"
            "---\n\n"
            f"# {name}\n"
        )


def write_local_skill(repo_root: Path, name: str, provenance: str) -> None:
    skill = repo_root / ".agents" / "skills" / name
    (skill / "evals").mkdir(parents=True, exist_ok=True)
    (skill / "references").mkdir(parents=True, exist_ok=True)
    (skill / "SKILL.md").write_text(
        f"---\nname: {name}\ndescription: Use when testing {name}\n---\n\n# {name}\n"
    )
    (skill / "evals" / "evals.json").write_text(
        json.dumps({"skill_name": name, "evals": [{"id": 1}]})
    )
    (skill / "evals" / "promptfooconfig.yaml").write_text("{}\n")
    (skill / "references" / "provenance.md").write_text(provenance)


def write_ledger(repo_root: Path, entries: list[dict[str, object]]) -> Path:
    ledger = repo_root / "docs" / "skill-migration-ledger.json"
    ledger.parent.mkdir(parents=True, exist_ok=True)
    ledger.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "entries": entries,
            },
            indent=2,
        )
    )
    return ledger


class SkillMigrationAuditTest(unittest.TestCase):
    def test_audit_detects_missing_source_paths(self) -> None:
        module = load_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            write_source_skill(
                repo_root, "references/skills/demo/skills/foo/SKILL.md", "foo"
            )
            write_source_skill(
                repo_root, "references/skills/demo/skills/bar/SKILL.md", "bar"
            )
            write_local_skill(
                repo_root,
                "gestel-foo",
                "Source: `references/source-repos/demo/skills/foo/SKILL.md`\n"
                "Commit: `abc123`\n"
                "License: MIT\n"
                "## Local Changes\n",
            )
            ledger = write_ledger(
                repo_root,
                [
                    {
                        "source_path": "references/skills/demo/skills/foo/SKILL.md",
                        "upstream_path": "references/source-repos/demo/skills/foo/SKILL.md",
                        "name": "foo",
                        "status": "merged into named local skill",
                        "local_skill": "gestel-foo",
                        "commit": "abc123",
                        "license": "MIT",
                        "reason": "Merged into a local GESTEL test skill.",
                    }
                ],
            )

            report = module.audit_ledger(repo_root, ledger)

            self.assertFalse(report.ok)
            self.assertIn(
                "missing ledger entry for references/skills/demo/skills/bar/SKILL.md",
                report.errors,
            )

    def test_audit_accepts_complete_ledger_with_local_skill_artifacts(self) -> None:
        module = load_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            write_source_skill(
                repo_root, "references/skills/demo/skills/foo/SKILL.md", "foo"
            )
            write_source_skill(
                repo_root, "references/skills/demo/skills/bar/SKILL.md", "bar"
            )
            write_local_skill(
                repo_root,
                "gestel-foo",
                "Source: `references/source-repos/demo/skills/foo/SKILL.md`\n"
                "Commit: `abc123`\n"
                "License: MIT\n"
                "## Local Changes\n",
            )
            ledger = write_ledger(
                repo_root,
                [
                    {
                        "source_path": "references/skills/demo/skills/foo/SKILL.md",
                        "upstream_path": "references/source-repos/demo/skills/foo/SKILL.md",
                        "name": "foo",
                        "status": "merged into named local skill",
                        "local_skill": "gestel-foo",
                        "commit": "abc123",
                        "license": "MIT",
                        "reason": "Merged into a local GESTEL test skill.",
                    },
                    {
                        "source_path": "references/skills/demo/skills/bar/SKILL.md",
                        "upstream_path": "references/source-repos/demo/skills/bar/SKILL.md",
                        "name": "bar",
                        "status": "blocked by missing runtime dependency",
                        "commit": "abc123",
                        "license": "MIT",
                        "reason": "The source skill references root scripts not present in this repo.",
                        "missing_runtime_refs": ["scripts/example.py"],
                        "next_input_needed": "Decide whether to migrate minimal local runtime with tests.",
                    },
                ],
            )

            report = module.audit_ledger(repo_root, ledger)

            self.assertTrue(report.ok, report.errors)
            self.assertEqual(report.source_count, 2)
            self.assertEqual(report.upstream_count, 2)
            self.assertEqual(report.unique_name_count, 2)
            self.assertEqual(report.status_counts["merged into named local skill"], 1)

    def test_audit_rejects_merged_entry_without_matching_provenance(self) -> None:
        module = load_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            write_source_skill(
                repo_root, "references/skills/demo/skills/foo/SKILL.md", "foo"
            )
            write_local_skill(
                repo_root,
                "gestel-foo",
                "Source: `references/source-repos/demo/skills/other/SKILL.md`\n"
                "Commit: `abc123`\n"
                "License: MIT\n"
                "## Local Changes\n",
            )
            ledger = write_ledger(
                repo_root,
                [
                    {
                        "source_path": "references/skills/demo/skills/foo/SKILL.md",
                        "upstream_path": "references/source-repos/demo/skills/foo/SKILL.md",
                        "name": "foo",
                        "status": "merged into named local skill",
                        "local_skill": "gestel-foo",
                        "commit": "abc123",
                        "license": "MIT",
                        "reason": "Merged into a local GESTEL test skill.",
                    }
                ],
            )

            report = module.audit_ledger(repo_root, ledger)

            self.assertFalse(report.ok)
            self.assertIn(
                "gestel-foo provenance does not mention references/source-repos/demo/skills/foo/SKILL.md",
                report.errors,
            )

    def test_audit_requires_blocker_resolution_details(self) -> None:
        module = load_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            write_source_skill(
                repo_root, "references/skills/demo/skills/foo/SKILL.md", "foo"
            )
            write_source_skill(
                repo_root, "references/skills/demo/skills/bar/SKILL.md", "bar"
            )
            ledger = write_ledger(
                repo_root,
                [
                    {
                        "source_path": "references/skills/demo/skills/foo/SKILL.md",
                        "upstream_path": "references/source-repos/demo/skills/foo/SKILL.md",
                        "name": "foo",
                        "status": "blocked by missing runtime dependency",
                        "commit": "abc123",
                        "license": "MIT",
                        "reason": "The source skill references root scripts not present in this repo.",
                    },
                    {
                        "source_path": "references/skills/demo/skills/bar/SKILL.md",
                        "upstream_path": "references/source-repos/demo/skills/bar/SKILL.md",
                        "name": "bar",
                        "status": "blocked by provider/auth/cost adapter",
                        "commit": "abc123",
                        "license": "MIT",
                        "reason": "The source skill assumes an external provider.",
                    },
                ],
            )

            report = module.audit_ledger(repo_root, ledger)

            self.assertFalse(report.ok)
            self.assertIn(
                "references/skills/demo/skills/foo/SKILL.md missing missing_runtime_refs",
                report.errors,
            )
            self.assertIn(
                "references/skills/demo/skills/foo/SKILL.md missing next_input_needed",
                report.errors,
            )
            self.assertIn(
                "references/skills/demo/skills/bar/SKILL.md missing adapter_contract",
                report.errors,
            )
            self.assertIn(
                "references/skills/demo/skills/bar/SKILL.md missing required_credentials",
                report.errors,
            )
            self.assertIn(
                "references/skills/demo/skills/bar/SKILL.md missing cost_or_quota_risk",
                report.errors,
            )
            self.assertIn(
                "references/skills/demo/skills/bar/SKILL.md missing next_input_needed",
                report.errors,
            )


if __name__ == "__main__":
    unittest.main()
