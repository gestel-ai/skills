<!-- Updated: 2026-06-28 | v1.0 -->
<!-- Sources (provenance only, not a runtime dependency): marketingskills/skills/ad-creative/references/platform-specs.md (MIT, 8bfcdffb); claude-ads/skills/ads-creative/SKILL.md (MIT, 283d9d49); claude-ads/skills/ads-plan/assets/ecommerce-creative.md (MIT, 283d9d49) -->
<!-- Used by: gestel-creative-package -->

# Platform Specs (Meta and Instagram, Static Image Packs)

GESTEL ships static product-photo image packs for Meta and Instagram only. This file holds
the local spec contract used when filling slots, validating copy length, and expanding ratios.
It deliberately omits Google, LinkedIn, TikTok, Twitter/X, and video formats — those are
out of scope and belong to a separate future design, not this skill.

Meta and Instagram change specs without notice. These values are an evergreen working baseline.
Before making a permanent platform claim to a user, verify live documentation or add a dated,
sourced reference and a refresh trigger.

## Text Element Limits

Character limits below are Latin-character guidance. Korean (`ko-KR`) copy renders wider per
glyph, so treat these as ceilings and prefer shorter, mobile-first lines. Always confirm in the
Meta ad preview before calling anything launch-ready.

| Element | Visible / Recommended | Maximum | Notes |
| --- | --- | --- | --- |
| Primary text | ~125 chars before "더 보기" truncation | 2,200 chars | Front-load the hook in the first line. |
| Headline | ~40 chars | 255 chars | Shown below the image; keep the value or CTA here. |
| Description | ~30 chars | 255 chars | May not render in every placement; never load-bearing. |
| In-image text overlay | Keep critical text minimal | — | Heavy overlay reduces delivery; keep well inside the safe zone. |

Placement notes:

- Feed: all elements can show; primary text is most visible.
- Stories and Reels (static): treat primary text as overlaid; keep under ~72 chars and inside the safe zone.
- Korean copy: avoid machine-translated stiffness, exaggerated medical or financial certainty, and unverifiable superlatives.

## Image and Ratio Specs

GESTEL's first pack is 4:5. Expand to 1:1 and 9:16 only after the user selects candidate variants.

| Placement | Aspect Ratio | Recommended Size | First-pack role |
| --- | --- | --- | --- |
| Feed (vertical) | 4:5 | 1080 x 1350 | Default first-pack ratio. |
| Feed (square) | 1:1 | 1080 x 1080 | Ratio expansion after candidate selection. |
| Stories / Reels (static) | 9:16 | 1080 x 1920 | Ratio expansion after candidate selection. |

Safe-zone guidance:

- Keep headline, badge, price, and CTA centered and away from edges.
- A ~900 x 1000 px usable core works across the vertical placements above.
- For 9:16, keep critical elements clear of the top and bottom UI bands (roughly the top ~250 px and bottom ~340 px).
- Most impressions are mobile; check legibility at phone scale.

## Copy Validation Rules (applied before launch-ready)

1. Every slot value fits its element ceiling; over-limit copy gets a trimmed alternative, not silent truncation.
2. Product form, color, package, and label stay faithful to the source photo — no invented product attributes.
3. Every factual claim (price, discount, ranking, certification, ingredient, effect, shipping promise, review quote, deadline) carries an evidence ID or URL, or it is softened or removed. See [slot-contract](slot-contract.md).
4. Required disclosures (advertising/sponsorship, AI virtual person, limited quantity, price evidence) are present when the corresponding claim is present.

## Creative Diversity and Fatigue (planning guidance)

These are planning heuristics for what to put in a package, not live-metric reads (GESTEL does not read ad accounts).

- Distinct concepts beat minor variants. Meta's retrieval engine clusters near-identical creatives, so color swaps and tiny text edits across a pack add little. Vary the angle, layout family, and value proposition, not just wording.
- A first pack of three should use three different template families and three different angles, not three recolors of one idea.
- When the user later brings their own performance export, map winners and losers by `variant_id` / `utm_content` (see [export-contract](export-contract.md)) and refresh by introducing genuinely new angles, not by re-tinting fatigued ones.
