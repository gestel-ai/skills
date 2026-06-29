<!-- Sources: references/source-repos/MANIFEST.md, source path listed below -->
<!-- Used by: gestel-seo-images -->

# Provenance

This skill is a local standardization of license-compatible source material. It does not
copy upstream runtime scripts (`parse_html.py`, `iptc_ai_label.py`), the DataForSEO MCP
dependency, paid-provider adapters, or hidden credential assumptions. Provenance is
attribution only; this skill must function even if the top-level `references/` tree is
deleted.

## Source Map

- Source path: `references/skills/claude-seo/skills/seo-images/SKILL.md`
- Upstream path: `references/source-repos/claude-seo/skills/seo-images/SKILL.md`
- Commit: `d830cdb2ad339bb7f062339fe82228b072e98061`
- License: MIT (`references/source-repos/claude-seo/LICENSE`; skill-local
  `references/skills/claude-seo/skills/seo-images/LICENSE.txt`)
- Upstream copyright: Copyright (c) 2026 AgriciDaniel — <https://github.com/AgriciDaniel/claude-seo>

## Reused Support Docs

None imported verbatim. `references/image-audit-checklist.md` and
`references/image-file-optimization.md` are distillations authored for this skill from the
single source `SKILL.md`; they hold the freshness-sensitive facts (browser-support %,
Merchant Center / Google Images policy, JPEG XL status) as dated snapshots, not as runtime
configuration.

## Related Repo Commits (attribution context)

- `claude-ads`: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- `claude-blog`: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- `claude-seo`: `d830cdb2ad339bb7f062339fe82228b072e98061`
- `marketingskills`: `8bfcdffb655f16e713940cd04fb08891899c47db`

## Local Changes

- Converted the source into a project-local skill with trigger-focused frontmatter.
- Moved the live Image-SERP feature (DataForSEO MCP `serp_google_images_live_advanced`)
  into a Boundary and routed it to `gestel-seo-dataforseo`.
- Moved the bundled upstream scripts (`scripts/parse_html.py` lazy-method classifier and
  `scripts/iptc_ai_label.py` AI-label audit/inject) into a Boundary, replacing them with
  manual classification and raw `exiftool` equivalents.
- Gated the file-optimization CLI recipes on tool-availability checks (`which …`); they
  apply only to local files, never as an assumed always-available pipeline.
- Recast freshness-sensitive browser-support %, Google Images / Merchant Center policy,
  and JPEG XL claims as dated snapshots needing live verification.
- Distilled the portable audit methodology into `SKILL.md`,
  `references/image-audit-checklist.md`, and `references/image-file-optimization.md`.
- Preserved the source as reference material rather than executable instructions.
