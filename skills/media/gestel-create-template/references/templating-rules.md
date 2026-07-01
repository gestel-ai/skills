<!-- Used by: gestel-create-template -->

# Templating Rules — freeze, slotify, vary

Turns a `gestel-image-reverse-prompt` extraction into a reusable `<scene>.txt`
template. Everything that makes the shot a *specific instance* (product,
brand, tagline wording) becomes swappable; everything that makes it a *scene*
(environment) stays fixed.

## The freeze / slot / vary table

| Element | Treatment | Rule |
| --- | --- | --- |
| Environment (background, composition, camera angle, lighting, palette, grading, placement) | **Freeze** | Copy from the extraction verbatim. Never paraphrase or soften a specific fact into a vague one — "35mm-equivalent, eye-level, three-quarter angle" stays exactly that, not "nice camera angle." |
| Product | **Slot** — `{PRODUCT}` | Replace the specific product noun phrase with the slot. The template must contain no trace of the original product's identity. |
| Brand name / label | **Slot** — `{BRAND}` | Replace the specific brand text with the slot, but keep the *typography* facts (case, weight, placement, color) as frozen environment. The slot carries the word; the frozen facts carry how it's set. |
| Tagline / secondary copy | **Vary** | Rewrite to a different message with the same structure, tone, and length as the original — see [Copy variation](#copy-variation). |
| Spec strings and numbers (volume, weight, count, percentage) | **Preserve**, unless clearly brand-bound | A spec like "12 oz" or "500mg" is a physical fact about the product category, not brand identity — keep it verbatim. Only replace a number if it is clearly part of the brand's own claim text (e.g. a proprietary formula name) rather than a physical measurement. |

## Identifying tokens in the verbatim text

The extraction's verbatim-text field is the input to this pass. Sort every
transcribed string into one of three buckets before deciding freeze/slot/vary:

1. **Brand-name tokens** — the product's own brand or company name, anywhere it
   appears (logo mark, cap text, label header). These map to `{BRAND}`.
2. **Descriptor tokens** — the product's own name, variant, flavor, or a
   marketing line specific to *that* product ("Aurora Night Cream," "Derived
   from Fruit"). These map to `{PRODUCT}` if they identify the physical item,
   or get **varied** if they are a tagline/claim describing it rather than
   naming it.
3. **Spec tokens** — measurements, counts, percentages, certifications
   ("12 FL OZ," "100% recycled," "Net Wt 8g"). These are **preserved**
   verbatim per the table above, because they describe the product category's
   physical reality, not this specific brand's voice.

When a string is ambiguous (e.g. a number embedded in a brand name, like "N°5"),
treat it as a brand-name token — it disappears into `{BRAND}` along with the
rest of the label rather than surviving as a stray spec.

## Copy variation

Vary tagline and secondary copy so the rebranded example reads as an authentic
line for the new brand, not a substitution exercise. Match the original's
**structure** (sentence shape), **tone** (register — clinical, playful, warm),
and **length** (word count within one or two words). Change the *content*, not
the *form*.

**Example 1 — beverage tagline**

- Original: `"Derived from Fruit"` (three words, capitalized title case, factual/clean register)
- Varied for GESTEL: `"Crafted from Nature"` — same three-word title-case shape,
  same factual/clean register, different content.

**Example 2 — supplement tagline**

- Original: `"Clinically Proven Results"` (three words, title case, clinical/confident register)
- Varied for GESTEL: `"Backed by the Science"` — same short declarative shape
  and confident register, four words is close enough in length to read the
  same on-pack, different content and no false clinical claim carried over.

Do not carry over a specific factual claim (a clinical trial result, a
certification, a numeric guarantee) that GESTEL cannot substantiate — vary
those into a tone-matched but non-specific line instead of a literal swap.

## Scene-stem derivation

Derive a kebab-case **scene stem** from the extraction's dominant scene facts,
in this order of priority:

1. **Subject/product category** (what kind of thing is shown — not its brand
   name), e.g. "lilac" (color/material cue), "serum bottle."
2. **A distinguishing environmental detail** that would collide with other
   scenes otherwise, e.g. "water-droplet" for a wet-surface studio shot.
3. **Medium/setting** — "studio," "editorial," "flatlay," "lifestyle."

Join 2-4 of the most identifying words with hyphens, lowercase, no brand names,
no product names (the stem describes the *scene*, which is reusable across
products/brands — never the one-off item that happened to be photographed).

Example: a source image of a lilac-hued serum bottle on a wet reflective
studio surface with soft top-down lighting derives the stem
`lilac-water-droplet-studio`.

## Full worked example

**Input scene** (from `gestel-image-reverse-prompt` extraction): a glass jar
of skincare cream on a wet slate surface, water droplets scattered around the
base, soft diffused daylight from camera-left, shallow depth of field, cool
neutral color grading, the jar's label reads "AURELIA — Derived from Fruit —
1.7 FL OZ."

**Scene stem:** `slate-water-droplet-jar`

**`slate-water-droplet-jar.txt` (template, slots left in place):**

```text
Scene: A glass jar of skincare cream rests on a wet dark slate surface,
scattered water droplets around its base, softly blurred neutral studio
backdrop.
Subject: {PRODUCT}, centered, occupying the lower two-thirds of the frame.
Important details: soft diffused daylight from camera-left, gentle
reflection on the slate, shallow depth of field with a 50mm-equivalent
feel, cool neutral color grading, low contrast. The jar's label reads
"{BRAND} — [VARIED TAGLINE] — 1.7 FL OZ" in clean sans-serif, matching the
original's case and placement.
Use case: product photography, e-commerce hero image.
Constraints: no watermark, no extra text beyond the label, no added
objects, preserve real proportions of the jar and droplets.
```

**Example fill values used for the render** (step 3 of `SKILL.md`):

- `{PRODUCT}` → `a cylindrical frosted-glass jar with a matte black lid, approximately 2 inches tall, holding a pale cream product`
- `{BRAND}` → `GESTEL`
- Varied tagline → `"Crafted from Nature"` (replacing `"Derived from Fruit"`, per [Copy variation](#copy-variation) Example 1)
- Spec string `1.7 FL OZ` → preserved verbatim (physical measurement, not brand-bound)

The filled prompt keeps every frozen environment fact (slate surface, water
droplets, camera-left daylight, cool grading, label typography and placement)
identical to the source, and only the slot values and the tagline change.
