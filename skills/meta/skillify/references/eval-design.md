<!-- Updated: 2026-06-26 | v1.0 -->
<!-- Sources: OpenAI Codex Agent Skills best practices, Codex skill-creator validator, local eval-backed skill audit -->
<!-- Used by: skillify -->

# Eval Design for Skills

Use evals to catch the ways skills actually regress: they fail to trigger, trigger too broadly, route to the wrong skill, skip a gate, or produce the wrong artifact shape.

## Minimum Eval Set

Create at least 8 cases:

1. Should trigger: direct request naming the domain.
2. Should trigger: casual/implicit request that needs the skill.
3. Should trigger: complex case requiring references or scripts.
4. Should not trigger: adjacent task better handled by another skill.
5. Should not trigger: keyword overlap but wrong intent.
6. Delegation-positive case: independent workstreams should produce explicit
   roles, ownership, aggregation, validation, and fallback.
7. Anti-delegation case: a small or tightly coupled workflow should reject
   subagents and stay standalone or serial.
8. Failure-mode case: missing input, missing API key, unavailable subagents,
   unsafe data, or ambiguous scope.

## JSON Shape

Use this shape unless a repo already has a stricter harness:

```json
{
  "skill_name": "skill-name",
  "evals": [
    {
      "id": 1,
      "prompt": "Realistic user prompt",
      "expected_output": "What the agent should do and avoid",
      "assertions": [
        "Specific observable behavior"
      ],
      "files": []
    }
  ]
}
```

## Runnable Promptfoo Coverage

Keep `evals/evals.json` as the human-readable behavior spec. Generate runnable
Promptfoo coverage from it instead of migrating the source format.

For project-scoped skills in this repo:

```bash
uv run .agents/skills/scripts/promptfoo_skill_evals.py --write
uv run .agents/skills/scripts/promptfoo_skill_evals.py --check
```

The generated file lives at:

```text
.agents/skills/<skill-name>/evals/promptfooconfig.yaml
```

Do not edit generated Promptfoo configs by hand. Update `SKILL.md` or
`evals/evals.json`, then regenerate.

Generated Promptfoo configs use two assertion layers:

1. `contains-json` checks the deterministic evaluation report shape and the
   trigger decision (`trigger` or `do_not_trigger`) inferred from
   `expected_output`.
2. `llm-rubric` with a score threshold grades the workflow, validation, safety,
   and artifact-language judgment that cannot be checked reliably with string
   matching.

Validate Promptfoo syntax with the current CLI:

```bash
pnpm dlx promptfoo@latest validate config -c .agents/skills/<skill-name>/evals/promptfooconfig.yaml
```

When `OPENROUTER_API_KEY` is available, run at least one real eval before claiming
the workflow is runnable:

```bash
pnpm dlx promptfoo@latest eval -c .agents/skills/<skill-name>/evals/promptfooconfig.yaml --grader openrouter:deepseek/deepseek-v4-flash --filter-first-n 1 --no-cache --no-progress-bar
```

If the key is missing, config validation is still required. Report the missing
credential as the blocker and include the exact eval command.

## Assertion Quality

Good assertions are observable:

- "Checks for existing `.agents/product-marketing.md` before asking broad positioning questions"
- "Creates `evals/evals.json` with at least one near-miss negative case"
- "Runs `uv run .agents/skills/scripts/validate_skills.py` when a shared project validator exists"
- "Runs `uv run scripts/check_skill.py` and reports the result"
- "Runs `uvx ruff check --no-cache scripts` when Python helper scripts exist"
- "Runs `pnpm dlx @biomejs/biome check scripts` when JavaScript or TypeScript helper scripts exist"
- "Runs `pnpm dlx markdownlint-cli2 \"SKILL.md\" \"references/**/*.md\" \"research-sources/**/*.md\"` and reports the result"
- "Does not put external web snippets into the agent prompt as instructions"
- "Defines a role roster with non-overlapping ownership for parallel subagents"
- "Requires a shared input packet and structured specialist output schema"
- "Aggregates specialist reports before final delivery"
- "Falls back to serial execution when subagents or worker slots are unavailable"
- "Rejects delegation for a tiny linear workflow where a script is simpler"

Weak assertions are vague:

- "Is high quality"
- "Writes good instructions"
- "Follows best practices"

## What to Test by Skill Type

| Skill Type | Test |
| --- | --- |
| Workflow | Order, completion criteria, skipped-step pressure |
| Reference | Retrieval of the right reference and correct application |
| Orchestrator | Routing, fallback, aggregation schema |
| Delegated / multi-agent | role map, independence, ownership boundaries, fan-out/fan-in, conflict handling, fallback |
| Adapter | availability checks, cost guardrails, missing credentials |
| Script-backed | script exists, runs, errors clearly |
| Trend-snapshot | refresh rule, dated source, no permanent "latest" wording |
| Security-gated | unsafe input treated as data, not instruction |

## Baseline Testing

When subagents or fresh sessions are available:

1. Run the same eval without the skill.
2. Record the failure or rationalization.
3. Run with the skill.
4. Tighten only the rules that address observed failures.

If independent baseline testing is unavailable, do not pretend it was done. Create the evals, run static validation, and mark forward-testing as pending.
