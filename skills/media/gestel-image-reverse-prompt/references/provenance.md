# Provenance

This skill's prompting rules are distilled from two vendor guides. They are
pointers for maintenance, not a runtime dependency — the skill operates fully
from `SKILL.md` and the other reference files without fetching these.

## Sources

- **fal.ai — GPT Image 2 Prompting Guide**
  `https://fal.ai/learn/tools/prompting-gpt-image-2`
  Source of the five-section template (Scene / Subject / Important details / Use
  case / Constraints), the anti-slop rules, the three operating modes
  (generate / edit / combine), text-rendering discipline, and the edit
  change-vs-preserve pattern.

- **OpenAI — Image generation models prompting guide**
  `https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide`
  Source of the background → subject → details → constraints ordering, the
  descriptive dimensions (subject/scale, composition, lighting, materials,
  color), `quality` tiers, `input_fidelity="high"` for edit fidelity, aspect
  ratio / size constraints, and the surgical-edit / virtual-try-on preserve
  patterns.

## Freshness

Model parameters, size limits, quality tiers, and reference-image caps are a
dated snapshot (captured 2026). GPT Image 2's API surface can change; re-verify
exact numbers against the live vendor docs before relying on them.
