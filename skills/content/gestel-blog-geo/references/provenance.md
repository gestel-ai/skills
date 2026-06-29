<!-- Sources: references/source-repos/MANIFEST.md, source paths listed below -->
<!-- Used by: gestel-blog-geo -->

# Provenance

This skill is a local standardization of license-compatible source material. It
does not copy upstream runtime scripts, provider adapters, generated assets, or
hidden credential assumptions. The records below are attribution only — the skill
runs from its own `SKILL.md` and local `references/`, with no dependency on the
top-level `references/` tree.

## Source Map

- Primary source path: `references/skills/claude-blog/skills/blog-geo/SKILL.md`
- Support doc copied: `references/skills/claude-blog/skills/blog/references/geo-optimization.md`
  → `references/geo-optimization.md` (filename preserved, freshness header prepended)
- Upstream path: `references/source-repos/claude-blog/skills/blog-geo/SKILL.md`
- Commit: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- License: MIT
- Notice: `references/source-repos/claude-blog/NOTICE`

## Related Source Commits (attribution context only)

- claude-blog: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- claude-ads: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- claude-seo: `d830cdb2ad339bb7f062339fe82228b072e98061`
- marketingskills: `8bfcdffb655f16e713940cd04fb08891899c47db`

## Local Changes

- Converted the source into a project-local skill with trigger-focused frontmatter.
- Distilled the full audit process, 0-100 scoring model, citation-capsule format,
  and report template into `SKILL.md` so the skill is self-contained.
- Copied the deep benchmark library into `references/geo-optimization.md` and added
  a freshness warning header.
- Converted the source's live-lookup steps (GSC adapter, upstream `scripts/run.py`)
  from features into explicit Boundaries, since this skill runs from project files
  only — no credentials, paid providers, live-account mutation, or upstream scripts.
- Marked all freshness-sensitive platform statistics as dated hypotheses requiring
  re-verification rather than verified facts.
