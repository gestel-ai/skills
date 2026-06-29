<!-- Sources: references/source-repos/MANIFEST.md, source path listed below -->
<!-- Used by: gestel-seo-ahrefs -->

# Provenance

This skill is a local standardization of license-compatible source material. It does not copy upstream runtime scripts, provider adapters, install wiring, generated assets, or hidden credential assumptions.

## Source Map

- Source path: `references/skills/claude-seo/extensions/ahrefs/skills/seo-ahrefs/SKILL.md`
- Upstream path: `references/source-repos/claude-seo/extensions/ahrefs/skills/seo-ahrefs/SKILL.md`
- Commit: `d830cdb2ad339bb7f062339fe82228b072e98061`
- License: MIT (`references/source-repos/claude-seo/LICENSE`)
- Note: the source skill shipped only a single `SKILL.md` (no `references/` or `evals/` subdirectory). The extension's `docs/AHREFS-SETUP.md`, `install.sh`, `install.ps1`, and `uninstall.sh` are install/credential wiring and were intentionally NOT migrated — they are adapter concerns captured as Boundaries, not support docs.

### Related source commits (provenance only, no runtime dependency)

- claude-ads: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- claude-blog: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- claude-seo: `d830cdb2ad339bb7f062339fe82228b072e98061`
- marketingskills: `8bfcdffb655f16e713940cd04fb08891899c47db`

## Local Changes

- Converted the source into a project-local skill with trigger-focused frontmatter.
- Converted the live `@ahrefs/mcp@0.0.11` MCP routing, the `install.sh`/`install.ps1`/`uninstall.sh` wiring, the `AHREFS_API_TOKEN` credential gate, the `mcpServers.ahrefs` settings merge, and the `dataforseo_costs.py` metered-cost workflow into Boundaries; live data pulls route to an Ahrefs adapter or user-supplied exports.
- Migrated and substantially deepened the portable analyst methodology that the source only gestured at: per-surface metric interpretation (DR/UR, referring domains vs total backlinks, organic-traffic-as-estimate), backlink/anchor-distribution and follow/nofollow judgment, toxic-link triage and disavow restraint, organic-keyword striking-distance and concentration reading, Content Explorer link-bait pattern reading, competitor link-gap, and multi-source confidence weighting (drawn from the source's "Output conventions" and "Cross-skill delegation" notes).
- Preserved the source as reference material rather than executable instructions.

These provenance files are an attribution record only. They must not become a runtime dependency: the skill is designed to work after the top-level `references/` tree is deleted.
