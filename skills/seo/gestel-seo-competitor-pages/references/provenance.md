<!-- Sources: references/source-repos/MANIFEST.md, source path listed below -->
<!-- Used by: gestel-seo-competitor-pages -->

# Provenance

This skill is a local standardization of license-compatible source material. It does not copy upstream runtime scripts, provider adapters, install wiring, generated assets, or hidden credential assumptions.

## Source Map

- Source path: `references/skills/claude-seo/skills/seo-competitor-pages/SKILL.md`
- Upstream path: `references/source-repos/claude-seo/skills/seo-competitor-pages/SKILL.md`
- Commit: `d830cdb2ad339bb7f062339fe82228b072e98061`
- License: MIT (`references/source-repos/claude-seo/LICENSE`)
- Note: the source skill shipped only a single `SKILL.md` plus `LICENSE.txt` (no `references/` or `evals/` subdirectory), so there were no upstream support documents to copy. All portable methodology was distilled directly into the local `SKILL.md`.

### Related source commits (provenance only, no runtime dependency)

- claude-ads: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- claude-blog: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- claude-seo: `d830cdb2ad339bb7f062339fe82228b072e98061`
- marketingskills: `8bfcdffb655f16e713940cd04fb08891899c47db`

## Local Changes

- Converted the source into a project-local skill with trigger-focused frontmatter (page-type triggers, near-miss vs scraper/rank-tracker/backlink-tool, and the "no hidden credentials / paid provider / live mutation / missing upstream scripts" scope statement).
- Converted the source's freshness-sensitive assertions — competitor pricing/feature accuracy, schema rich-result rendering behavior, and "current year" keyword freshness tactics — into a single explicit freshness Boundary: such claims are not settled until backed by user-provided dated research or a live lookup. This skill was originally deferred because it leans on freshness-sensitive platform/SEO/marketplace facts; that dependency is now a Boundary, not an assumed capability.
- Migrated the portable methodology in full: the four page types (X vs Y, alternatives, roundup, matrix), feature-matrix construction rules (buyer-priority rows, honest three-state cells, sourced/dated cells), the Product/SoftwareApplication/ItemList JSON-LD shapes, competitive-intent keyword patterns with title/H1 formulas, conversion layout (CTA placement, social proof, pricing highlights, trust signals), fairness guidelines, internal linking, the output contract, and error/degradation handling.
- Added an Untrusted Data Handling section and an Output Contract aligned with the other gestel-seo-* skills.
- Preserved the source as reference material rather than executable instructions.

These provenance files are an attribution record only. They must not become a runtime dependency: the skill is designed to work after the top-level `references/` tree is deleted.
