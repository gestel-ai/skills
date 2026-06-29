# Generation Briefing, Prompting, Manifest & Quality Gate (distilled)

Deep support for `gestel-ads-generate`. This is render-agnostic: it produces prompts, a manifest
spec, a cost-estimate method, and a review rubric. It does **not** invoke any paid image provider —
the actual render is a Boundary (see the skill's Boundaries section).

## 1. Brief schema (`## Image Generation Briefs`)

Each brief entry should resolve into a job with these fields:

| Field | Meaning |
| --- | --- |
| `concept_id` | Stable ID grouping all platform sizes of one creative idea. |
| `angle` | The reason the viewer stops/clicks (proof, problem-relief, offer, comparison, feature). |
| `mode` | Creative-direction mode: Product / Editorial / Cinema / UI-Web / Portrait. |
| `platforms` | Target platforms + placements (fan out to one job per size). |
| `ratios` | Required aspect ratios/dimensions. |
| `headline` | In-image text, 3-5 words max. |
| `product_constraints` | True color, packaging, label, evidence-backed claims only. |

One `concept_id` typically yields several jobs (e.g. Meta 4:5, Meta 9:16, Google 1:1).

## 2. Creative-direction modes

These steer composition, lighting, and prompt vocabulary (upstream "domain modes").

- **Product** — packshots, e-commerce. Clean studio or contextual surface, true color, sharp
  product edges, no fabricated packaging detail.
- **Editorial** — brand/lifestyle. Natural scene, aspirational human framing, soft narrative light.
- **Cinema** — dramatic hero / video thumbnail. High contrast, directed key light, depth, one focal
  subject.
- **UI / Web** — app-install / SaaS. Real product UI framed in a device or browser mock. Capture a
  real screenshot; never let a generative model invent UI.
- **Portrait** — testimonial / founder / people. Subject-forward, flattering light, shallow depth.

## 3. Prompt framework

Structure: **Subject + Setting + Style + Lighting + Composition + Technical.**

- 40-80 words; specific beats comprehensive.
- Always state the aspect ratio explicitly.
- Inject brand color + mood from `brand-profile.json` (named hex/mood, not "on brand").
- Cap baked-in text at 3-5 words; add longer copy in post or as the ad's text field.
- Keep product faithful: form, color, package, label match the source photo.
- Logos: add in post — generative placement is unreliable.

Brand injection from `brand-profile.json` (example fields → prompt use):

```text
primary_color / accent_color → palette direction
tone / mood                  → lighting + styling adjectives
typography                   → only relevant if text is composited later (note, don't bake)
product_reference            → fidelity anchor (do not deviate)
```

### Worked examples

**Product mode, Meta 4:5 (1080x1350):**
> Studio packshot of a matte amber skincare bottle centered on a smooth sand-toned surface, single
> soft sapphire-blue (#1B3A6B) gradient backdrop matching brand, diffused top-left key light with
> gentle reflection, generous negative space above for a 3-word headline, 4:5 vertical, high detail,
> true-to-label color, photorealistic. (no baked text)

**Cinema mode, YouTube thumbnail (1280x720):**
> Dramatic close-up of the product held toward camera, high-contrast directed light against a deep
> teal background, strong focal subject with shallow depth, bold negative space on the right for a
> 3-word hook, 16:9, cinematic, photorealistic. (headline composited in post)

**UI/Web mode, Google portrait (960x1200):**
> Clean phone mockup showing the app's real dashboard screenshot, soft studio gradient in brand
> indigo, subtle shadow, centered device, 4:5, crisp, modern SaaS look. (UI = real capture, not
> generated)

## 4. Cost estimate method

`estimated_cost = number_of_image_jobs × per_image_price_of_user_render_path`

State the render path the price assumes (it is the user's path, not an assumed installed provider).
Show the estimate before routing to render. If it exceeds ~$1.00, ask for confirmation. This is a
planning estimate, not a billing action. Indicative public per-image prices to confirm against live
docs (drift; verify): gpt-image-1 ~$0.04, Stability SD 3.5 ~$0.065, Replicate FLUX.1 Pro ~$0.055.

## 5. Manifest spec

`ad-assets/generation-manifest.json` — array of job records:

```json
{
  "concept_id": "proof-01",
  "angle": "social_proof",
  "mode": "product",
  "platform": "meta",
  "placement": "feed",
  "dimensions": "1080x1350",
  "ratio": "4:5",
  "prompt": "<final prompt>",
  "brand_preset": "<brand-slug or null>",
  "output_path": "ad-assets/meta/proof-01/feed-1080x1350.png",
  "cost": null,
  "quality_score": null,
  "status": "planned"
}
```

`cost`, `quality_score`, and `status` (`planned` → `rendered` → `passed`/`rejected`) are filled
after the render and quality gate by whoever runs them. Asset path convention:
`ad-assets/[platform]/[concept]/[placement-WxH].png`.

## 6. Quality gate (post-render)

Score each rendered asset 1-10 on brand alignment, composition, and platform fit:

- **9-10** — professional, brand-aligned, platform-optimized. Ship.
- **7-8** — good; minor composition/brand improvement possible.
- **5-6** — acceptable but regenerate once: text readability, weak composition, or brand mismatch.
- **Below 5** — reject; regenerate with an adjusted prompt.

**Format check:** confirm every required placement/dimension from the brief was produced. Report
missing or mis-sized formats explicitly (a `format-report`) rather than shipping a partial set.

## 7. Report shape

```text
Generation plan (render routed out):
  Concept proof-01 (social_proof, product mode)
    - meta/feed     1080x1350 (4:5)  → ad-assets/meta/proof-01/feed-1080x1350.png
    - meta/reels    1080x1920 (9:16) → ad-assets/meta/proof-01/reels-1080x1920.png
  Estimated render cost: $N (path: <user render path>) — confirm before render
  Manifest: ad-assets/generation-manifest.json
  Post-render: apply quality gate (1-10) + format check
  Next: route render to <adapter / implementation task / user-supplied assets>
```
