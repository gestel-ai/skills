<!-- Sources: references/source-repos/MANIFEST.md, source path listed below -->
<!-- Used by: gestel-seo-image-gen -->

# Provenance

This skill is a local standardization of license-compatible source material. It does not copy upstream runtime scripts, provider adapters, generated assets, or hidden credential assumptions. Provenance is attribution only; this skill must function even if the top-level `references/` tree is deleted.

## Source Map

- Source path: `references/skills/claude-seo/extensions/banana/skills/seo-image-gen/SKILL.md`
- Upstream path: `references/source-repos/claude-seo/extensions/banana/skills/seo-image-gen/SKILL.md`
- Commit: `d830cdb2ad339bb7f062339fe82228b072e98061`
- License: MIT
- Notice: `references/source-repos/claude-seo/NOTICE`
- Upstream copyright: Copyright (c) 2026 AgriciDaniel — <https://github.com/AgriciDaniel/claude-seo>

## Reused Support Docs

- `references/gemini-models.md` and `references/mcp-tools.md` were reused from the local `gestel-blog-image` distillation (origin repo `claude-blog`, commit `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`, MIT). They are retained as dated snapshots of freshness-sensitive model/tool facts, not as runtime configuration.

## Related Repo Commits (attribution context)

- `claude-ads`: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- `claude-blog`: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- `claude-seo`: `d830cdb2ad339bb7f062339fe82228b072e98061`
- `marketingskills`: `8bfcdffb655f16e713940cd04fb08891899c47db`

## Local Changes

- Converted the source into a project-local skill with trigger-focused frontmatter.
- Moved paid-provider rendering, MCP tools, and upstream install/preset/cost/generate scripts into Boundaries.
- Distilled the 6-component creative-director methodology, SEO asset-type mapping, and post-generation SEO package into `SKILL.md`, `references/prompt-engineering-seo.md`, and `references/seo-image-checklist.md`.
- Recast freshness-sensitive platform/policy/pricing claims as dated snapshots gated on dated research or live lookup.
- Preserved the source as reference material rather than executable instructions.
