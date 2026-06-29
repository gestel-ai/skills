<!-- Used by: gestel-blog -->

# Provenance

This skill is a local standardization of license-compatible source material. It
does not copy upstream runtime scripts, provider adapters, Task agents, generated
assets, or hidden credential assumptions.

## Source Map

- Source path: `references/skills/claude-blog/skills/blog/SKILL.md`
- Upstream path: `references/source-repos/claude-blog/skills/blog/SKILL.md`
- Commit: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- License: MIT
- Notice: `references/source-repos/claude-blog/NOTICE`

## Copied Support Docs

The source orchestrator linked deep methodology docs from
`claude-blog/skills/blog/references/`. To keep this skill self-contained, the
following were copied verbatim into this folder (filenames preserved), commit
`49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`, MIT:

- `content-rules.md`
- `quality-scoring.md`
- `content-templates.md`
- `platform-guides.md`
- `flow-alignment.md`
- `eeat-signals.md`
- `geo-optimization.md`
- `blog-delivery-contract.md` (design reference only; its scripts are not shipped)

## Sibling Repo Commits (provenance only)

- claude-ads: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- claude-blog: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- claude-seo: `d830cdb2ad339bb7f062339fe82228b072e98061`
- marketingskills: `8bfcdffb655f16e713940cd04fb08891899c47db`

## Local Changes

- Converted the source orchestrator into a project-local routing + standards skill
  with trigger-focused frontmatter.
- Distilled the 6 pillars, FLOW evidence triple, 5-category 100-point scoring model,
  quality gates, 12 content templates, and platform detection inline into SKILL.md.
- Rewrote the source's automated 5-gate "delivery contract" (root scripts
  `blog_preflight.py` / `blog_render.py` / `generate_hero.py`, blocking
  `blog-reviewer` Task agent) as a **manual delivery checklist**, because none of
  those scripts or agents are present in this project. The original design is kept
  as a copied reference doc for attribution, not as an executable dependency.
- Converted the `load_untrusted_root.py` nonce-fence helper, paid providers
  (Gemini image/TTS, NotebookLM, premium stock APIs, Google APIs), and live-data
  fetches into explicit Boundaries with manual fallbacks or routing.
- Routed the missing `write` path (no `gestel-blog-write` skill, no `blog-writer`
  agent) to a hand-composed outline → draft → seo-check → analyze pipeline.
- Dropped the upstream Skool community-promo footer (third-party self-promotion).
- Preserved the source as reference material rather than executable instructions.

These records are attribution only. The skill's runtime behavior does not depend
on the top-level `references/` tree.
