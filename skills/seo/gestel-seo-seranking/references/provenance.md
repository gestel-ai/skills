<!-- Sources: references/source-repos/MANIFEST.md, source path listed below -->
<!-- Used by: gestel-seo-seranking -->

# Provenance

This skill is a local standardization of license-compatible source material. It does not
copy upstream runtime scripts, provider adapters, generated assets, or hidden credential
assumptions.

## Source Map

- Source path: `references/skills/claude-seo/extensions/seranking/skills/seo-seranking/SKILL.md`
- Upstream path: `references/source-repos/claude-seo/extensions/seranking/skills/seo-seranking/SKILL.md`
- Related upstream doc (provider-bound, not migrated as runtime): `references/source-repos/claude-seo/extensions/seranking/docs/SERANKING-SETUP.md`
- Commit: `d830cdb2ad339bb7f062339fe82228b072e98061`
- License: MIT (`references/source-repos/claude-seo/LICENSE`)
- Migrated support docs: none — the source skill folder contained no `references/` or
  `evals/` files to copy. All migrated methodology lives in this skill's `SKILL.md`.

### Related source commits (provenance only, no runtime dependency)

- claude-ads: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- claude-blog: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- claude-seo: `d830cdb2ad339bb7f062339fe82228b072e98061`
- marketingskills: `8bfcdffb655f16e713940cd04fb08891899c47db`

## Local Changes

- Converted the source into a project-local skill with trigger-focused frontmatter.
- Converted the live SE Ranking REST API, the `SERANKING_API_KEY` gate, the
  `install.sh`/`install.ps1`/`uninstall.sh` installer, the `/seo seranking …` live
  commands, and the unit-cost accounting (`~5 units/query`, `dataforseo_costs.py`) into
  Boundaries; live numbers route to a SE Ranking adapter or user-supplied exports.
- Migrated and deepened the portable methodology: AI Share-of-Voice prompt-set design,
  the mention/citation/position/sentiment scoring rubric, the SoV and competitive-SoV
  formulas, sample-size confidence tiers, cross-surface interpretation, and the
  SERP / backlink / competitor-gap / tracking frameworks.
- Preserved the source as reference material rather than executable instructions.
