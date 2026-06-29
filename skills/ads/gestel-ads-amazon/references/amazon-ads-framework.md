<!-- Used by: gestel-ads-amazon -->
<!-- Distilled from claude-ads/skills/ads-amazon/SKILL.md (MIT, commit 283d9d49) -->
<!-- Stable methodology. Freshness-sensitive facts (report names, surfaces,
     market-share figures) are NOT verified here — gate them per SKILL Boundaries. -->

# Amazon Ads Framework — Seven Scoring Categories

Each category below lists what to inspect and why. The weights and
pass/warning/fail thresholds live in `benchmarks-and-scoring.md`. Evaluate every
check against the user-supplied exports; never assume console access.

## 1. Campaign Structure & Portfolios (15%)

- **Portfolio organization** — campaigns grouped by funnel stage (Awareness /
  Consideration / Conversion) or by product line, not ad-hoc.
- **Naming convention** consistent and machine-parseable
  (e.g. `SP_Brand_Exact_USD_Conv`, `SB_NonBrand_HSA_Video_USD_Cons`).
- **Auto vs Manual mix** — Sponsored Products has ≥1 Auto campaign per ASIN
  cluster for search-term harvesting (the auto-mining workflow).
- **ASIN-level coverage** — every priority ASIN appears in ≥1 Manual SP
  campaign (Exact, Phrase, or Broad) **and** ≥1 Auto campaign.
- **Targeting-type mix in SP** — Manual Keyword + Manual Product (ASIN
  targeting) + Auto (for harvesting). Pure Auto is a learning-only state.
- **Sponsored Brands** — at least one HSA (Headline Search Ad) campaign per
  brand storefront; SB Video tested for high-AOV products.
- **Sponsored Display** — separate Audience (retargeting + lookalike) and
  Contextual (product/category) campaigns; never mixed in one campaign.

## 2. Search-Term Harvesting & Negatives (25%) — highest weight

- **Auto → Manual harvest cadence** weekly or bi-weekly: pull converting search
  terms from Auto, promote winners to Manual Exact in their target campaign, and
  add them as negatives to the Auto so spend redirects.
- **Negative keyword coverage** — every Auto campaign carries the Manual
  campaign's ASIN keywords as negatives (prevents Auto cannibalizing Manual
  placements).
- **Negative product targeting** — irrelevant ASINs added at campaign level
  (keeps Sponsored Display contextual off incompatible products).
- **Recency** — Search Term Report harvested within the last 7 days; any
  high-spend, zero-conversion term above ~$10 / 30 days should be a negative.
- **Brand defense** — branded search terms isolated in a separate exact-match
  campaign with competitor-name negatives.
- **Top-of-search visibility** — compare branded-search auction CPC vs default;
  flag if a competitor is bidding above your brand-defense bid.

## 3. ACOS / TACOS Discipline (20%)

- **ACOS targets set per portfolio** from contribution margin
  (`target ACOS = (1 − contribution_margin) × buffer`). A flat "30% across the
  board" target is itself a finding.
- **TACOS trending down** quarter-over-quarter — TACOS = total ad spend / total
  revenue including organic; a downward trend means paid is lifting organic, not
  replacing it.
- **ROAS reported alongside ACOS** for teams that think in ROAS.
- **Coupon + Lightning Deal stacking** — when live, relax ACOS targets to
  capture lift; auto-flag campaigns that need a temporary ACOS uplift.
- **Day-parting** — bid adjustments by hour for ASINs where add-to-cart hours
  differ from purchase hours (common for high-AOV electronics). *(Feature
  availability is freshness-sensitive — verify before asserting.)*

## 4. Bid & Budget Management (15%)

- **Dynamic bidding strategy** — `Up and Down` for Manual Exact converting
  campaigns; `Down Only` for Auto campaigns and Sponsored Display contextual
  (avoid bid escalation in learning campaigns).
- **Placement bid multipliers** — Top-of-search adjusted by ROAS-by-placement
  from the Placement Report (often +50–100% for top-of-search, −30% for
  product-page placements; treat the exact multipliers as starting heuristics,
  not guarantees).
- **Budget caps appropriate** — no campaign capped below ~2× current daily spend
  (caps strangle algorithm learning).
- **Bulk bid adjustments** — bid optimization runs weekly via Bulk Operations,
  not ad-hoc in the UI.

## 5. Sponsored Brands (10%)

- **HSA (Headline Search Ad)** — brand logo + 3-product showcase + landing
  destination (Store, custom URL, or product list).
- **SB Video** — 6–45s; 15–30s sweet spot; hook within 2s; captions on.
  Recommended for high-AOV products.
- **Brand Store linked** as landing destination where available (typically
  higher CVR than the product detail page).
- **Negative keywords on SB** include competitor brand names if you do not want
  top-of-funnel competitor traffic; remove them if you do.

## 6. Sponsored Display (10%)

- **Audience targeting** — Views Remarketing, Purchase Remarketing, Cross-Sell,
  and Lookalike audiences each scaled with appropriate bids.
- **Contextual targeting** — relevant categories **and** specific ASIN targeting
  (your own complementary products + competitor ASINs you can win).
- **Display creative quality** — at minimum the default product creative; custom
  creative tested for top SKUs.
- **Off-Amazon Sponsored Display** (third-party sites / apps) audited separately
  — different CPC dynamics and attribution windows. *(Available surfaces are
  freshness-sensitive — verify before naming specific properties.)*

## 7. Brand Analytics & Reporting (5%)

- **Brand Analytics accessed** (Brand-Registered only): Top Search Terms, Item
  Comparison, Repeat Purchase Behavior. *(Report names/availability are
  freshness-sensitive — confirm against the user's actual console.)*
- **Top Search Terms** used to find share-of-voice gaps vs competitors on
  category keywords.
- **Repeat Purchase Behavior** informs subscription / replenishment ad strategy.
- **Amazon Attribution** tracked if running external (off-Amazon) ads driving to
  Amazon listings.

## Deliverables this framework feeds

- Per-category findings with the health score from `benchmarks-and-scoring.md`.
- Search-term harvest plan: promote-to-Manual list + negative list, ranked by
  estimated spend recovery ($).
- ACOS-by-ASIN matrix highlighting SKUs over their margin-derived target.
- Sponsored Brands video opportunity list (priority ASINs without SB Video).
- Pre-launch checklist for entering a new product category.
- Basic Amazon DSP entry recommendation (yes/no on total monthly spend and
  audience size only — full DSP audit is out of scope per SKILL Boundaries).
