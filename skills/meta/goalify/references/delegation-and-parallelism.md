<!-- Updated: 2026-06-26 | v1.0 -->
<!-- Sources: local Codex subagent tool guidance, bundled superpowers subagent guidance, project skill migration audit -->
<!-- Used by: goalify -->

# Delegation and Parallelism in Goal Prompts

Use this reference when a Goal may benefit from subagents, multi-agent
execution, parallel workers, or an agent-team split.

## Core Rule

Parallelism is an execution policy, not the Goal's success condition. The Goal
still needs one measurable end state, verification evidence, constraints,
checkpoints, progress reporting, and a blocked stop condition.

The main agent remains the controller. It owns task decomposition, context
packets, worker scopes, aggregation, conflict resolution, and final
verification. A worker report is not evidence by itself.

## When To Add Delegation

Add a delegation plan when the task has independent lanes such as:

- packages, modules, files, locales, pages, platforms, tenants, or candidate
  batches that can be inspected independently
- unrelated test failures with distinct root-cause domains
- separate audit lanes, for example performance, security, accessibility, data
  flow, copy, or legal review
- research lanes where each worker checks a different source set and returns
  structured findings
- generation shards with fixed ownership, result paths, duplicate checks, and
  aggregation rules
- user-explicit requests for subagents, multi-agent work, agent teams, parallel
  workers, or maximum worker fan-out

Use serial specialist review, not parallel implementation, when the output of
one role must feed the next role. Examples: implementer then spec reviewer then
code-quality reviewer; writer then editor; migration then verifier.

## When Not To Add Delegation

Keep the Goal serial when:

- the task is a small one-turn edit, simple explanation, or tiny formatting job
- the failures may share one root cause
- the work needs whole-system context before it can be decomposed
- workers would edit the same files, branch, database rows, manifest, quota,
  generated artifact path, or provider account
- result collection, ownership, or duplicate detection is not defined yet
- subagents are unavailable, thread slots are exhausted, or the user did not
  authorize agent fan-out where the environment requires explicit authorization

If a broad workload is not safely decomposed yet, make the first checkpoint
"map independent lanes and choose delegation or serial execution" instead of
forcing parallelism immediately.

## Goal Prompt Pattern

When delegation is useful, include these elements in the fenced Goal prompt:

- controller responsibility: the main agent integrates and verifies everything
- role or shard roster: who owns which package, locale, platform, file group, or
  review lane
- non-overlap rule: workers must not edit outside their assigned scope or revert
  other workers' changes
- context packet: exact files, plan, acceptance criteria, commands, and output
  schema each worker receives
- fan-in gate: required fields, reports, diffs, artifacts, scores, or command
  outputs that must be collected before final delivery
- final verification: commands or artifact checks the main agent runs after
  integration
- fallback: what to do if subagents are unavailable or unsafe for the current
  work

Example sentence:

```text
If the repo shows independent package groups, dispatch parallel workers with disjoint package ownership. Each worker must return changed files, test commands, results, and blockers. The main agent must integrate the results, resolve conflicts, run the full verification suite, and fall back to serial execution if ownership is unclear.
```

## Anti-Patterns

- "Use as many agents as possible" without shard ownership and result paths.
- Letting parallel workers edit the same files or generated manifest.
- Treating subagent summaries as final proof.
- Asking the user to manually run every specialist instead of aggregating.
- Making "spawn subagents" part of the completion condition instead of using it
  as an execution policy when it helps.
