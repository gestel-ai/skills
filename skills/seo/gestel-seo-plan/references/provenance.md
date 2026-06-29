<!-- Sources: references/source-repos/MANIFEST.md, source paths listed below -->
<!-- Used by: gestel-seo-plan -->

# Provenance

This skill is a local standardization of license-compatible source material. It does not copy upstream
runtime scripts, an at-scale crawler, a subagent dispatcher, a report renderer, paid provider adapters
(DataForSEO/Ahrefs/Semrush/Moz), Google API field-data integrations, real metric assumptions, or
hidden credential assumptions.

## Source Map

Single MIT-licensed source.

- Methodology source path: `references/skills/claude-seo/skills/seo-plan/SKILL.md`
  - Upstream path: `references/source-repos/claude-seo/skills/seo-plan/SKILL.md`
  - Commit: `d830cdb2ad339bb7f062339fe82228b072e98061`
  - License: MIT (Copyright (c) 2026 AgriciDaniel, <https://github.com/AgriciDaniel/claude-seo>)
- Supporting industry templates copied from (filenames preserved), originally in the source `assets/`:
  `references/skills/claude-seo/skills/seo-plan/assets/saas.md`,
  `.../assets/local-service.md`, `.../assets/ecommerce.md`, `.../assets/publisher.md`,
  `.../assets/agency.md`, `.../assets/generic.md`

## Local Changes

- Inlined the stable methodology into a self-contained `SKILL.md`: the six planning phases (discovery,
  competitive analysis, architecture, content strategy, technical foundation, implementation roadmap),
  the four-phase 12-month rollout, the KPI frame, the per-page-type schema-plan approach, and the
  industry-template routing — so the skill works without the top-level `references/` tree.
- Copied the six industry templates into local `references/` (filenames preserved) and linked them from
  `SKILL.md`; no dependency on the top-level `references/` tree at runtime.
- Wrote trigger-focused frontmatter (triggers, near-miss exclusions, and the
  no-credentials / no-paid-provider / no-live-mutation / no-upstream-scripts boundary inline).
- Converted the source's optional **DataForSEO** integration and any assumed crawler/automation/
  real-metrics access into explicit Boundaries: competitor/traffic/keyword/Domain-Authority numbers now
  require user-provided exports or a live-lookup/Deep-Research task and are never fabricated.
- Marked freshness-sensitive material as requiring dated user research or a live lookup before being
  presented as verified. This applies both to the methodology (CWV thresholds, AI-search behavior) and
  to the copied templates, which carry dated platform/policy/statistic claims (e.g. Google News
  inclusion, GBP/SAB policy, FAQPage rich-result status, conversion-rate figures). The templates'
  stable structure (architecture trees, schema mappings, content tiers) is durable; their dated claims
  are not asserted as current without verification.
- Preserved the source as reference material rather than executable instructions, and preserved
  the MIT license/attribution.

## Related Source Repo Commits (attribution only)

- claude-ads: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- claude-blog: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- claude-seo: `d830cdb2ad339bb7f062339fe82228b072e98061`
- marketingskills: `8bfcdffb655f16e713940cd04fb08891899c47db`
