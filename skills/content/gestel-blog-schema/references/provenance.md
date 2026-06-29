<!-- Generated to match .agents/skills/scripts/scaffold_active_skill_migrations.py output -->
<!-- Sources: references/source-repos/MANIFEST.md, source path listed below -->
<!-- Used by: gestel-blog-schema -->

# Provenance

This skill is a local standardization of license-compatible source material. It does not copy upstream runtime scripts, provider adapters, generated assets, or hidden credential assumptions.

## Source Map

- Source path: `references/skills/claude-blog/skills/blog-schema/SKILL.md`
- Upstream path: `references/source-repos/claude-blog/skills/blog-schema/SKILL.md`
- Commit: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- License: MIT
- Notice: `references/source-repos/claude-blog/NOTICE`

## Related Source Repositories (MANIFEST)

These commits are recorded for the broader migration manifest; this skill draws only from `claude-blog`.

- `claude-blog`: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- `claude-ads`: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- `claude-seo`: `d830cdb2ad339bb7f062339fe82228b072e98061`
- `marketingskills`: `8bfcdffb655f16e713940cd04fb08891899c47db`

## Local Changes

- Converted the source into a project-local skill with trigger-focused frontmatter.
- Lifted the source's deep schema templates, property tables, deprecation list, and validation rubric into `references/schema-methodology.md` so the skill is self-contained.
- Isolated the source's freshness-sensitive policy/rich-result/statistic claims into `references/freshness-and-policy.md` and converted "run locally" gaps into Boundaries.
- Moved source-specific usage limits into `references/source-usage.md`.
- Preserved the source as reference material rather than executable instructions.

This file is an attribution record only; the skill does not depend on the top-level `references/` tree to run.
