<!-- Generated for the gestel-seo-firecrawl active-skill migration -->
<!-- Sources: references/source-repos/MANIFEST.md, source path listed below -->
<!-- Used by: gestel-seo-firecrawl -->

# Provenance

This skill is a local standardization of license-compatible source material. It does not copy upstream runtime scripts, provider adapters, generated assets, or hidden credential assumptions.

## Source Map

- Source path: `references/skills/claude-seo/extensions/firecrawl/skills/seo-firecrawl/SKILL.md`
- Upstream path: `references/source-repos/claude-seo/extensions/firecrawl/skills/seo-firecrawl/SKILL.md`
- Commit: `d830cdb2ad339bb7f062339fe82228b072e98061`
- License: MIT (`references/source-repos/claude-seo/LICENSE`; source skill ships its own `LICENSE.txt`, © 2026 AgriciDaniel, <https://github.com/AgriciDaniel/claude-seo>)
- Migrated support doc: `references/firecrawl-patterns.md` (distilled from the source's per-operation parameter tables, usage patterns, scrape-vs-fetch matrix, cross-skill integration, and error table — the source skill had no separate `references/` or `evals/` directory to copy)

### Related source commits (provenance only, no runtime dependency)

- claude-ads: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- claude-blog: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- claude-seo: `d830cdb2ad339bb7f062339fe82228b072e98061`
- marketingskills: `8bfcdffb655f16e713940cd04fb08891899c47db`

## Local Changes

- Converted the source into a project-local skill with trigger-focused frontmatter.
- Converted the paid Firecrawl provider, the `FIRECRAWL_API_KEY`/MCP gate, the `extensions/firecrawl/install.sh` setup script, the MCP-availability probe, and the live `firecrawl_*` tool calls into Boundaries; live execution routes to a Firecrawl adapter/MCP or to a user-supplied crawl/map/scrape export.
- Migrated the portable methodology — operation selection (map/crawl/scrape/search), crawl-scoping strategies, result interpretation (URL-pattern report, orphan/thin/duplicate/broken detection, sitemap coverage), credit-budget discipline, and cross-skill routing — into SKILL.md.
- Copied the deep parameter tables, SEO usage patterns, scrape-vs-fetch decision matrix, cross-skill integration detail, and the error/condition table to `references/firecrawl-patterns.md` so the skill works after the top-level `references/` tree is deleted.
- Reframed pricing/free-tier/rate-limit figures as dated snapshots requiring live verification.
- Preserved the source as reference material rather than executable instructions.
