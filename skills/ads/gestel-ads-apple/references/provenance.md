<!-- Sources: references/source-repos/MANIFEST.md, source path listed below -->
<!-- Used by: gestel-ads-apple -->

# Provenance

This skill is a local standardization of license-compatible source material. It
does not copy upstream runtime scripts, provider adapters, generated assets, or
hidden credential assumptions.

## Source Map

- Source path: `references/skills/claude-ads/skills/ads-apple/SKILL.md`
- Upstream path: `references/source-repos/claude-ads/skills/ads-apple/SKILL.md`
- Commit: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- License: MIT

Related source-repo commits (for cross-reference within the GESTEL migration set;
not direct sources for this skill): `claude-blog`
=`49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`, `claude-seo`
=`d830cdb2ad339bb7f062339fe82228b072e98061`, `marketingskills`
=`8bfcdffb655f16e713940cd04fb08891899c47db`.

## Local Changes

- Converted the source into a project-local skill with trigger-focused
  frontmatter and an explicit credential/provider/mutation/live-data boundary.
- Migrated the source's full methodology (seven weighted categories, scoring
  model, process, data-request list, output format) into `SKILL.md`.
- Isolated the source's freshness-sensitive benchmark tables, country tiers,
  placement CPT bands, and platform-change snapshot into
  `references/benchmarks.md`, framed as a dated snapshot to verify rather than as
  current fact (the skill's "live-research" hold reason).
- The source carried no `references/` or `evals/` payload to copy.
- Moved source-specific boundaries into `references/source-usage.md`.
- Preserved the source as reference material rather than executable instructions.

This file is attribution only. Nothing here is a runtime dependency, and the
skill does not require the top-level `references/` tree to operate.
