<!-- Sources: references/source-repos/MANIFEST.md, source paths listed below -->
<!-- Used by: gestel-seo-technical -->

# Provenance

This skill is a local standardization of license-compatible source material. It does not copy upstream
runtime scripts, the headless renderer, the accessibility-tree scorer, the PageSpeed/CrUX/GSC API
integrations, paid provider adapters (DataForSEO MCP), generated assets, or hidden credential
assumptions.

## Source Map

Single-source migration; MIT-licensed.

- Methodology source path: `references/skills/claude-seo/skills/seo-technical/SKILL.md`
  - Upstream path: `references/source-repos/claude-seo/skills/seo-technical/SKILL.md`
  - Commit: `d830cdb2ad339bb7f062339fe82228b072e98061`
  - License: MIT (Copyright (c) 2026 AgriciDaniel, <https://github.com/AgriciDaniel/claude-seo>)
- Supporting reference copied from (filename preserved):
  `references/skills/claude-seo/skills/seo-technical/references/agent-friendly-pages.md`

## Local Changes

- Renamed to the project-local `gestel-seo-technical` and rewrote frontmatter to be trigger-focused
  (triggers, near-miss exclusions, and the no-credentials / no-paid-provider / no-live-mutation /
  no-upstream-scripts boundary inline).
- Inlined the full 9-category methodology (crawlability incl. AI-crawler robots.txt policy,
  indexability, security headers, URL structure, mobile/mobile-first, Core Web Vitals thresholds,
  structured-data detection caveat, JavaScript rendering guidance, IndexNow) plus the agent-friendly
  (accessibility-tree) audit summary, so the skill is self-contained.
- Copied `agent-friendly-pages.md` into local `references/` and linked it from SKILL.md; no dependency
  on the top-level `references/` tree.
- Converted deferred runtime dependencies into explicit Boundaries: the local helper scripts
  (`agent_ux_check.py`, `render_page.py`, `pagespeed_check.py`, `crux_history.py`, `gsc_inspect.py`),
  the DataForSEO MCP integration, and the Google PSI/CrUX/GSC field-data integrations now route to
  manual browser/DevTools execution, user-provided exports, or a dedicated implementation/live-lookup
  task. The automation is described as absent, never inlined or faked.
- Marked freshness-sensitive claims (AI-crawler tokens, CWV metric timeline, mobile-first-indexing
  status, JS-SEO doc specifics, IndexNow engine support) as requiring dated user research or a live
  lookup before being presented as verified.
- Preserved the source as reference material rather than executable instructions.

## Related Source Repo Commits (attribution only)

- claude-ads: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- claude-blog: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- claude-seo: `d830cdb2ad339bb7f062339fe82228b072e98061`
- marketingskills: `8bfcdffb655f16e713940cd04fb08891899c47db`
