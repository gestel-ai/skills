<!-- Used by: gestel-ads-server-side-tracking -->

# Provenance

This skill is a local standardization of license-compatible source material. It
does not copy upstream runtime scripts, provider adapters, generated assets, or
hidden credential assumptions. Provenance below is attribution only and is not a
runtime dependency.

## Source Map

- Source path: `references/skills/claude-ads/skills/ads-server-side-tracking/SKILL.md`
- Upstream path: `references/source-repos/claude-ads/skills/ads-server-side-tracking/SKILL.md`
- Commit: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- License: MIT (Copyright (c) 2026 agricidaniel)

Related repos referenced by the GESTEL skill set (attribution only):
`claude-blog` commit `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`,
`claude-seo` commit `d830cdb2ad339bb7f062339fe82228b072e98061`,
`marketingskills` commit `8bfcdffb655f16e713940cd04fb08891899c47db`.

## Local Changes

- Distilled the source SKILL.md into a project-local, self-contained skill with
  trigger-focused frontmatter; no top-level `references/` runtime dependency.
- Moved the source's per-surface checklists, threshold table, health-score
  breakdown, and PII/hashing rules into local `references/*.md` files
  (`pipeline-audit-checklist.md`, `hashing-and-pii.md`,
  `thresholds-and-scoring.md`).
- Converted "can't run locally" capabilities (live event capture, account
  reads/writes, real end-to-end fires, server deployment) from features into
  explicit Boundaries instead of inlining assumed access.
- Added a live-research / freshness Boundary: platform tag behavior, CAPI
  Gateway feature sets, EMQ scoring, ITP/ATT mechanics, and data-loss
  percentages are not asserted as current without dated evidence.
- Preserved the source as reference material rather than executable instructions.
