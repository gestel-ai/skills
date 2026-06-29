<!-- Sources: references/source-repos/MANIFEST.md, source paths listed below -->
<!-- Used by: gestel-seo-page -->

# Provenance

This skill is a local standardization of license-compatible source material. It does not copy upstream
runtime scripts, a page renderer/SPA capture, a PDF/HTML report generator, paid provider adapters
(e.g. DataForSEO), Google API field-data integrations, generated assets, or hidden credential
assumptions.

## Source Map

Single-source migration; MIT-licensed.

- Methodology source path: `references/skills/claude-seo/skills/seo-page/SKILL.md`
  - Upstream path: `references/source-repos/claude-seo/skills/seo-page/SKILL.md`
  - Commit: `d830cdb2ad339bb7f062339fe82228b072e98061`
  - License: MIT (Copyright (c) 2026 AgriciDaniel, <https://github.com/AgriciDaniel/claude-seo>)
- Supporting references copied: none. The source `seo-page/` folder shipped only `SKILL.md` and
  `LICENSE.txt`; it had no `references/` or `evals/` content to copy. The full methodology was inlined
  into the local SKILL.md instead.

## Local Changes

- Wrote trigger-focused frontmatter (triggers, near-miss exclusions routing to gestel-seo-audit /
  gestel-blog-schema / gestel-copywriting / gestel-cro, and the
  no-credentials / no-paid-provider / no-live-mutation / no-upstream-scripts boundary inline).
- Inlined the full single-page methodology — on-page, content-quality, technical-meta, schema, image,
  and Core-Web-Vitals risk checks plus the score-card / issues-by-priority / recommendations / JSON-LD
  output — so the skill is self-contained with no dependency on the top-level `references/` tree.
- Added an explicit per-group scoring model with weights and priority bands.
- Converted the source's optional DataForSEO integration into a Boundary; added boundaries for the
  missing renderer/report generator, paid providers/credentials, field CWV (CrUX/GSC/GA4), and live
  account mutation.
- Marked freshness-sensitive claims (rich-result eligibility/deprecations such as HowTo/FAQ, lazy-loader
  plugin behavior, exact CWV thresholds, OG/Twitter-card spec) as requiring dated user research or a
  live lookup before being presented as verified, while preserving the stable framework around them.
- Preserved the source as reference material rather than executable instructions.

## Related Source Repo Commits (attribution only)

- claude-ads: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- claude-blog: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- claude-seo: `d830cdb2ad339bb7f062339fe82228b072e98061`
- marketingskills: `8bfcdffb655f16e713940cd04fb08891899c47db`
