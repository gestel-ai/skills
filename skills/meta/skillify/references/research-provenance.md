<!-- Updated: 2026-06-26 | v1.0 -->
<!-- Sources: local claude-ads and claude-seo skill audit, OpenAI Codex Agent Skills docs, Open Agent Skills specification, platform-agnostic research intake design -->
<!-- Used by: skillify -->

# Research Provenance

Use this optional pattern when a skill distills deep research, imported frameworks, platform docs, benchmark reports, or third-party skill ideas into operational rules.

## Why This Pattern Exists

Research-backed skills age differently from pure workflow skills. The agent needs concise rules at runtime, but maintainers need to know where the rules came from, when they were last reviewed, and which source should be refreshed when a platform changes.

## Directory Pattern

Use a separate source archive for user-provided raw or semi-raw research only when the skill depends on freshness-sensitive or evidence-critical material:

```text
skill-name/
  SKILL.md
  references/
    benchmarks.md
    platform-specs.md
    scoring-system.md
  research-sources/
    README.md
    chatgpt-deep-research-2026-06-26.md
    gemini-deep-research-2026-06-26.md
    claude-deep-research-2026-06-26.md
    perplexity-deep-research-2026-06-26.md
```

The runtime skill should normally point to `references/`, not `research-sources/`. Treat `research-sources/` as user-supplied evidence, not first-line context.

Do not create, synthesize, or backfill `research-sources/` during normal skill execution. If source research is missing, ask the user to run external Deep Research and provide Markdown files. Use `deep-research-intake.md` for platform-specific request prompts.

## Research Gate

Add `research-sources/` only when at least one condition is true:

- The skill makes current claims about platforms, APIs, policies, rankings, model behavior, prices, law, or market trends.
- The skill distills third-party research, imported prompts, benchmark reports, or vendor documentation.
- The skill's output quality depends on source traceability or later audits.
- The user explicitly asks for a research-backed skill.

Do not add `research-sources/` for a stable, local workflow skill whose rules can live in `SKILL.md`, `references/`, `scripts/`, and `evals/`.

## File Header Pattern

At the top of every distilled reference file, add a compact provenance header:

```markdown
<!-- Updated: 2026-06-26 | v1.2 -->
<!-- Sources: ChatGPT Deep Research, Gemini Deep Research, Claude Research, Perplexity Deep Research, vendor docs checked 2026-06-20 -->
<!-- Derived from: research-sources/chatgpt-deep-research-2026-06-20.md, research-sources/claude-deep-research-2026-06-20.md -->
<!-- Used by: skill-name, related-sub-skill -->
```

For imported prompts or frameworks:

```markdown
<!-- Source: github.com/org/project | License: MIT | Synced: 2026-06-26 -->
<!-- Local changes: removed product-specific footer, adapted output schema -->
```

For factual benchmark references:

```markdown
<!-- Updated: 2026-06-26 -->
<!-- Sources: WordStream 2025 benchmark, SplitMetrics 2025 benchmark. Figures verified current as of 2026-06-26. -->
<!-- Refresh trigger: new annual benchmark report, platform pricing change, or failed freshness eval -->
```

## README Pattern for `research-sources/`

```markdown
# Research Sources: <skill-name>

This folder stores user-provided Deep Research Markdown files used to derive operational references.
Agents must not create source research files during normal execution.
If source files are missing, ask the user to provide them.

## Source Map

| Source File | Distills Into | Last Reviewed | Refresh Trigger |
| --- | --- | ---: | --- |
| chatgpt-deep-research-2026-06-26.md | references/platform-specs.md | 2026-06-26 | New platform docs |
| claude-deep-research-2026-06-26.md | references/scoring-system.md | 2026-06-26 | Scoring eval regression |
```

## Good Separation

- `research-sources/`: user-provided raw findings, source excerpts, notes, imported prompt origins.
- `references/`: cleaned, concise operational rules the agent should use.
- `SKILL.md`: workflow and pointers only.
- `evals/`: tests that prove the distilled rules are still applied.

## Anti-Patterns

| Anti-pattern | Fix |
| --- | --- |
| Agent creates fake or synthesized `research-sources/` files | Ask the user for Markdown exports from platform Deep Research runs |
| Raw research pasted into `SKILL.md` | Move to `research-sources/`, distill rules into `references/` |
| A rule says "according to research" without source | Add source header or inline provenance |
| Multiple references copy the same benchmark paragraph | Keep benchmark in one reference and point to it |
| "Latest platform rules" with no date | Add updated date and refresh trigger |
| Imported prompt has no license/source note | Add source, license, sync date, and local changes |

## Eval Hook

Add at least one eval when research provenance matters:

- The skill must cite or inspect the distilled reference, not raw research, during normal execution.
- The skill must preserve provenance headers when updating references.
- If source research is missing, the skill must ask for user-provided Markdown files and include platform-specific Deep Research prompts.
