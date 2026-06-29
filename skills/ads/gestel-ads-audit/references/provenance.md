<!-- Sources: references/source-repos/MANIFEST.md, source path listed below -->
<!-- Used by: gestel-ads-audit -->

# Provenance

This skill is a local standardization of license-compatible source material. It does not copy upstream runtime scripts, the parallel-subagent dispatcher, the PDF report renderer, provider adapters, generated assets, or hidden credential assumptions.

## Source Map

- Source path: `references/skills/claude-ads/skills/ads-audit/SKILL.md`
- Upstream path: `references/source-repos/claude-ads/skills/ads-audit/SKILL.md`
- Supporting references copied from: `references/skills/claude-ads/ads/references/thinking-framework.md`, `references/skills/claude-ads/ads/references/scoring-system.md`
- Commit: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- License: MIT (Copyright (c) 2026 agricidaniel)

## Local Changes

- Converted the source into a project-local skill with trigger-focused frontmatter (triggers, near-miss exclusions, and the no-credentials/no-mutation/no-upstream-scripts boundary inline).
- Inlined the per-platform category checklists, cross-platform checks, scoring algorithm, grading bands, Quick Wins logic, and priority definitions so the skill is self-contained.
- Copied `thinking-framework.md` and `scoring-system.md` into local `references/` (filenames preserved) and linked them from SKILL.md; no dependency on the top-level `references/` tree.
- Converted the deferred runtime dependencies (six parallel audit subagents, `scripts/generate_report.py`, live platform/API access) into explicit Boundaries that route to manual sequential execution or a dedicated implementation task.
- Preserved the source as reference material rather than executable instructions.

## Related Source Repo Commits (attribution only)

- claude-ads: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- claude-blog: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- claude-seo: `d830cdb2ad339bb7f062339fe82228b072e98061`
- marketingskills: `8bfcdffb655f16e713940cd04fb08891899c47db`
