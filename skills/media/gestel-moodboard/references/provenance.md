<!-- Used by: gestel-moodboard -->

# Provenance

This skill is a local distillation of license-compatible source material. It does
not copy upstream runtime scripts, the vision-catalog pipeline, provider
adapters, generated assets, or hidden credential assumptions.

## Source Map

- Source repository: `github.com/choandahn/brand-moodboard-prompt-pipeline`
- Distilled material: the 4-stage analysis method, the 9-category taxonomy, the
  scene-template structure, the `moodboard.json` shape, and the product-fidelity
  (anti-distortion) discipline — drawn from `engine/shared/PRODUCT_SPEC_GUIDE.md`,
  `GENERATOR.md`, `LESSONS.md`, the category taxonomy, and the `brands/jgracelet/`
  worked example.
- License: MIT

## Local Changes

- Converted the methodology into a self-contained GESTEL skill with
  trigger-focused frontmatter.
- Deliberately **excluded** the ~590-image, ~2M-token Python+Workflow catalog
  pipeline; this skill is reasoning-only over a small curated set.
- Deliberately **excluded** product-prompt generation, which is
  `gestel-ads-photoshoot` / `gestel-image`'s job; this skill stops at the
  templates with `{PRODUCT}` slots.
- Moved source-usage and safe/unsafe boundaries into
  [source-usage.md](source-usage.md).
- Added eval coverage for trigger, near-miss vs `gestel-ads-photoshoot`,
  output-contract, anti-delegation, and untrusted-data cases.
- Preserved the source as reference material rather than executable instructions.
