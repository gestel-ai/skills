<!-- Generated for the gestel-seo-hreflang active-skill migration -->
<!-- Sources: references/source-repos/MANIFEST.md, source path listed below -->
<!-- Used by: gestel-seo-hreflang -->

# Provenance

This skill is a local standardization of license-compatible source material. It does not copy upstream runtime scripts, provider adapters, generated assets, or hidden credential assumptions. The references below are attribution only and must never become a runtime dependency.

## Source Map

- Source path: `references/skills/claude-seo/skills/seo-hreflang/SKILL.md`
- Upstream path: `references/source-repos/claude-seo/skills/seo-hreflang/SKILL.md`
- Commit: `d830cdb2ad339bb7f062339fe82228b072e98061`
- License: MIT (`references/source-repos/claude-seo/LICENSE`; source skill ships its own `LICENSE.txt`, © 2026 AgriciDaniel, <https://github.com/AgriciDaniel/claude-seo>; original cultural/parity/locale methodology author: Chris Muller, Pro Hub Challenge)
- Migrated support docs (copied verbatim from the source's own `references/`, so the skill works after the top-level `references/` tree is deleted):
  - `references/cultural-profiles.md`
  - `references/content-parity.md`
  - `references/locale-formats.md`
  - `references/machine-translation-qa.md`

### Related source commits (provenance only, no runtime dependency)

- claude-ads: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- claude-blog: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- claude-seo: `d830cdb2ad339bb7f062339fe82228b072e98061`
- marketingskills: `8bfcdffb655f16e713940cd04fb08891899c47db`

## Local Changes

- Converted the source into a project-local skill with trigger-focused frontmatter (triggers, near-miss routing, and an explicit no-credentials / no-paid-provider / no-live-mutation / no-missing-upstream-scripts scope boundary).
- Migrated the portable methodology into SKILL.md: the eight core validation checks (self-reference, return tags, x-default, ISO 639-1 language and ISO 3166-1 region codes, canonical alignment, protocol consistency, cross-domain), the common-mistake table, the three implementation methods with code examples (HTML link tags, HTTP headers, XML sitemap), the seven-step generation workflow, the validation-report shape, and the four deeper-audit passes (cultural adaptation, content parity, locale formats, machine-translation QA).
- Converted the skill's "could not run locally" gap into Boundaries rather than inlining capabilities: no authenticated crawling, no paid SERP/crawl providers, no browser automation, no live-account mutation, and no assumed upstream runtime scripts. Live crawling, SERP fetches, and JS rendering at scale are routed out.
- Reframed freshness-sensitive facts (Google ranking/indexing behavior, the Jan 2025 Quality Rater Guidelines §4.6.5 machine-translation-abuse language and its version/date, marketplace/regulatory policy) as provisional claims requiring user-supplied dated research or a live lookup before being asserted as verified.
- Copied the four deep support docs into `references/` (filenames preserved) and linked them on-demand from SKILL.md.
- Preserved the source as reference material rather than executable instructions.
