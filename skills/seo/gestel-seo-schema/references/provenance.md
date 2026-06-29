<!-- Generated to match .agents/skills/scripts/scaffold_active_skill_migrations.py output -->
<!-- Sources: references/source-repos/MANIFEST.md, source path listed below -->
<!-- Used by: gestel-seo-schema -->

# Provenance

This skill is a local standardization of license-compatible source material. It does not copy upstream runtime scripts, provider adapters, generated assets, or hidden credential assumptions.

## Source Map

- Source path: `references/skills/claude-seo/skills/seo-schema/SKILL.md`
- Upstream path: `references/source-repos/claude-seo/skills/seo-schema/SKILL.md`
- Commit: `d830cdb2ad339bb7f062339fe82228b072e98061`
- License: MIT
- Notice: `references/skills/claude-seo/skills/seo-schema/LICENSE.txt` (Copyright (c) 2026 AgriciDaniel, <https://github.com/AgriciDaniel/claude-seo>)
- Copied support doc: `references/skills/claude-seo/skills/seo-schema/references/deprecated-types-2024-2026.md` (verbatim, filename preserved)

## Related Source Repositories (MANIFEST)

These commits are recorded for the broader migration manifest; this skill draws only from `claude-seo`.

- `claude-seo`: `d830cdb2ad339bb7f062339fe82228b072e98061`
- `claude-ads`: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- `claude-blog`: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- `marketingskills`: `8bfcdffb655f16e713940cd04fb08891899c47db`

## Local Changes

- Converted the source into a project-local skill with trigger-focused frontmatter.
- Lifted the source's detection / validation / generation methodology, JSON-LD templates, type-status list, and error-handling table into `references/schema-methodology.md` so the skill is self-contained.
- Isolated the source's freshness-sensitive type-status, deprecation-date, rich-result-eligibility, and JS-rendering claims into `references/freshness-and-policy.md` and converted "can't run locally / live lookup" gaps into Boundaries.
- Copied the source support doc `deprecated-types-2024-2026.md` verbatim (filename preserved) and linked it from SKILL.md.
- Moved source-specific usage limits into `references/source-usage.md`.
- Preserved the source as reference material rather than executable instructions.

This file is an attribution record only; the skill does not depend on the top-level `references/` tree to run.
