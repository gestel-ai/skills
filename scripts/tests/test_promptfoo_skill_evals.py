from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "promptfoo_skill_evals.py"


def load_module():
    spec = importlib.util.spec_from_file_location("promptfoo_skill_evals", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load promptfoo_skill_evals.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PromptfooSkillEvalsTest(unittest.TestCase):
    def test_builds_promptfoo_config_from_existing_behavior_spec(self) -> None:
        module = load_module()
        skill_dir = ROOT / "skillify"
        config = module.build_config(skill_dir)
        evals = json.loads((skill_dir / "evals" / "evals.json").read_text())["evals"]

        self.assertEqual(config["description"], "Promptfoo skill evals: skillify")
        self.assertEqual(
            config["providers"][0]["id"], "openrouter:deepseek/deepseek-v4-flash"
        )
        self.assertEqual(
            config["providers"][0]["config"]["apiKeyEnvar"], "OPENROUTER_API_KEY"
        )
        self.assertEqual(config["prompts"][0]["id"], "skill-behavior-contract")
        self.assertEqual(config["defaultTest"]["vars"]["skill_name"], "skillify")
        self.assertIn("# Skillify", config["defaultTest"]["vars"]["skill_markdown"])
        self.assertEqual(len(config["tests"]), len(evals))
        self.assertEqual(config["tests"][0]["vars"]["prompt"], evals[0]["prompt"])
        self.assertNotIn("skill_markdown", config["tests"][0]["vars"])
        self.assertIn("contains-json", config["tests"][0]["assert"][0]["type"])
        self.assertEqual(
            config["tests"][0]["assert"][0]["value"]["properties"]["trigger_decision"][
                "enum"
            ],
            ["trigger"],
        )
        self.assertEqual(
            config["tests"][0]["assert"][0]["value"]["properties"]["skill_name"][
                "enum"
            ],
            ["skillify"],
        )
        self.assertIn("llm-rubric", config["tests"][0]["assert"][1]["type"])
        self.assertEqual(config["tests"][0]["assert"][1]["threshold"], 0.8)
        self.assertIn(
            evals[0]["expected_output"], config["tests"][0]["assert"][1]["value"]
        )
        self.assertEqual(
            config["tests"][3]["assert"][0]["value"]["properties"]["trigger_decision"][
                "enum"
            ],
            ["do_not_trigger"],
        )
        self.assertEqual(
            config["tests"][3]["assert"][0]["value"]["properties"]["skill_name"][
                "enum"
            ],
            ["none"],
        )

    def test_check_mode_detects_missing_or_stale_generated_configs(self) -> None:
        module = load_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir) / "skills"
            skill_dir = temp_root / "demo"
            (skill_dir / "evals").mkdir(parents=True)
            (skill_dir / "SKILL.md").write_text(
                "---\n"
                "name: demo\n"
                "description: Use when testing demo skills\n"
                "---\n\n"
                "# Demo\n",
            )
            (skill_dir / "evals" / "evals.json").write_text(
                json.dumps(
                    {
                        "skill_name": "demo",
                        "evals": [
                            {
                                "id": 1,
                                "prompt": "Make a demo skill",
                                "expected_output": "Should trigger demo.",
                                "assertions": ["Triggers demo"],
                                "files": [],
                            }
                        ],
                    }
                )
            )

            self.assertEqual(
                run_quietly(module, ["--root", str(temp_root), "--check"]), 1
            )

            self.assertEqual(
                run_quietly(module, ["--root", str(temp_root), "--write"]), 0
            )
            self.assertEqual(
                run_quietly(module, ["--root", str(temp_root), "--check"]), 0
            )

            config_path = skill_dir / "evals" / "promptfooconfig.yaml"
            config_path.write_text(config_path.read_text() + "\n# stale\n")
            self.assertEqual(
                run_quietly(module, ["--root", str(temp_root), "--check"]), 1
            )


def run_quietly(module, argv: list[str]) -> int:
    with redirect_stdout(StringIO()), redirect_stderr(StringIO()):
        return module.main(argv)


if __name__ == "__main__":
    unittest.main()
