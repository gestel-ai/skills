<!-- Used by: gestel-blog-write -->

# Provenance

This skill is a local standardization of license-compatible source material. It
does not copy upstream runtime scripts, provider adapters, generated assets, or
hidden credential assumptions.

## Source Map

- Source path: `references/skills/claude-blog/skills/blog-write/SKILL.md`
- Upstream path: `references/source-repos/claude-blog/skills/blog-write/SKILL.md`
- Commit: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- License: MIT
- Notice: `references/source-repos/claude-blog/NOTICE`

## Copied Support Docs

The source SKILL linked deep methodology docs from `claude-blog/skills/blog/references/`
and 12 content templates from `claude-blog/skills/blog/templates/`. To keep this
skill self-contained, the following were copied verbatim (filenames preserved),
commit `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`, MIT:

- `content-templates.md`
- `synthesis-contract.md`
- `flow-alignment.md`
- `quality-scoring.md`
- `eeat-signals.md`
- `internal-linking.md`
- `visual-media.md`
- `cta-placement.md`
- `content-rules.md`
- `video-embeds.md`
- `templates/` — `how-to-guide`, `listicle`, `case-study`, `comparison`,
  `pillar-page`, `product-review`, `thought-leadership`, `roundup`, `tutorial`,
  `news-analysis`, `data-research`, `faq-knowledge`.

## Sibling Repo Commits (provenance only)

- claude-ads: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- claude-blog: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- claude-seo: `d830cdb2ad339bb7f062339fe82228b072e98061`
- marketingskills: `8bfcdffb655f16e713940cd04fb08891899c47db`

## Local Changes

- Converted the source into a project-local skill with trigger-focused frontmatter.
- Distilled the surface-targeting, template-selection, research, outline, chart,
  writing (frontmatter, Key Takeaways, answer-first + FLOW triple, information-gain
  markers, citation capsules, internal-link zones, paragraph/heading/embedding
  rules, FAQ), and self-quality-check methodology inline into SKILL.md.
- Converted source dependencies that are not present locally into explicit
  Boundaries with manual fallbacks or routing: the Phase 6.5 delivery contract and
  its root scripts (`blog_preflight.py`, `blog_render.py`, `generate_hero.py`), the
  `blog-chart`/`blog-image`/`blog-notebooklm` sub-skills, nanobanana-mcp and other
  paid/keyed media providers, and the `blog-researcher`/`blog-reviewer` agents.
- Did NOT mirror `blog-delivery-contract.md` as an executable gate; the render/
  preflight/visual loop it describes is flagged as a future implementation task.
- Copied the linked methodology docs and templates locally so the skill survives
  deletion of the top-level `references/` tree.
- Preserved the source as reference material rather than executable instructions.

These records are attribution only. The skill's runtime behavior does not depend
on the top-level `references/` tree.
