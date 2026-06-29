<!-- Updated: 2026-06-28 | v1.0 -->
<!-- Used by: gestel-ads-youtube -->
<!-- FRESHNESS: Format rules and benchmarks below are PRIORS distilled from source
     research, NOT current truth. Platforms change durations, ratios, CTA timing, and
     measurement behavior frequently. Verify against a live source before asserting. -->

# YouTube Format Specs & Benchmark Snapshots

## YouTube Ad Formats

| Format | Ratio | Resolution | Duration | Skip | Typical bidding |
| --- | --- | --- | --- | --- | --- |
| Skippable In-Stream (TrueView) | 16:9 | 1920×1080 | 12s–3min (rec 15–30s) | After 5s | Target CPV / Target CPA |
| Non-Skippable In-Stream | 16:9 | 1920×1080 | 15–60s (expanded 2025) | No | Target CPM |
| Bumper | 16:9 | 1920×1080 | ≤6s | No | Target CPM |
| In-Feed (Discovery) | 16:9 | 1920×1080 | Any | N/A | varies |
| YouTube Shorts | 9:16 | 1080×1920 | ≤60s | Swipe | Demand Gen / Video View |
| CTV Non-Skippable | 16:9 | 1920×1080 | 30s | No | Target CPM |

## YouTube Shorts

- **Safe zone:** center **1080×1420px**. Bottom **480px = UI overlay** — keep critical
  text, logos, faces, and CTAs out of it; place the main subject in the upper portion.
- **CTA timing:** the CTA button appears at **3 seconds** for PMax/App/Demand Gen
  campaigns, **10 seconds** for Video View/Reach campaigns.
- **Sound-on** is expected; music/voiceover is reported to lift conversions ~20%+
  (prior — flag).
- **Placement exclusions for Shorts work at account level only**, not campaign/ad-group.

## Demand Gen (VAC successor)

- Placements: YouTube Home Feed, Watch Next, Discover, Gmail, and Google Display
  Network (with channel controls).
- **Multi-format uplift (prior):** uploading both video AND image assets is reported to
  deliver ~20% more conversions at the same CPA vs video-only.
- **Frequency capping is NOT supported.** Only workaround: Video Frequency Groups
  (alpha). This is a real loss vs VAC for former frequency-capped campaigns.

## Connected TV (CTV)

- 30s non-skippable available on CTV; shoppable CTV uses Merchant Center feeds with QR
  codes.
- CTV-specific creative: larger text, simpler visuals for TV viewing distance.
- **Critical measurement limitation:** Floodlight conversion measurement does NOT work
  on CTV devices. Use Google Ads conversion tracking or GA4 instead.
- "~75% of YouTube ad spend now on CTV" and "~150M Americans watching on TV" are dated
  priors — flag, do not assert as current.

## Benchmark Snapshots (priors — not current truth)

| Metric | Prior value | Notes |
| --- | --- | --- |
| View Rate (skippable) | ≥15% good | Higher = stronger hook |
| CPV (skippable) | $0.01–0.10 | Varies heavily by targeting/market |
| VTR (bumper) | ~90%+ | Non-skippable, should approach 100% |
| CPM (non-skippable) | $6–15 | Market-dependent |
| CTR (Demand Gen) | ≥0.5% | Image + video combined |
| Demand Gen video+image | ~20% more conversions vs video-only | Dated stat |
| CTV ad spend share | ~75% of YouTube ad spend (prior) | Dated stat |

All figures are snapshots distilled from source research at one point in time. Treat as
directional priors; confirm with a dated/live source before presenting as today's value.
