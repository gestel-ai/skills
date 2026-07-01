# GPT Image 2 Prompting Reference

Distilled prompting rules for GPT Image 2 (`gpt-image-2`), the engine this skill
targets. Use these when assembling and tuning the reverse-engineered prompt.

## Contents

- [Five-section prompt structure](#five-section-prompt-structure)
- [Anti-slop discipline](#anti-slop-discipline)
- [Text rendering in images](#text-rendering-in-images)
- [Three operating modes](#three-operating-modes)
- [Fidelity: reference mode for exact reproduction](#fidelity-reference-mode-for-exact-reproduction)
- [Generation parameters](#generation-parameters)
- [Aspect ratio and size](#aspect-ratio-and-size)
- [Worked example](#worked-example)

## Five-section prompt structure

The model responds to a five-section template with line breaks between sections.
Write them in this order:

1. **Scene** — where/when the image exists, background, environment.
2. **Subject** — the main focus, who or what, with scale and placement.
3. **Important details** — materials, textures, lighting sources and direction,
   camera angle, lens feel, composition, mood, color grading.
4. **Use case** — editorial photo, product mockup, poster, UI screen, concept
   art, logo, etc. Naming the real deliverable steers the model.
5. **Constraints** — what must not drift: `no watermark`, `no extra text`, `no
   added objects`, `preserve real proportions`.

The fifth slot is where most mediocre prompts fail silently. Describe the idea
without bounding it and the model gets inventive in directions you will regret.

The recommended ordering is consistent with OpenAI's own guidance:
**background/scene → subject → key details → constraints.** Labeled segments or
line breaks beat one dense paragraph for anything complex.

## Anti-slop discipline

**Replace vague praise with visual facts.**

- Avoid: stunning, incredible, epic, gorgeous, cinematic, masterpiece.
- Use instead: `overcast daylight`, `brushed aluminum`, `chipped paint`,
  `50 mm feel, soft bounce light`.

**Every style tag needs a visual target.** Instead of "minimalist brutalist
editorial luxury," specify: `cream background, heavy black condensed sans serif,
asymmetrical type block, one hero object, generous negative space`.

**Photoreal requires specificity.** Instead of "beautiful woman in museum":
`natural smile, realistic skin texture with visible pores, beige knit sweater,
dark jeans, white sneakers, eye-level full-body framing, marble floor
reflections, warm neutral color balance, shallow depth of field`.

- Name light **sources and direction**: `window light from camera left`,
  `incandescent work lamps`, `blue hour mixed with warm shop light`.
- Name **lens feel** and **believable imperfection**: `35 mm`, `50 mm`, film
  grain, slight chromatic aberration, faint reflections.
- Use the word `photorealistic` (or `real photograph`, `professional
  photography`) explicitly when the source is a photo. Detailed camera specs are
  interpreted loosely, so pair them with the visible effect (e.g. shallow depth
  of field) rather than relying on the number alone.

## Text rendering in images

Treat text like typography, not prose:

- Wrap literal text in quotes or ALL CAPS, transcribed **verbatim**.
- Specify font style, weight, size, color, and placement.
- Spell difficult words letter-by-letter when needed.
- State `no extra words` and `no duplicate text`.
- Mark critical strings as `EXACT TEXT` or `verbatim`.
- For small or dense text, use `quality="high"` (or at least `medium`).

## Three operating modes

1. **Generate from scratch** — endpoint `openai/gpt-image-2` with the five-section
   template. This is the text-only reproduction path.
2. **Edit a single image** — endpoint `openai/gpt-image-2/edit`. Separate
   **change** from **preserve**, and repeat the preserve list on every iteration
   to reduce drift. This is the exact-reproduction / faithful-variant path.
3. **Combine multiple images** — label each input by role and reference the
   labels in the instruction (`Image 1: base scene to preserve. Image 2: jacket
   reference.`). Up to 16 reference images are accepted.

## Fidelity: reference mode for exact reproduction

A text-only prompt cannot pixel-match a specific face, logo, or exact layout —
words discard that information. To actually reproduce an image, pass the original
back to the model:

- Use `openai/gpt-image-2/edit` with the original image as the reference input.
- Set `input_fidelity="high"` — this preserves likeness and geometry through
  larger edits.
- Provide an explicit **preserve list**: identity, face, pose, geometry, layout,
  framing, background, and any locked text. Example: `preserve identity,
  geometry, layout, and brand elements; do not alter saturation, contrast,
  camera angle, or surrounding objects`.
- Keep edits **surgical and one change per turn**; small iterative edits read
  better than one simultaneous rewrite.

When the goal is a true copy or a minimally-changed variant, reference mode is
the answer and the extracted text description is the *supporting* description,
not the whole rebuild.

## Generation parameters

| Parameter | Guidance |
| --- | --- |
| `quality="low"` | Fast, high-volume ideation; acceptable fidelity for many uses. |
| `quality="medium"` | Balanced; good default for general reproduction. |
| `quality="high"` | Small/dense text, infographics, close-up portraits, identity-sensitive edits. |
| `input_fidelity="high"` | On `gpt-image-2/edit`, preserves likeness during larger edits. |
| `num_images` | Usually `1` for a targeted reproduction. |
| `output_format` | `png` for crisp graphics/text; otherwise per need. |

## Aspect ratio and size

`gpt-image-2` size constraints:

- Both edges must be multiples of 16.
- Long-to-short ratio ≤ 3:1.
- Max edge < 3,840 px; total pixels between 655,360 and 8,294,400.
- Recommended reliability ceiling: 2,560 × 1,440 (2K).

Match the source aspect ratio to the nearest common size:

| Source shape | Use `image_size` |
| --- | --- |
| Square (~1:1) | `1024x1024` |
| Portrait (~2:3, taller) | `1024x1536` |
| Landscape (~3:2, wider) | `1536x1024` |

If the source is a non-standard ratio, pick the closest valid size and note the
crop/pad tradeoff rather than forcing an out-of-range dimension.

## Worked example

Source: a warm-lit ceramic coffee mug on a wooden café table, shallow depth of
field, morning window light.

```text
Scene: A quiet café interior in the morning, out-of-focus warm bokeh in the
background, natural window light spilling from camera left.

Subject: A single matte-cream ceramic coffee mug, centered, filled with black
coffee, gentle steam rising.

Important details: Ceramic with a soft matte glaze and one small chip near the
handle, resting on a worn oak table with visible grain; window light from camera
left, soft falloff to shadow on the right; 50 mm feel, shallow depth of field
with creamy background blur; warm neutral white balance; faint reflection of the
window on the coffee surface; subtle film grain.

Use case: Editorial lifestyle photograph.

Constraints: Photorealistic. No watermark, no text, no added objects. Preserve
realistic mug proportions and a single handle.
```

Settings: `image_size="1536x1024"` (landscape source), `quality="high"`,
`num_images=1`, `output_format="png"`.

Exact reproduction: instead of the above, call `gpt-image-2/edit` with the
original photo as reference, `input_fidelity="high"`, and preserve list
`preserve the mug shape, chip position, table grain, framing, and lighting; do
not change color balance or camera angle`.
