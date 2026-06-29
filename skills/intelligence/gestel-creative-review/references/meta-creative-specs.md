<!-- Updated: 2026-06-28 | v1.0 -->
<!-- Distilled from claude-ads ads/references/meta-creative-specs.md (MIT) and marketingskills ad-creative references/platform-specs.md (MIT). -->
<!-- Used by: gestel-creative-review (Platform Fit gate) -->

# Meta And Instagram Static Creative Specs

Concrete dimensions, safe zones, and copy limits for the GESTEL static review gate.
These are the placement facts the Platform Fit gate checks against.

> Freshness warning: dimensions, copy limits, and disclosure rules can change.
> Verify against live Meta/Instagram documentation, or cite a dated source, before
> asserting any freshness-sensitive platform fact in a review result.

## Image Specs By Placement

| Placement | Ratio | Dimensions | GESTEL priority |
| --- | --- | --- | --- |
| Feed (preferred) | 4:5 | 1080x1350 | Primary first-pack target |
| Feed (square) | 1:1 | 1080x1080 | Expansion after candidate selection |
| Stories | 9:16 | 1080x1920 | Expansion after candidate selection |
| Reels (static) | 9:16 | 1080x1920 | Expansion after candidate selection |

- Minimum width 600px; 1080px recommended.
- The first pack defaults to 4:5. Do not pre-generate every ratio before the user
  selects candidates unless scope is explicitly widened.

## Safe Zones

### 9:16 (Stories / Reels, 1080x1920)

- Top ~120px: status bar area — avoid critical content.
- Bottom ~35% (~670px): UI overlay (CTA button, caption, reactions, profile) — avoid
  placing product, faces, price, badges, or headline here.
- Keep all critical elements in the center ~1080x1300 zone, ideally the top 60% of frame.

### 4:5 and 1:1 (Feed)

- No hard safe zone, but the bottom ~120px can be covered by the like/comment bar on mobile.
- Keep the primary subject and price text in the upper ~80% of the frame.

## Copy Limits

| Component | Recommended | Notes |
| --- | --- | --- |
| Primary text | 40-125 chars visible | Anything past ~125 chars truncates with "See More"; the key message must land in 125. |
| Headline | 27-40 chars | Below image. |
| Description | ~20-30 chars | May not render on all placements. |
| Reels/Stories overlaid text | <= 72 chars visible | Keep short for mobile. |
| CTA button | Predefined list | Not free text. |

For Korean commerce copy, also check that the copy reads naturally at feed size and is
not too dense for mobile, regardless of the raw character count.

## Advantage+ Creative Crop Implication

If Advantage+ Creative enhancements are enabled, Meta may re-crop the image to other
aspect ratios and adjust brightness/contrast. Treat critical elements near any edge as
crop-risk and keep product, logo, price, and headline well inside the frame.

## Composition Guidance (Placement-Agnostic)

These are review heuristics for whatever upstream renderer produced the asset; this gate
does not generate images itself (see SKILL.md Boundaries):

- Subject fills the upper portion of the frame; bottom third is clean background for 9:16.
- High contrast and a clear focal product (thumb-stopping at feed scale).
- Faces and product not cropped at edges.
- Required advertising / sponsorship / AI-virtual-person / price / limited-quantity
  disclosures stay visible inside the safe zone when applicable.
