<!-- Sources: references/source-repos/MANIFEST.md, source path listed below -->
<!-- Used by: gestel-blog-factcheck -->

# Provenance

This skill is a local standardization of license-compatible source material. It
does not copy upstream runtime scripts, provider adapters, generated assets, live
fetch tooling, or hidden credential assumptions.

## Source Map

- Source path: `references/skills/claude-blog/skills/blog-factcheck/SKILL.md`
- Upstream path: `references/source-repos/claude-blog/skills/blog-factcheck/SKILL.md`
- Commit: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- License: MIT
- Notice: `references/source-repos/claude-blog/NOTICE`

### Related source-repo commits (attribution only)

- claude-ads: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- claude-blog: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- claude-seo: `d830cdb2ad339bb7f062339fe82228b072e98061`
- marketingskills: `8bfcdffb655f16e713940cd04fb08891899c47db`

## Local Changes

- Converted the source into a project-local skill with trigger-focused frontmatter.
- Split "verify" into offline structural verification (always available) and
  factual verification (gated behind user-supplied or live-fetched evidence),
  because the source assumed live `WebFetch` of cited URLs.
- Added a freshness guard so platform/SEO/marketplace/pricing claims cannot be
  asserted true without dated evidence — converting the original live-research
  blocker into a guardrail rather than a hard dependency.
- Lifted the source's extraction patterns, scoring rubric, evidence triple, and
  report templates into `references/factcheck-methodology.md`.
- Moved source-specific safe/unsafe boundaries into `references/source-usage.md`.
- Preserved the source as reference material rather than executable instructions.

These records are attribution only. The skill does not depend on the top-level
`references/` tree to run.
