<!-- Updated: 2026-06-26 | v1.0 -->
<!-- Sources: OpenAI Codex Agent Skills docs fetched 2026-06-26, Open Agent Skills specification, local skill pattern audit -->
<!-- Used by: skillify -->

# Skill Design Patterns

Use this reference when deciding how to structure a new or revised skill.

## Pattern Selection

| Pattern | Use When | Include | Avoid |
| --- | --- | --- | --- |
| Standalone skill | One repeated task has a clear workflow | `SKILL.md`, optional evals | Extra folders without a job |
| Orchestrator + sub-skills | A suite has many related commands or specialists | Router, command table, sub-skill map, aggregation contract | One giant skill that owns every branch |
| Delegated team / multi-agent orchestrator | Independent workstreams, shards, platforms, locales, or review roles can run concurrently and synthesize into one result | Role roster, ownership map, shared input packet, output schema, fan-out/fan-in gate, fallback | Parallel agents touching the same files or solving the same root cause |
| Eval-backed skill | Triggering, delegation, or output shape can regress | `evals/evals.json`, should/should-not trigger prompts | Vague assertions like "good quality" |
| Script-backed skill | Work is deterministic, fragile, or repeated | `scripts/`, command examples, failure handling | Asking the model to rewrite the same parser/checker every run |
| Adapter skill | External API/MCP/CLI supplies live data | availability check, auth check, cost/rate limits, fallback | Silent failure when credentials are absent |
| Shared-context skill | Many skills need the same product/brand/domain context | canonical file path, precedence rules, update workflow | Multiple competing context files |
| Trend-snapshot skill | Rules change with platforms, policies, or markets | dated reference, source list, refresh rule | Permanent "latest" claims in `SKILL.md` |
| Research-provenance skill | Rules depend on freshness-sensitive or evidence-critical research | optional `research-sources/`, source comments, traceable distilled references | Adding research folders to every skill by default |
| Security-gated skill | It loads user files, web snippets, generated research, or root docs | untrusted-data fence, provenance, size/path checks | Treating retrieved text as instructions |

## Architecture Rules

- Split by invocation only when the new skill has a distinct trigger word.
- Split by sequence only when later steps cause premature completion of earlier steps.
- Keep detailed variants one level below `SKILL.md`; avoid deep reference chains.
- Use one canonical source for each rule. If a rule appears in `SKILL.md`, do not repeat it in a reference unless the reference owns the detail and the body only points to it.
- For suites, make the top-level skill responsible for routing, shared context, aggregation, and cross-skill safety. Let sub-skills own narrow execution.
- Use parallel subagents only after the problem is split into independent
  domains. The unit of parallelism is a problem domain, not an agent count.
- Keep a controller role. The controller scopes each task, supplies the context
  packet, reviews returned artifacts, integrates outputs, and runs final
  verification.
- Require disjoint write ownership for parallel code or file edits. If agents
  would edit the same files, records, manifest, branch, quota, or artifact path,
  make the workflow serial or read-only.
- Avoid delegation for simple one-turn edits, small formatting workflows,
  related failures, exploratory debugging before decomposition, or tasks that
  require whole-system context.
- Keep raw research separate from operational reference. The agent should execute distilled rules, while maintainers can trace the rules back to research sources.
- Create `research-sources/` only after a research gate says the skill needs user-provided source reports for freshness, claims, benchmarks, platform behavior, policy, pricing, law, or other evidence-critical material.

## Delegation Decision

Every non-trivial skill design should name one of these decisions:

- `none`: one agent or a deterministic script is simpler and lower-risk.
- `serial-specialist`: a specialist, reviewer, or validator runs after the main
  work because the output depends on earlier state.
- `parallel-fanout`: independent shards can run at the same time and report into
  one aggregation step.
- `orchestrated-team`: a router assigns roles, manages dependencies, validates
  specialist outputs, resolves conflicts, and owns final delivery.

Use `parallel-fanout` for read-heavy audits, independent locale/page/package
checks, separated candidate batches, or independent test failures. For coding
work, prefer bounded ownership by file or module and review the merged result.
Do not dispatch parallel writers until ownership, result paths, duplicate
checks, and final verification are clear.

## Context Ladder

1. `description`: trigger conditions only.
2. `SKILL.md`: the workflow every valid run needs.
3. `references/`: branch-specific details, examples, policies, frameworks, dated snapshots.
4. `scripts/`: deterministic checks, parsing, rendering, report generation, cost accounting.
5. `assets/`: templates or media used in outputs, not read as instructions.

## Orchestrator Contract

An orchestrator should define:

- Command or branch routing table.
- Shared prerequisites and context intake.
- Which sub-skills are user-facing and which are internal-only.
- Role roster with each specialist's responsibility and write ownership.
- Dependency graph: what can run in parallel and what must wait.
- Shared context packet passed to every specialist.
- Aggregation schema for specialist outputs.
- Conflict-resolution policy when specialists disagree.
- Validation gate before final delivery.
- Fallback path when subagents, MCPs, APIs, or scripts are unavailable.

## Adapter Contract

An adapter should define:

- How to detect whether the tool/API/MCP is available.
- What credentials are required and where they are expected.
- Cost/rate-limit guardrails before calls.
- Structured output shape.
- Fallback behavior when unavailable.
- What the agent may cache in-session to avoid repeated cost.

## Shared-Context Contract

A shared-context skill should define:

- Canonical path.
- Migration path for legacy filenames.
- Precedence when multiple context files exist.
- Whether files are trusted instructions or untrusted data.
- Which downstream skills consume the context.
- Update workflow that preserves user-authored facts.
