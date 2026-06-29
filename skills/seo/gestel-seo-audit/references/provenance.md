<!-- Sources: references/source-repos/MANIFEST.md, source paths listed below -->
<!-- Used by: gestel-seo-audit -->

# Provenance

This skill is a local standardization of license-compatible source material. It does not copy upstream
runtime scripts, the at-scale crawler, the parallel-subagent dispatcher, the PDF report renderer, paid
provider adapters, Google API field-data integrations, generated assets, or hidden credential
assumptions.

## Source Map

This is a two-source merge; both are MIT-licensed.

- Primary methodology source path: `references/skills/marketingskills/skills/seo-audit/SKILL.md`
  - Upstream path: `references/source-repos/marketingskills/skills/seo-audit/SKILL.md`
  - Commit: `8bfcdffb655f16e713940cd04fb08891899c47db`
  - License: MIT
- Scoring/orchestration source path: `references/skills/claude-seo/skills/seo-audit/SKILL.md`
  - Upstream path: `references/source-repos/claude-seo/skills/seo-audit/SKILL.md`
  - Commit: `d830cdb2ad339bb7f062339fe82228b072e98061`
  - License: MIT (Copyright (c) 2026 AgriciDaniel, <https://github.com/AgriciDaniel/claude-seo>)
- Supporting references copied from (filenames preserved):
  `references/skills/marketingskills/skills/seo-audit/references/ai-writing-detection.md`,
  `references/skills/marketingskills/skills/seo-audit/references/international-seo.md`

## Local Changes

- Merged the two source skills into one project-local skill, de-duplicating overlapping technical/
  on-page/content coverage while preserving each source's unique value: marketingskills supplies the
  hands-on, manually-runnable methodology and i18n depth; claude-seo supplies the health-score weighting
  model, the structured audit-data envelope, priority definitions, and error handling.
- Wrote trigger-focused frontmatter (triggers, near-miss exclusions, and the
  no-credentials / no-paid-provider / no-live-mutation / no-upstream-scripts boundary inline).
- Inlined the full technical, on-page, content, international, and AI-readiness checklists plus the
  scoring weights and priority bands so the skill is self-contained.
- Copied `ai-writing-detection.md` and `international-seo.md` into local `references/` and linked them
  from SKILL.md; no dependency on the top-level `references/` tree.
- Converted deferred runtime dependencies into explicit Boundaries: the at-scale crawler and
  `render_page.py`, the ~15 parallel SEO specialist subagents, `google_report.py` (PDF/HTML report),
  the drift baseline store, DataForSEO MCP, Moz/Bing/Common Crawl backlink data, paid tools
  (Ahrefs/Semrush/Sitebulb/Screaming Frog), and Google API field data (CrUX/GSC/GA4) now route to manual
  execution, user-provided exports, or a dedicated implementation/live-lookup task.
- Marked freshness-sensitive platform/policy/SEO claims as requiring dated user research or live lookup
  before being presented as verified.
- Preserved the sources as reference material rather than executable instructions.

## Related Source Repo Commits (attribution only)

- claude-ads: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- claude-blog: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- claude-seo: `d830cdb2ad339bb7f062339fe82228b072e98061`
- marketingskills: `8bfcdffb655f16e713940cd04fb08891899c47db`
