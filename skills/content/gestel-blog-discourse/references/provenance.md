<!-- Sources: references/source-repos/MANIFEST.md, source path listed below -->
<!-- Used by: gestel-blog-discourse -->

# Provenance

This skill is a local standardization of license-compatible source material. It does not copy upstream runtime scripts, platform-API provider adapters, generated assets, or hidden credential assumptions. The references below are attribution only; they are not a runtime dependency, and this skill must keep working if the top-level `references/` tree is deleted.

## Source Map

- Source path: `references/skills/claude-blog/skills/blog-discourse/SKILL.md`
- Upstream path: `references/source-repos/claude-blog/skills/blog-discourse/SKILL.md`
- Commit: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- License: MIT
- Notice: `references/source-repos/claude-blog/NOTICE`

### Supporting references copied into this skill

- `references/research-quality.md` and `references/synthesis-contract.md` are copied from the `claude-blog` repo (commit `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`, MIT). Both adapt material from `last30days-skill` (Matt Van Horn, MIT, <https://github.com/mvanhorn/last30days-skill>).

### Upstream methodology lineage

- Multi-platform discourse-research methodology adapted from `last30days-skill` (Matt Van Horn, MIT, <https://github.com/mvanhorn/last30days-skill>).

### Related source commits (for cross-repo audit only)

- `claude-ads`: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- `claude-blog`: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- `claude-seo`: `d830cdb2ad339bb7f062339fe82228b072e98061`
- `marketingskills`: `8bfcdffb655f16e713940cd04fb08891899c47db`

## Local Changes

- Converted the source into a project-local, self-contained skill with trigger-focused frontmatter.
- Distilled the source methodology (pre-flight trap classes, named-entity decomposition, platform-targeted site operators, recency filters, result schema, untrusted-data scan, cross-source clustering, recency/engagement scoring, NEW/consensus/niche buckets, DISCOURSE.md shape, 6 synthesis LAWs) directly into `SKILL.md`.
- Copied `research-quality.md` and `synthesis-contract.md` into this skill's `references/` so it stands alone if the top-level `references/` tree is removed.
- Converted the missing upstream runtime (the `discourse_research.py` helper, platform APIs, orchestrator slash commands, and `--feed-into` chaining) from assumed functionality into explicit Boundaries: perform clustering/scoring/synthesis by hand or route to an implementation task.
- Preserved the source as reference material rather than executable instructions.
