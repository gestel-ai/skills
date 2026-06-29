<!-- Generated for the gestel-seo-sitemap active-skill migration -->
<!-- Sources: references/source-repos/MANIFEST.md, source path listed below -->
<!-- Used by: gestel-seo-sitemap -->

# Provenance

This skill is a local standardization of license-compatible source material. It does not copy upstream runtime scripts, provider adapters, generated assets, bundled industry-template directories, or hidden credential assumptions. The references below are attribution only and must never become a runtime dependency.

## Source Map

- Source path: `references/skills/claude-seo/skills/seo-sitemap/SKILL.md`
- Upstream path: `references/source-repos/claude-seo/skills/seo-sitemap/SKILL.md`
- Commit: `d830cdb2ad339bb7f062339fe82228b072e98061`
- License: MIT (`references/source-repos/claude-seo/LICENSE`; source skill ships its own `LICENSE.txt`, © 2026 AgriciDaniel, <https://github.com/AgriciDaniel/claude-seo>)
- Migrated support docs: none. The source directory contains only `SKILL.md` and `LICENSE.txt` (no `references/` or `evals/` subfolders), so there were no deep support docs to copy. All portable methodology was distilled directly into `SKILL.md`.

### Related source commits (provenance only, no runtime dependency)

- claude-ads: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- claude-blog: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- claude-seo: `d830cdb2ad339bb7f062339fe82228b072e98061`
- marketingskills: `8bfcdffb655f16e713940cd04fb08891899c47db`

## Local Changes

- Converted the source into a project-local skill with trigger-focused frontmatter (triggers, near-miss routing, and an explicit no-credentials / no-paid-provider / no-live-mutation / no-missing-upstream-scripts scope boundary).
- Migrated the portable methodology into SKILL.md: Mode 1 analysis (the validation checks, quality signals, and the common-issues severity table), Mode 2 generation (process, the 30+/50+ scale quality-gates, the safe-to-scale vs penalty-risk lists), the standard-sitemap and sitemap-index XML formats with the lastmod / priority / changefreq guidance, error handling, and the output artifacts (VALIDATION-REPORT.md, sitemap.xml + index, STRUCTURE.md). Added the explicit 50,000-URL / 50 MB Sitemaps.org file limits and the uncompressed-measurement / gzip note.
- Did NOT inline the source's `../seo-plan/assets/` industry-template dependency. Those templates live in the sibling `gestel-seo-plan` skill; the generation flow routes there or accepts a user-supplied inventory rather than assuming a local templates directory exists.
- Converted the skill's "could not run locally" gap into Boundaries rather than inlining capabilities: no authenticated/live crawling, no paid crawl/SERP providers, no browser automation, no Search Console submission, and no assumed upstream runtime scripts or bundled assets. Live crawling/coverage, Search Console submission, programmatic-scale builds, and industry templates are routed out (gestel-seo-firecrawl / gestel-seo-audit, gestel-seo-google, gestel-seo-programmatic, gestel-seo-plan).
- Reframed freshness-sensitive facts (Google's handling of lastmod/priority/changefreq, indexing/discovery behavior, Search Console submission flows, current platform rules) as provisional claims requiring user-supplied dated research or a live lookup before being asserted as verified.
- Preserved the source as reference material rather than executable instructions.
