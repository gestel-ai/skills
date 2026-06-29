<!-- Sources: references/source-repos/MANIFEST.md, source path listed below -->
<!-- Used by: gestel-ads-generate -->

# Provenance

This skill is a local standardization of license-compatible source material. It does not copy
upstream runtime scripts, provider adapters, MCP integrations, generated assets, or hidden
credential assumptions. The upstream pixel-render path is intentionally converted into a Boundary.

## Source Map

- Source path: `references/skills/claude-ads/skills/ads-generate/SKILL.md`
- Upstream path: `references/source-repos/claude-ads/skills/ads-generate/SKILL.md`
- Commit: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- License: MIT

The source skill had no `references/` or `evals/` files of its own; the support docs in this folder
are distilled from the source SKILL.md body, not copied files.

## Related upstream repos (attribution, not runtime dependencies)

- `claude-ads` — commit `283d9d4917cb7c4f2ce9181e125bb1970f74ab04` (primary source)
- `claude-blog` — commit `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- `claude-seo` — commit `d830cdb2ad339bb7f062339fe82228b072e98061`
- `marketingskills` — commit `8bfcdffb655f16e713940cd04fb08891899c47db`

## Local Changes

- Converted the source into a project-local skill with trigger-focused frontmatter.
- Converted the provider-bound render path (banana-claude / nanobanana-mcp, with gpt-image-1 /
  Stability / Replicate / Ideogram fallbacks) and the upstream agents/scripts/cost-log into an
  explicit Boundary that routes rendering out.
- Transferred the render-agnostic methodology: brief parsing, creative-direction modes, prompt
  framework, platform creative specs, cost-estimate method, manifest spec, and quality gate.
- Moved source-specific boundaries into `references/source-usage.md`.
- Preserved the source as reference material rather than executable instructions. Nothing in this
  skill depends on the top-level `references/` tree at runtime.
