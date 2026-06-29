<!-- Sources: references/source-repos/MANIFEST.md, source path listed below -->
<!-- Used by: gestel-blog-rewrite -->

# Provenance

This skill is a local standardization of license-compatible source material. It does
not copy upstream runtime scripts, provider adapters, generated assets, specialist
agents, or hidden credential assumptions. The source is recorded for attribution only
and is never a runtime dependency.

## Source Map

- Source path: `references/skills/claude-blog/skills/blog-rewrite/SKILL.md`
- Upstream path: `references/source-repos/claude-blog/skills/blog-rewrite/SKILL.md`
- Commit: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- License: MIT
- Notice: `references/source-repos/claude-blog/NOTICE`

### Supporting methodology references (copied verbatim from the same upstream repo)

Copied from `references/skills/claude-blog/skills/blog/references/` (commit
`49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`, MIT):

- `references/quality-scoring.md`
- `references/eeat-signals.md`
- `references/internal-linking.md`
- `references/visual-media.md`
- `references/video-embeds.md`
- `references/ai-slop-detection.md`

### Related upstream commit hashes (sibling source repos)

- `claude-ads`: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- `claude-blog`: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- `claude-seo`: `d830cdb2ad339bb7f062339fe82228b072e98061`
- `marketingskills`: `8bfcdffb655f16e713940cd04fb08891899c47db`

## Local Changes

- Converted the source into a project-local skill with trigger-focused frontmatter,
  including explicit near-miss routing and a credential/provider/live-mutation/missing-script boundary.
- Ported the full hand-followable methodology (6-phase audit→rewrite→verify workflow,
  first- and second-order AI-slop detection, anti-AI-detection transforms, citation
  capsules, information-gain markers, scoring rubric) directly into `SKILL.md`.
- Copied the load-bearing methodology references locally so the skill stands alone if
  the top-level `references/` tree is deleted.
- Converted the upstream script/agent dependencies (`generate_hero.py`,
  `blog_render.py`, `blog_preflight.py`, `blog-reviewer` agent, `blog-chart`/`blog-image`
  sub-skills) into explicit Boundaries with manual fallbacks and routing targets,
  rather than inlining fabricated automation.
- Preserved the source as reference material rather than executable instructions.
