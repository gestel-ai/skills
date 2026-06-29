<!-- Used by: gestel-ads-google -->

# Provenance

This skill is a local standardization of license-compatible source material. It does not copy upstream runtime scripts, provider adapters, generated assets, or hidden credential assumptions.

## Source Map

- Source path: `references/skills/claude-ads/skills/ads-google/SKILL.md`
- Upstream path: `references/source-repos/claude-ads/skills/ads-google/SKILL.md`
- Commit: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- License: MIT (Copyright (c) 2026 agricidaniel)

### Copied reference files

Copied verbatim (filenames preserved) from `references/source-repos/claude-ads/ads/references/`:

- `google-audit.md` — 80-check Google Ads audit checklist.
- `scoring-system.md` — weighted Health Score algorithm, severity multipliers, category weights.
- `benchmarks.md` — dated 2025–2026 industry benchmarks (treat as snapshots).
- `gaql-notes.md` — GAQL field incompatibilities, deduplication, false-positive guards.

### Related upstream repos (attribution only, not a runtime dependency)

- `claude-ads` commit `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- `claude-blog` commit `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- `claude-seo` commit `d830cdb2ad339bb7f062339fe82228b072e98061`
- `marketingskills` commit `8bfcdffb655f16e713940cd04fb08891899c47db`

## Local Changes

- Converted the source into a project-local skill with trigger-focused frontmatter.
- Distilled the source methodology (process, category weights, negative-keyword rules, GAQL guards, PMax/AI Max/Demand Gen audits, thresholds, output contract) directly into `SKILL.md` so the skill is self-contained.
- Converted "can't run locally" live-platform features (API/MCP pulls, account writes, upstream scoring scripts) into explicit Boundaries instead of assumed capabilities.
- Added a freshness Boundary: platform rules, migration deadlines, lift percentages, and benchmarks are freshness-sensitive and must be backed by dated research or a live lookup before being asserted.
- Moved source-specific boundaries and untrusted-data handling into this skill and `source-usage.md`.
- Preserved the source as reference material rather than executable instructions.

## Notice

Provenance is attribution only. This skill must keep functioning if the top-level `references/` tree is deleted; nothing here is a runtime dependency.
