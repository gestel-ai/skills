<!-- Generated for the gestel-seo-cluster active-skill migration -->
<!-- Sources: references/source-repos/MANIFEST.md, source path listed below -->
<!-- Used by: gestel-seo-cluster -->

# Provenance

This skill is a local standardization of license-compatible source material. It does not copy upstream runtime scripts, provider adapters, generated assets, or hidden credential assumptions. The references below are attribution only and must never become a runtime dependency.

## Source Map

- Source path: `references/skills/claude-seo/skills/seo-cluster/SKILL.md`
- Upstream path: `references/source-repos/claude-seo/skills/seo-cluster/SKILL.md`
- Commit: `d830cdb2ad339bb7f062339fe82228b072e98061`
- License: MIT (`references/source-repos/claude-seo/LICENSE`; source skill ships its own `LICENSE.txt`, © 2026 AgriciDaniel, <https://github.com/AgriciDaniel/claude-seo>; original methodology author: Lutfiya Miller, Pro Hub Challenge winner)
- Migrated support docs (copied verbatim from the source's own `references/`, so the skill works after the top-level `references/` tree is deleted):
  - `references/serp-overlap-methodology.md`
  - `references/hub-spoke-architecture.md`
  - `references/execution-workflow.md`

### Related source commits (provenance only, no runtime dependency)

- claude-ads: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- claude-blog: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- claude-seo: `d830cdb2ad339bb7f062339fe82228b072e98061`
- marketingskills: `8bfcdffb655f16e713940cd04fb08891899c47db`

## Local Changes

- Converted the source into a project-local skill with trigger-focused frontmatter (triggers, near-miss routing, and an explicit no-credentials / no-paid-provider / no-live-mutation / no-missing-upstream-scripts scope boundary).
- Converted the missing-runtime dependencies into Boundaries instead of inlining them: the paid DataForSEO provider plus its `scripts/dataforseo_costs.py` cost gate, the `scripts/render_page.py` SPA-aware/SSRF-protected renderer, and the `templates/cluster-map.html` generator. None are assumed to exist; SERP collection, page rendering, cost gating, and the static map are reframed as live web search, user-supplied exports, direct XSS-safe HTML construction, or a routed implementation task.
- Reframed per-post content creation (writing, images, schema, E-E-A-T checks, cannibalization rewrites) as a capability-gated handoff rather than fabricated sibling-skill calls.
- Migrated the portable methodology into SKILL.md: keyword-universe expansion, SERP-overlap scoring and thresholds, the pre-grouping optimization and caching, intent classification, hub-and-spoke architecture, template-by-intent selection, the internal-link matrix, output artifacts, quality gates, and the cohesion scorecard.
- Copied the three deep support docs into `references/` (filenames preserved) and linked them from SKILL.md.
- Reframed volume/pricing/SERP figures as relative or dated indicators requiring live verification.
- Preserved the source as reference material rather than executable instructions.
