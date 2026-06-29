<!-- Sources: references/source-repos/MANIFEST.md, source paths listed below -->
<!-- Used by: gestel-programmatic-seo -->

# Provenance

This skill is a local standardization of license-compatible source material. It does not copy upstream
runtime scripts, a page generator, a keyword/SERP/rank data provider, paid provider adapters
(DataForSEO, Ahrefs, SE Ranking, etc.), live conversion-data feeds, generated assets, or hidden
credential assumptions.

## Source Map

Single-source migration; MIT-licensed.

- Methodology source path: `references/skills/marketingskills/skills/programmatic-seo/SKILL.md`
  - Upstream path: `references/source-repos/marketingskills/skills/programmatic-seo/SKILL.md`
  - Commit: `8bfcdffb655f16e713940cd04fb08891899c47db`
  - License: MIT (Copyright (c) 2025 Corey Haines, marketingskills)
- Supporting reference copied: `references/playbooks.md` (filename preserved), copied verbatim from
  `references/skills/marketingskills/skills/programmatic-seo/references/playbooks.md`. The source
  `evals/evals.json` was used only to validate trigger/output coverage and was not copied as a runtime
  dependency.

## Local Changes

- Wrote trigger-focused frontmatter (playbook triggers and casual phrasings, near-miss exclusions
  routing to gestel-seo-page / gestel-seo-audit / gestel-content-strategy / gestel-seo-cluster /
  gestel-copywriting / gestel-blog-schema / gestel-site-architecture, an explicit near-miss to the
  sibling gestel-seo-programmatic, and the
  no-credentials / no-paid-provider / no-live-mutation / no-upstream-scripts boundary inline).
- Inlined the full methodology — initial assessment, core principles with the data-defensibility
  hierarchy, the 12-playbook table and asset-match/combination guidance, the five-step implementation
  framework, pre-launch quality checklist, an indexation-diagnosis sequence (distilled from the source
  eval cases), common mistakes, and the strategy-doc / page-template output — so the skill is
  self-contained with no dependency on the top-level `references/` tree.
- Copied the source `references/playbooks.md` into this skill's `references/` and linked it from
  SKILL.md (deep per-playbook detail lives there; the SKILL.md table is the index).
- Converted the source's implicit reliance on live keyword/SERP/volume data, live conversion data, and
  current-Google-policy facts into Boundaries and freshness flags; marked search volumes, SERP
  positions, rich-result eligibility, penalty waves, and marketplace/platform rules as requiring dated
  user research or a live lookup before being presented as verified.
- Preserved the source as reference material rather than executable instructions.

## Related Source Repo Commits (attribution only)

- claude-ads: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- claude-blog: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- claude-seo: `d830cdb2ad339bb7f062339fe82228b072e98061`
- marketingskills: `8bfcdffb655f16e713940cd04fb08891899c47db`
