<!-- Sources: references/source-repos/MANIFEST.md, source path listed below -->
<!-- Used by: gestel-seo-content-brief -->

# Provenance

This skill is a local standardization of license-compatible source material. It does not copy upstream runtime scripts, provider adapters, generated assets, or hidden credential assumptions. This file records attribution only; it must not become a runtime dependency.

## Source Map

- Source path: `references/skills/claude-seo/skills/seo-content-brief/SKILL.md`
- Upstream path: `references/source-repos/claude-seo/skills/seo-content-brief/SKILL.md`
- Commit: `d830cdb2ad339bb7f062339fe82228b072e98061`
- License: MIT (Copyright (c) 2026 puneetindersingh, <https://github.com/AgriciDaniel/claude-seo>)
- Notice: `references/source-repos/claude-seo/NOTICE`

### Adapted reference files

- `references/page-type-templates.md` <- source `references/page-type-templates.md`
- `references/keyword-density.md` <- source `references/keyword-density.md`
- `references/excluded-domains.md` <- source `references/excluded-domains.md`

## Related upstream commits (attribution only, not dependencies)

- claude-ads: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- claude-blog: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- claude-seo: `d830cdb2ad339bb7f062339fe82228b072e98061`
- marketingskills: `8bfcdffb655f16e713940cd04fb08891899c47db`

## Local Changes

- Converted the source into a project-local self-contained skill with trigger-focused frontmatter.
- Migrated the full methodology (brief modes, SERP/gap scoring, intent classification, density and meta rules, information gain, E-E-A-T, internal linking, output formats) into the local SKILL.md so it works if the top-level `references/` tree is removed.
- Copied the three source reference files locally (filenames preserved) and linked them from SKILL.md.
- Converted the "cannot run locally" parts into explicit Boundaries: freshness-sensitive SERP/volume/difficulty/platform claims require live lookups or user-provided dated research and are never invented; no live account mutation; optional SEO MCPs are not assumed present.
- Moved safe/unsafe-use boundaries into `references/source-usage.md`.
- Preserved the source as reference material rather than executable instructions.
