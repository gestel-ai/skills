<!-- Sources: references/source-repos/MANIFEST.md, source paths listed below -->
<!-- Used by: gestel-seo-local -->

# Provenance

This skill is a local standardization of license-compatible source material. It does not copy upstream
runtime scripts, a page renderer, an at-scale crawler, a local-pack SERP fetcher, a PDF/HTML report
renderer, the DataForSEO MCP adapter, the GBP API / GBP Insights, geo-grid rank trackers, paid
citation/backlink scanners, generated assets, or hidden credential assumptions. The statistics and
platform-status facts it carries are dated reference material, not currently-verified claims.

## Source Map

Single MIT-licensed source.

- Methodology source path: `references/skills/claude-seo/skills/seo-local/SKILL.md`
  - Upstream path: `references/source-repos/claude-seo/skills/seo-local/SKILL.md`
  - Commit: `d830cdb2ad339bb7f062339fe82228b072e98061`
  - License: MIT (Copyright (c) 2026 AgriciDaniel, <https://github.com/AgriciDaniel/claude-seo>)
- Supporting references copied from (filenames preserved), originally under the source's
  `skills/seo/references/`:
  `references/skills/claude-seo/skills/seo/references/local-seo-signals.md`,
  `references/skills/claude-seo/skills/seo/references/local-schema-types.md`

## Local Changes

- Wrote trigger-focused frontmatter (triggers, near-miss exclusions, and the no-credentials /
  no-paid-provider / no-live-mutation / no-upstream-scripts boundary inline).
- Distilled the source's stable methodology inline so the skill is self-contained: business-type
  (brick-and-mortar / SAB / hybrid) and industry-vertical detection, the six weighted analysis
  dimensions (GBP, reviews, local on-page, NAP & citations, local schema, local links/authority) with
  their checklists and scoring guides, the doorway-page "swap test," the three-source NAP cross-check,
  the schema-subtype mapping, the multi-location architecture pattern, the output spec, priority bands,
  and error handling.
- Repointed both support-doc references from the source's `../seo/references/...` paths to local
  `references/...` and copied the files in; no dependency on the top-level `references/` tree.
- Converted the source's freshness-sensitive content — all ranking-factor statistics, GBP feature
  status (Q&A removal, verified badge, etc.), review-platform usage, algorithm-update specifics, and
  AI-local claims — into an explicit [live-research] Boundary: durable as a checklist, but requiring
  dated user research or a live lookup before being presented as verified.
- Converted the source's DataForSEO MCP integration and any live local-pack / GBP / field-data path
  into [missing-runtime] Boundaries (live local-pack position, geo-grid rank, GBP Insights, Domain
  Authority, comprehensive citation/backlink scans) routing to user-provided exports or a
  live-lookup/implementation task, rather than inlining them as available.
- Added the `web_fetch`/`curl` JSON-LD-detection caveat to the schema dimension so the skill does not
  emit false "no schema" findings.
- Preserved the source as reference material rather than executable instructions.

## Related Source Repo Commits (attribution only)

- claude-ads: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- claude-blog: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- claude-seo: `d830cdb2ad339bb7f062339fe82228b072e98061`
- marketingskills: `8bfcdffb655f16e713940cd04fb08891899c47db`
