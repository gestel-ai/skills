# Platform Ad Creative Specs (distilled)

Per-platform image-ad dimensions, ratios, and safe-zone notes used to size each generation job.
These specs **drift** — treat them as a strong default, but verify against the platform's current
ad-spec docs before committing real spend. Pixels are minimums for crisp display; larger at the
same ratio is fine.

## Meta (Facebook / Instagram)

| Placement | Pixels | Ratio | Notes |
| --- | --- | --- | --- |
| Feed (FB/IG) | 1080x1350 | 4:5 | Default primary. Tallest ratio Meta serves in-feed; maximizes screen share. |
| Feed square | 1080x1080 | 1:1 | Safe universal fallback across placements. |
| Stories / Reels | 1080x1920 | 9:16 | Keep text/CTA out of top ~14% and bottom ~20% (UI overlays). |
| Right column | 1200x628 | 1.91:1 | Desktop only; tiny render — minimal text. |

Safe zone: center critical product + headline; assume edges crop per placement. In-image text
minimal (Meta no longer hard-rejects >20% text but heavy text still suppresses delivery).

## Google (Performance Max / Display)

| Asset | Pixels | Ratio | Notes |
| --- | --- | --- | --- |
| Landscape | 1200x628 | 1.91:1 | Required for PMax/Display. |
| Square | 1200x1200 | 1:1 | Required. |
| Portrait | 960x1200 | 4:5 | Recommended. |
| Logo (square) | 1200x1200 | 1:1 | Plus 1200x300 (4:1) landscape logo. |

PMax wants multiple ratios of each concept — plan landscape + square + portrait per concept. Keep
~20% text-free margin; Google penalizes overlaid-text-heavy images.

## TikTok

| Placement | Pixels | Ratio | Notes |
| --- | --- | --- | --- |
| In-feed (image/thumb) | 1080x1920 | 9:16 | Full-screen vertical native. |
| Square fallback | 1080x1080 | 1:1 | Lower performance; avoid if possible. |

Safe zone: keep text/logo clear of right-side action rail and bottom caption/CTA band
(~top 8%, bottom ~35%, right ~12%). Native, non-polished look outperforms slick studio ads.

## LinkedIn

| Asset | Pixels | Ratio | Notes |
| --- | --- | --- | --- |
| Single-image feed | 1200x1200 | 1:1 | Default; strong on mobile feed. |
| Landscape | 1200x628 | 1.91:1 | Link-share style. |
| Carousel card | 1080x1080 | 1:1 | Per-card. |

B2B context: professional tone, legible at small feed size, value-prop-forward.

## YouTube

| Asset | Pixels | Ratio | Notes |
| --- | --- | --- | --- |
| Video thumbnail | 1280x720 | 16:9 | High-contrast, large readable focal subject. |
| Companion banner | 300x250 | — | Display companion to video. |
| Shorts thumb/cover | 1080x1920 | 9:16 | Vertical. |

Thumbnails are a click contract — face/product + 2-3 word hook, high contrast for small render.

## Microsoft (Bing) Audience/Display

| Asset | Pixels | Ratio | Notes |
| --- | --- | --- | --- |
| Landscape | 1200x628 | 1.91:1 | Primary. |
| Square | 1200x1200 | 1:1 | |
| 4:5 portrait | 1200x1500 | 4:5 | |

Mirrors Google ratios; reuse Google assets when budgets are shared.

## Cross-platform rules

- Center critical content; assume per-placement edge crop.
- In-image text 3-5 words max; longer copy belongs in the ad's text field, not baked pixels.
- Maintain product fidelity (true color, real packaging/label) across every ratio of a concept.
- Plan the tallest/most-constrained placement first, then expand to wider ratios of the same concept.
