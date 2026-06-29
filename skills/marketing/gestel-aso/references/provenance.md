<!-- Sources: references/source-repos/MANIFEST.md, source paths listed below -->
<!-- Used by: gestel-aso -->

# Provenance

This skill is a local standardization of license-compatible source material. It does not copy upstream
runtime scripts, listing scrapers, page renderers, paid ASO provider adapters (AppTweak, Sensor Tower,
MobileAction, SplitMetrics), console API integrations, generated assets, or hidden credential
assumptions.

## Source Map

Single source, MIT-licensed.

- Methodology source path: `references/skills/marketingskills/skills/aso/SKILL.md`
  - Upstream path: `references/source-repos/marketingskills/skills/aso/SKILL.md`
  - Commit: `8bfcdffb655f16e713940cd04fb08891899c47db`
  - License: MIT
- Supporting references copied from (filenames preserved):
  `references/skills/marketingskills/skills/aso/references/scoring-criteria.md`,
  `references/skills/marketingskills/skills/aso/references/apple-specs.md`,
  `references/skills/marketingskills/skills/aso/references/google-play-specs.md`,
  `references/skills/marketingskills/skills/aso/references/benchmarks.md`,
  `references/skills/marketingskills/skills/aso/references/report-template.md`

## Local Changes

- Wrote trigger-focused frontmatter (triggers, near-miss exclusions, and the
  no-credentials / no-paid-provider / no-live-mutation / no-upstream-scripts boundary inline).
- Inlined the full methodology so the skill is self-contained: store detection + field extraction
  (Phase 1), brand-maturity tiering (Phase 1.5), the six-dimension 0–10 scoring model with weights and
  final-score formula (Phase 2), competitor comparison (Phase 3), report generation (Phase 4), the
  Apple/Google platform rules and what-each-store-indexes table, and the common-issues checklist.
- Copied the five support docs (scoring-criteria, apple-specs, google-play-specs, benchmarks,
  report-template) into local `references/` and linked them from SKILL.md; no dependency on the top-level
  `references/` tree.
- Converted the source's "live-research" assumptions into explicit Boundaries: freshness-sensitive
  platform rules, indexing behavior, character limits, rejection triggers, Android Vitals thresholds,
  policies, and the dated benchmark/conversion numbers must be backed by user-provided dated research or a
  live lookup before being presented as verified.
- Converted the source's reliance on paid ASO tools (AppTweak/Sensor Tower/MobileAction/SplitMetrics),
  console-only metrics, the hidden Apple keyword field, and live listing scraping/rendering into
  Boundaries that route to user-supplied data, `web_fetch` + the `agent-browser` CLI, or a
  live-lookup/Deep-Research task — rather than assuming those exist locally.
- Marked no live App Store Connect / Google Play Console mutation.
- Preserved the source as reference material rather than executable instructions.

## Related Source Repo Commits (attribution only)

- claude-ads: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- claude-blog: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- claude-seo: `d830cdb2ad339bb7f062339fe82228b072e98061`
- marketingskills: `8bfcdffb655f16e713940cd04fb08891899c47db`
