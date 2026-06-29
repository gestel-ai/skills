<!-- Sources: references/source-repos/MANIFEST.md, source path listed below -->
<!-- Used by: gestel-blog-seo-check -->

# Provenance

This skill is a local standardization of license-compatible source material. It does not copy upstream runtime scripts, provider adapters, generated assets, or hidden credential assumptions. The records below are attribution only; the skill does not depend on the top-level `references/` tree to run.

## Source Map

- Source path: `references/skills/claude-blog/skills/blog-seo-check/SKILL.md`
- Upstream path: `references/source-repos/claude-blog/skills/blog-seo-check/SKILL.md`
- Commit: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- License: MIT
- Notice: `references/source-repos/claude-blog/NOTICE`

## Related Source Commits (attribution only, not runtime dependencies)

- claude-ads: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- claude-blog: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- claude-seo: `d830cdb2ad339bb7f062339fe82228b072e98061`
- marketingskills: `8bfcdffb655f16e713940cd04fb08891899c47db`

## Local Changes

- Converted the source into a project-local, self-contained skill with trigger-focused frontmatter (triggers, near-miss routing, and the no-credentials/no-paid-provider/no-live-mutation/no-upstream-scripts boundary).
- Distilled the full validation workflow, per-step pass/fail checklists, link-dedup logic, FLOW evidence triple, status vocabulary, and report template into `SKILL.md`.
- Moved freshness-sensitive numeric thresholds (title/meta windows, og:image spec, Twitter Card limits, URL-length norms, crawler/robots policy) into `references/seo-check-reference.md` with dated caveats.
- Converted the source's "Live Performance Check (blog-google)" step — which depends on upstream `scripts/run.py`, a credential check, and a PageSpeed adapter — from a feature into an explicit Boundary.
- Added an UNVERIFIED status so missing-context checks are never reported as PASS.
- Preserved the source as reference material rather than executable instructions.
