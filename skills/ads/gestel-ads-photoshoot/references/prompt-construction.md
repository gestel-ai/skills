# Prompt Construction for Product Photography

<!-- GESTEL local support doc for gestel-ads-photoshoot. Distilled from the -->
<!-- MIT-licensed claude-ads repo (commit 283d9d4917cb7c4f2ce9181e125bb1970f74ab04), -->
<!-- file ads/references/image-providers.md, with all credential / MCP / live-pricing / -->
<!-- account-mutation content removed and converted to a Boundary in the parent SKILL.md. -->
<!-- This doc is provider-neutral prompt-engineering methodology only. It does NOT assume -->
<!-- any generation backend (banana-claude, nanobanana-mcp, Gemini, OpenAI, Replicate, -->
<!-- Stability) is installed or authenticated. It produces prompt TEXT, not pixels. -->

## What this doc is for

A photoshoot prompt is a structured string plus a target size and a treatment hint.
This doc gives you the provider-neutral grammar to write that string well, regardless
of which generator eventually runs it. The actual generation, cost, and file output are
out of scope for this skill — see the Boundaries section of `SKILL.md`.

## The 5-Component Prompt Formula

Build every product-photo prompt from these five ordered components. Each style template
in `SKILL.md` is a pre-filled instance of this formula; use this when you need to adapt
or extend a template.

1. **[SUBJECT]** — physical details, appearance, material of the product. Pull from the
   user's product description. Be specific (e.g., "matte black ceramic travel mug with a
   bamboo lid"), not generic ("a mug").
2. **[ACTION / STATE]** — what the product is doing or how it sits: floating, held in
   hands, flat-laid, standing on a surface, in use.
3. **[LOCATION / CONTEXT]** — where, when, atmosphere. For Studio this is a seamless
   sweep; for Lifestyle it is an environment implied by `target_audience`.
4. **[COMPOSITION]** — camera angle, framing, perspective, negative space, where the
   subject sits in the frame (critical for 9:16 safe zones — see the spec docs).
5. **[STYLE]** — lighting, lens feel, brand-voice-mapped attributes, mood keywords,
   and an explicit aspect-ratio statement. End with the negative list (forbidden colors,
   forbidden imagery from brand DNA).

Keep the prompt tight: state the aspect ratio explicitly, cap any in-image text at a few
words (real ad copy goes in platform copy fields, not baked into the photo), and avoid
requesting product UI screenshots (capture real ones instead — generators hallucinate UI).

## Treatment Hint: Product vs Editorial

Many generators expose a "mode" or you can steer with descriptors. Map styles this way so
the brief carries intent regardless of backend:

| Style | Treatment hint | Why |
| --- | --- | --- |
| Studio | **Product / packshot** | Clean, catalog-accurate, even lighting |
| Floating | **Product / packshot** | Product is the hero; controlled background |
| Ingredient | **Product / packshot** (flat-lay) | Top-down catalog clarity |
| In Use | **Editorial / lifestyle** | Human context, shallow depth of field |
| Lifestyle | **Editorial / lifestyle** | Environmental story, aspirational mood |

When you hand the brief to a generator that has named domain modes (e.g. Product,
Editorial, Cinema, Portrait), pass the hint above. When it does not, fold the hint into
the [STYLE] component as words ("clean ecommerce packshot lighting" vs "editorial
lifestyle photography, shallow depth of field, warm natural light").

## Aspect Ratio → Platform Map

Always state the ratio in the prompt AND record the target pixel size in the brief.

| Ratio | Pixels | Platform use |
| --- | --- | --- |
| 1:1 | 1080x1080 | Meta Feed, LinkedIn, carousel cards |
| 4:5 | 1080x1350 | Meta Feed (preferred), Instagram Feed |
| 9:16 | 1080x1920 | TikTok, Reels, Shorts, Stories |
| 16:9 | 1920x1080 | YouTube, Google Display, LinkedIn |
| 2:3 | 800x1200 | Pinterest, posters |
| 4:1 | 1200x300 | Website / leaderboard banners |

Note: some generators do not natively support 1.91:1 (the Google PMax / LinkedIn link
ratio). The portable workaround is to generate 16:9 and crop to 1200x628 in post — record
that crop step in the brief rather than assuming native support.

## Safe Zones

For any 9:16 output, the bottom ~35% and the right-edge icon column are covered by
platform UI. Keep the product, faces, and any critical element in the center safe box.
See `meta-creative-specs.md` and `tiktok-creative-specs.md` for exact pixel boxes and the
prompt modifiers that push the subject into the safe zone ("subject in top 60% of frame,
bottom third clear background").

## Iterative Refinement

If a first pass would not match brand expectations, refine the prompt by adjusting ONE
lever at a time, in this order of leverage: lighting direction → color temperature →
background texture/color → product angle → composition/negative space. Record the changed
lever in the brief so the next generation pass is reproducible. Because this skill does
not run the generator, "refinement" here means producing a revised prompt spec, not
re-rolling pixels.

## Cost & Output (routed out)

Per-image cost, resolution tiers, batch discounts, rate limits, and the actual saved
`.png` files all depend on the chosen paid provider and its credentials. This skill does
not price or generate. The brief should instead carry the **inputs a cost estimate needs**
(number of styles x number of sizes = image count, plus desired resolution) so whoever
runs the provider adapter can compute spend and confirm before generating.
