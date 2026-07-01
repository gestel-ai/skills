# Provenance

Endpoint and parameter details for this adapter are distilled from two vendor
guides. They are maintenance pointers, not a runtime dependency — the skill runs
from `SKILL.md`, `references/gpt-image-2-api.md`, and `scripts/generate.py`.

## Sources

- **fal.ai — GPT Image 2 Prompting Guide**
  `https://fal.ai/learn/tools/prompting-gpt-image-2`
  Source of the fal endpoint ids (`openai/gpt-image-2`, `openai/gpt-image-2/edit`),
  the `fal.subscribe` argument shape (`prompt`, `image_size`, `quality`,
  `num_images`, `output_format`), the reference-image / mask edit flow, and the
  16-image reference cap.

- **OpenAI — Image generation models prompting guide**
  `https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide`
  Source of the `quality` tiers, `input_fidelity="high"` for edit fidelity, and
  the aspect-ratio / size constraints (edges multiple of 16, ratio ≤ 3:1, pixel
  bounds, 2K reliability ceiling).

## Freshness

Endpoint ids, parameters, `image_size` presets, quality tiers, and pricing are a
dated snapshot (captured 2026). The fal API surface can change; if a call fails
on an unknown parameter or endpoint, re-verify against the live vendor docs
before editing the script.
