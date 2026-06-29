<!-- Used by: gestel-moodboard -->

# `moodboard.json` Schema

The machine-readable artifact that `gestel-ads-photoshoot` and `gestel-image`
consume as a visual scene layer. Write it alongside `BRAND_MOODBOARD.md` in
`moodboard/<brand>/`. Keys are lowercase; category keys are kebab-case and match
the adopted taxonomy.

## Shape

```json
{
  "schema_version": "1.0",
  "brand": "jgracelet",
  "product_type": "jewelry",
  "source_image_count": 22,
  "generated_from": "curated reference set (reasoning-only)",
  "color_system": {
    "dominant": ["#1A1A1A", "#F4F1EC"],
    "accent": ["#C9A24B"],
    "background_tones": ["#FFFFFF", "#EDE8E0"]
  },
  "signature_motifs": [
    "soft paper sweep backdrops",
    "single-source window light",
    "generous negative space"
  ],
  "photography_principles": {
    "photorealism": "high",
    "white_balance": "warm",
    "lens": "50-85mm equivalent, shallow depth of field",
    "negative_space": "generous"
  },
  "taxonomy": {
    "default_slots": ["hero-white", "product-card", "macro", "editorial-light", "editorial-neutral", "editorial-dark", "flatlay", "lifestyle", "conceptual-prop"],
    "adopted": ["hero-white", "gemstone-macro", "editorial-neutral", "lifestyle"],
    "pruned": ["editorial-dark", "flatlay", "conceptual-prop"],
    "relabeled": {"macro": "gemstone-macro"}
  },
  "categories": [
    {
      "key": "editorial-neutral",
      "intent": "mid-tone editorial scene, product as calm hero",
      "evidence_image_count": 6,
      "confidence": "high",
      "template": {
        "backdrop": "warm neutral stone surface, soft paper sweep behind",
        "lighting": "single soft window-direction key, gentle fill, low contrast",
        "camera": "50mm-equivalent, eye-level, shallow depth of field",
        "composition": "product right-of-center, generous negative space left",
        "grading": "warm white balance, muted saturation, soft film curve",
        "logo": "none in-frame",
        "prompt_template": "{PRODUCT} on a warm neutral stone surface, soft paper sweep behind, single soft window-direction key light with gentle fill, low contrast, 50mm look, shallow depth of field, product right-of-center with generous negative space, warm muted editorial grading, photorealistic"
      }
    }
  ]
}
```

## Field notes

- `schema_version` — bump on breaking schema changes; consumers gate on it.
- `color_system` — Hex strings; arrays may hold one or several values.
- `taxonomy.adopted` / `pruned` / `relabeled` — make the adaptation auditable so
  consumers know the category set is brand-specific, not the default 9.
- `categories[].template` — mirrors [scene-template-spec.md](scene-template-spec.md);
  `prompt_template` is runnable verbatim once `{PRODUCT}` is filled.
- `categories[].evidence_image_count` / `confidence` — let downstream skills
  weight a thin category or skip a low-confidence one.
- The product-fidelity guard is **not** stored here — it is applied at hand-off
  by the consuming skill against the real product value.

## Consumer contract

`gestel-ads-photoshoot` / `gestel-image` read `categories[].template.prompt_template`,
replace `{PRODUCT}` / `{PRODUCT_LABEL}`, append the product-fidelity anti-distortion
clause, and emit a runnable prompt. They must not rewrite the brand-constant
scene fields, only fill the slots.
