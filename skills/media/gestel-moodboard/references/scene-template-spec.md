<!-- Used by: gestel-moodboard -->

# Scene Template Spec — structure + `{PRODUCT}` slot contract

Each adopted category gets one reusable **scene template**. A template fixes
everything that is brand-constant (backdrop, lighting, camera, grading, logo) and
leaves the product as a slot a downstream skill fills. Templates inherit the
Stage 2 visual DNA so every category stays on-brand.

## Slot contract

| Slot | Filled by downstream with | Rule |
| --- | --- | --- |
| `{PRODUCT}` | A full product description (the geometry-precise noun phrase) | Required. The only place a specific product enters. |
| `{PRODUCT_LABEL}` | A short human label for filenames/captions | Optional. Slug-friendly, no spaces if used in paths. |

Rules:

- A template **never** hard-codes a specific product. If you find yourself
  writing the brand's actual SKU into a template, move it to a slot.
- Slots use exact spelling `{PRODUCT}` and `{PRODUCT_LABEL}` so the downstream
  expander (`gestel-ads-photoshoot` / `gestel-image`) can string-replace them.
- Everything outside the slots is brand-constant and must be expressible from the
  visual DNA, not invented per product.

## Template fields

Write each template as a small block with these fields:

```text
category:        editorial-neutral
intent:          mid-tone editorial scene, product as calm hero
backdrop:        warm neutral stone surface, soft paper sweep behind
lighting:        single soft window-direction key, gentle fill, low contrast
camera:          50mm-equivalent, eye-level, shallow depth of field
composition:     product right-of-center, generous negative space left
grading:         warm white balance, muted saturation, soft film curve
logo:            none in-frame (added in post)
prompt_template: >
  {PRODUCT} on a warm neutral stone surface, soft paper sweep behind,
  single soft window-direction key light with gentle fill, low contrast,
  50mm look, shallow depth of field, product right-of-center with generous
  negative space, warm muted editorial grading, photorealistic
```

## Authoring guidance

- Derive `backdrop` / `lighting` / `camera` / `grading` from the Stage 2 DNA and
  the catalog rows for that category — do not freelance a look the brand never
  shoots.
- Keep `prompt_template` self-contained and runnable verbatim once the slot is
  filled. Aim for 40-80 words, specific over exhaustive.
- State photorealism explicitly when the DNA is photoreal; state the rendering
  style otherwise.
- Do **not** add product-fidelity language to the template itself — the
  anti-distortion guard is applied at hand-off time from
  [product-fidelity-guard.md](product-fidelity-guard.md), against the real
  `{PRODUCT}` value.
- Mirror each template into `moodboard.json` under its category key per
  [moodboard-json-schema.md](moodboard-json-schema.md).
