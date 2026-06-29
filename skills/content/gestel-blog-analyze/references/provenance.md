<!-- Used by: gestel-blog-analyze -->

# Provenance

This skill is a local standardization of license-compatible source material. It
does not copy upstream runtime scripts, provider adapters, generated assets, or
hidden credential assumptions.

## Source Map

- Source path: `references/skills/claude-blog/skills/blog-analyze/SKILL.md`
- Upstream path: `references/source-repos/claude-blog/skills/blog-analyze/SKILL.md`
- Commit: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- License: MIT
- Notice: `references/source-repos/claude-blog/NOTICE`

## Copied Support Docs

The source SKILL linked deep rubric docs from `claude-blog/skills/blog/references/`.
To keep this skill self-contained, the following were copied verbatim into this
folder (filenames preserved), commit `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`, MIT:

- `quality-scoring.md`
- `eeat-signals.md`
- `ai-slop-detection.md`
- `editorial-heuristics.md`
- `cognitive-load.md`
- `flow-alignment.md`

## Sibling Repo Commits (provenance only)

- claude-ads: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- claude-blog: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- claude-seo: `d830cdb2ad339bb7f062339fe82228b072e98061`
- marketingskills: `8bfcdffb655f16e713940cd04fb08891899c47db`

## Local Changes

- Converted the source into a project-local skill with trigger-focused frontmatter.
- Distilled the 5-category 100-point scoring model, AI-content detection, and
  report templates inline into SKILL.md.
- Converted source dependencies that are not present locally (root
  `scripts/cognitive_load.py`, a `/blog rewrite` companion, live URL fetch) into
  explicit Boundaries with manual fallbacks or routing.
- Copied the linked deep rubric docs locally so the skill survives deletion of
  the top-level `references/` tree.
- Preserved the source as reference material rather than executable instructions.

These records are attribution only. The skill's runtime behavior does not depend
on the top-level `references/` tree.
