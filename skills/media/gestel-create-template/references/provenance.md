<!-- Used by: gestel-create-template -->

# Provenance

This skill is an orchestrator: it composes two sibling skills that already
carry their own provenance, plus one novel step of its own. These are pointers
for maintenance, not a runtime dependency — the skill operates fully from
`SKILL.md` and [templating-rules.md](templating-rules.md) without fetching
anything below.

## Composed skills

- **`gestel-image-reverse-prompt`** supplies step 1 (extract the five-section
  blueprint from the source image). See that skill's own
  `references/provenance.md` for its source map.
- **`gestel-image-render`** supplies step 3 (render the filled template as
  WEBP through GPT Image 2 on fal) and the cost-and-confirmation gate this
  skill inherits. See that skill's own `references/provenance.md` for its
  source map.

## Vendor sources behind the composed skills

- **fal.ai — GPT Image 2 Prompting Guide**
  `https://fal.ai/learn/tools/prompting-gpt-image-2`
  Source of the five-section prompt structure this skill's template inherits
  from step 1, and the endpoint/parameter surface step 3 renders against.

- **OpenAI — Image generation models prompting guide**
  `https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide`
  Source of the descriptive-dimension ordering and `quality` / `input_fidelity`
  guidance the composed skills apply.

## This skill's own contribution

The freeze/slot/vary templating method in
[templating-rules.md](templating-rules.md) — the environment/product/brand/copy
classification, the `{PRODUCT}` / `{BRAND}` slot contract, the copy-variation
discipline, and the scene-stem derivation rule — is original to this skill. It
is not distilled from the two vendor guides above; it is the glue that makes a
one-off reverse-engineered prompt into a reusable, rebrandable template.

## Freshness

Model parameters, size limits, quality tiers, and output-format support are a
dated snapshot (captured 2026) inherited from `gestel-image-render`. GPT Image
2's API surface can change; re-verify exact numbers against the live vendor
docs before relying on them.
