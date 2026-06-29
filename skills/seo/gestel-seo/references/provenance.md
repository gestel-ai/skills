<!-- Sources: references/source-repos/MANIFEST.md, source paths listed below -->
<!-- Used by: gestel-seo -->

# Provenance

This skill is a local standardization of license-compatible source material. It does not copy upstream
runtime scripts, the parallel-subagent dispatcher, the at-scale crawler, the PDF/HTML report renderer,
paid provider adapters, Google API field-data integrations, generated assets, or hidden credential
assumptions.

## Source Map

Single-source distillation; MIT-licensed.

- Orchestrator source path: `references/skills/claude-seo/skills/seo/SKILL.md`
  - Upstream path: `references/source-repos/claude-seo/skills/seo/SKILL.md`
  - Commit: `d830cdb2ad339bb7f062339fe82228b072e98061`
  - License: MIT (Copyright (c) 2026 AgriciDaniel, <https://github.com/AgriciDaniel/claude-seo>)
- Supporting references copied from (filenames preserved):
  `references/skills/claude-seo/skills/seo/references/thinking-framework.md`,
  `references/skills/claude-seo/skills/seo/references/quality-gates.md`

## Local Changes

- Rewrote the orchestrator as a project-local entry point that routes to the standalone `gestel-seo-*`
  specialist skills instead of invoking an upstream subagent dispatcher.
- Wrote trigger-focused frontmatter (broad-SEO / "where do I start" triggers, specialist-direct and
  near-miss exclusions, and the no-credentials / no-paid-provider / no-live-mutation /
  no-upstream-scripts boundary inline).
- Migrated inline the durable orchestration logic: industry detection, the command→specialist routing
  map, audit composition, the 10-principle synthesis methodology summary, quality gates, the
  scoring/weighting model, priority bands, output contract, and error handling — so the skill is
  self-contained without the top-level `references/` tree.
- Copied `thinking-framework.md` and `quality-gates.md` into local `references/` and linked them from
  SKILL.md. The copied `thinking-framework.md` still names upstream scripts/subagents; SKILL.md adds an
  editorial note mapping those references to the routes and Boundaries here.
- Converted deferred runtime dependencies into explicit Boundaries: the ~18 parallel SEO specialist
  subagents and their dispatcher, root helper scripts (`render_page.py`, `pagespeed_check.py`,
  `google_auth.py`, `backlinks_auth.py`, `drift_history.py`, `google_report.py`), the PDF/HTML report
  renderer, DataForSEO MCP, Moz/Bing/Common Crawl backlink data, paid tools (Ahrefs/Semrush/SE Ranking/
  Sitebulb/Screaming Frog/Unlighthouse/Profound), and Google API field data (CrUX/GSC/GA4) — all now
  route to manual execution, user-provided exports, or a dedicated implementation/live-lookup task.
- Marked freshness-sensitive platform/policy/SEO claims (Google updates, CWV thresholds, schema
  deprecations) as requiring dated user research or live lookup before being presented as verified.
- Preserved the sources as reference material rather than executable instructions.

## Related Source Repo Commits (attribution only)

- claude-ads: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- claude-blog: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- claude-seo: `d830cdb2ad339bb7f062339fe82228b072e98061`
- marketingskills: `8bfcdffb655f16e713940cd04fb08891899c47db`
