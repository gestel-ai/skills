# Image Extraction Checklist

The observation method for reverse-engineering an image. Read the picture against
every dimension below and record **concrete visual facts** — the kind of detail
that lets GPT Image 2 rebuild the shot, not adjectives that praise it. Facts you
cannot read from the image are low-confidence: flag them, do not invent them.

Work top to bottom; the order roughly matches the five-section prompt so the
notes assemble cleanly afterward.

## 1. Medium and overall read

- Is it a **photograph, 3D render, illustration, painting, or graphic/UI**? This
  decides whether to say `photorealistic` or name the medium.
- Overall mood in visual terms (not "epic" — say `overcast and muted` or
  `high-key and clean`).

## 2. Aspect ratio and framing

- Aspect ratio: square, portrait, landscape, or non-standard. Record it so you
  can pick the nearest valid `image_size`.
- Crop: full scene, tight crop, headroom, rule-of-thirds placement.

## 3. Scene and environment

- Location and time (interior/exterior, day/night, season, weather).
- Background contents and depth: what is behind the subject, in focus or bokeh.
- Foreground elements, if any.

## 4. Subject(s)

- The main focus: who or what, how many.
- Scale and placement within the frame (centered, off to one side, filling the
  frame).
- For people: body framing (full body, waist-up, headshot), pose, gesture,
  expression, wardrobe, hands.
- For products/objects: form, orientation, count, condition.

## 5. Composition and viewpoint

- Camera angle: eye-level, low-angle, high-angle, top-down/flat-lay.
- Distance: close-up, medium, wide.
- Symmetry, leading lines, negative space, layering.

## 6. Camera and lens feel

- Apparent focal length / lens character: wide distortion, `35 mm`, `50 mm`,
  telephoto compression.
- Depth of field: deep (all sharp) vs shallow (subject sharp, background creamy).
- Motion blur or freeze.

## 7. Lighting

- Source(s) and **direction**: window from camera left, overhead, backlit, rim
  light, ring light, mixed sources.
- Quality: soft/diffuse vs hard/direct; contrast level.
- Time-of-day signature: golden hour, blue hour, midday, artificial.
- Shadows: length, softness, direction; highlights and reflections.

## 8. Color and grading

- Dominant and accent colors — give **Hex** where you can read them confidently.
- White balance / color temperature: warm, neutral, cool.
- Grading feel: natural, teal-orange, desaturated, high-saturation, monochrome.

## 9. Materials and textures

- Surfaces and materials: brushed aluminum, matte ceramic, knit wool, glossy
  plastic, raw concrete, oak grain.
- Texture detail: pores, fabric wear, scratches, condensation, dust.

## 10. Style and post-processing

- Named visual style only if you anchor it to concrete elements (see anti-slop
  rules in the prompting reference).
- Post effects: film grain, vignette, chromatic aberration, HDR, bloom.

## 11. Text in the image

- Transcribe every readable string **verbatim**, in quotes.
- Note font style, weight, color, size, and placement.
- Note logos/marks — but remember exact logo reproduction needs reference mode,
  not text.

## 12. Believable imperfection

- Reflections, smudges, wear, asymmetry, sensor noise. These sell realism; name
  them so the model does not render a sterile, too-perfect image.

## Confidence pass

Before writing the prompt, mark anything ambiguous: occluded objects, unreadable
text, uncertain materials, or details the resolution does not support. Carry
these into the output as **low-confidence reads** so the user knows what the
prompt is guessing at.
