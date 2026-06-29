<!-- Updated: 2026-06-26 | v1.0 -->
<!-- Sources: references/source-repos/MANIFEST.md, local source-repo files listed below -->
<!-- Used by: gestel-creative-package -->

# Provenance

This skill is a GESTEL-specific distillation. It does not copy upstream runtime scripts, provider-specific templates, generated assets, or broad platform suites.

## Source Map

| Source | Commit | License | Local use |
| --- | --- | --- | --- |
| `references/source-repos/marketingskills/skills/ad-creative/SKILL.md` | `8bfcdffb655f16e713940cd04fb08891899c47db` | MIT | Angle generation, copy constraints, performance iteration concepts |
| `references/source-repos/marketingskills/skills/ads/SKILL.md` | `8bfcdffb655f16e713940cd04fb08891899c47db` | MIT | Lightweight paid ads trigger shape and campaign context |
| `references/source-repos/claude-ads/skills/ads-creative/SKILL.md` | `283d9d4917cb7c4f2ce9181e125bb1970f74ab04` | MIT | Creative quality and fatigue concepts, narrowed to static assets |
| `references/source-repos/claude-ads/skills/ads-create/SKILL.md` | `283d9d4917cb7c4f2ce9181e125bb1970f74ab04` | MIT | Campaign brief and image brief structure, narrowed to GESTEL package manifests |
| `references/source-repos/claude-ads/skills/ads-plan/SKILL.md` and `skills/ads-plan/assets/ecommerce-creative.md` | `283d9d4917cb7c4f2ce9181e125bb1970f74ab04` | MIT | E-commerce creative family inspiration, Meta static creative rules |
| `references/source-repos/marketingskills/skills/ad-creative/references/platform-specs.md` | `8bfcdffb655f16e713940cd04fb08891899c47db` | MIT | Distilled into local `references/platform-specs.md`, scoped to Meta/Instagram static |

This skill is now self-contained: its methodology lives in `SKILL.md` and its support docs
(`slot-contract.md`, `template-catalog.md`, `export-contract.md`, `platform-specs.md`) live in
this `references/` folder. The table above is attribution only; deleting the top-level
`references/` tree does not change this skill's behavior.

## Local Changes

- Restricts output to product-photo Meta and Instagram static image packs.
- Uses GESTEL's 6-family, 18-template MVP catalog instead of upstream all-channel assets.
- Adds package manifest validation and variant ID mapping for manual performance import.
- Removes video generation, platform API writes, broad campaign architecture, and provider-specific assumptions.
- The upstream `ad-creative/references/generative-tools.md` (paid image/video/voice providers and code-based renderers) is intentionally NOT imported. GESTEL has no local renderer, so that capability is expressed as a Boundary in `SKILL.md` (route rendering to a dedicated image-generation adapter task) rather than inlined as a feature.
