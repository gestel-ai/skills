<!-- Used by: gestel-blog-google -->

# Provenance

This skill is a local standardization of license-compatible source material. It does not copy upstream runtime scripts, provider adapters, generated assets, or hidden credential assumptions.

## Source Map

- Source path: `references/skills/claude-blog/skills/blog-google/SKILL.md`
- Upstream path: `references/source-repos/claude-blog/skills/blog-google/SKILL.md`
- Commit: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- License: MIT
- Notice: `references/source-repos/claude-blog/NOTICE`

### Support docs copied verbatim (read-only reference)

- `references/api-reference.md` ← source `references/api-reference.md`
- `references/auth-setup.md` ← source `references/auth-setup.md`
- `references/rate-limits-quotas.md` ← source `references/rate-limits-quotas.md`

## Related upstream commits (attribution only)

- claude-ads: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- claude-blog: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- claude-seo: `d830cdb2ad339bb7f062339fe82228b072e98061`
- marketingskills: `8bfcdffb655f16e713940cd04fb08891899c47db`

## Local Changes

- Converted the source into a project-local skill with trigger-focused frontmatter.
- Dropped the source's executable `scripts/` client and the shared
  `~/.config/claude-seo/google-api.json` credential file; this skill makes no live
  calls and holds no credentials.
- Converted every provider-bound feature (PSI/CrUX/GSC/GA4/NLP/YouTube/Keyword
  Planner) into local interpretation frameworks plus explicit provider-adapter
  Boundaries that route live access out to a configured adapter or user-provided data.
- Copied the three source support docs into `references/` as read-only reference
  for reading payloads and for adapter authors; the skill does not depend on them
  to run.
- Preserved the source as reference material rather than executable instructions.

These records are attribution only and must not become a runtime dependency.
