<!-- Sources: references/source-repos/MANIFEST.md, source paths listed below -->
<!-- Used by: gestel-seo-content -->

# Provenance

This skill is a local standardization of license-compatible source material. It does not copy upstream runtime scripts, provider adapters, generated assets, or hidden credential assumptions. The records below are attribution only; the skill does not depend on the top-level `references/` tree to run.

## Source Map

- Source path: `references/skills/claude-seo/skills/seo-content/SKILL.md`
- Shared reference source path: `references/skills/claude-seo/skills/seo/references/eeat-framework.md`
- Upstream path: `references/source-repos/claude-seo/skills/seo-content/SKILL.md`
- Upstream shared reference path: `references/source-repos/claude-seo/skills/seo/references/eeat-framework.md`
- Commit: `d830cdb2ad339bb7f062339fe82228b072e98061`
- License: MIT (Copyright (c) 2026 AgriciDaniel)
- Notice: `references/source-repos/claude-seo/LICENSE`

## Related Source Commits (attribution only, not runtime dependencies)

- claude-ads: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- claude-blog: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- claude-seo: `d830cdb2ad339bb7f062339fe82228b072e98061`
- marketingskills: `8bfcdffb655f16e713940cd04fb08891899c47db`

## Local Changes

- Converted the source into a project-local, self-contained skill with trigger-focused frontmatter (triggers, near-miss routing, and the no-credentials/no-paid-provider/no-live-mutation/no-upstream-scripts boundary).
- Distilled the Who/How/Why heuristic, the four E-E-A-T dimensions and signal checklists, content metrics and topical-coverage floors, the AI-content markers, the GEO/AI-citation signals, the freshness/structure heuristics, and the output format into `SKILL.md`.
- Copied the full E-E-A-T rubric (signal checklists, per-dimension weights, scoring bands, 0-100 guide, improvement-by-band playbook) into `references/eeat-framework.md` so the skill is self-contained.
- Converted the source's freshness-dependent claims (Quality Rater Guideline dates, the Helpful-Content-System-into-core merge, named algorithm-update traffic-drop percentages, AI-search product names/versions/usage counts, rich-result support status, AI-surface citation overlap, RSL/licensing and spam-category specifics) from asserted fact into an explicit freshness-sensitive Boundary; they are usable only as dated defaults pending the user's date-stamped research or a live lookup.
- Converted the source's optional DataForSEO integration from a feature into a no-paid-provider Boundary; the skill assumes no paid provider and never fabricates provider output.
- Preserved the source as reference material rather than executable instructions.
