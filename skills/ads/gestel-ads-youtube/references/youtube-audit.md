<!-- Updated: 2026-06-28 | v1.0 -->
<!-- Used by: gestel-ads-youtube -->
<!-- FRESHNESS: Thresholds, dated stats, and migration dates below are PRIORS distilled
     from source research, NOT current truth. Verify any "as of <year>" claim, format
     rule, or benchmark against a live source before asserting it. -->

# YouTube Ads Audit Checklist

Mark each applicable check **PASS / WARNING / FAIL / N/A**. N/A = the campaign type or
data isn't present; N/A is excluded from the score (never scored as fail). Severity
feeds the weighted score (Critical 5.0, High 3.0, Medium 1.5, Low 0.5).

## Campaign Setup

| ID | Check | Severity | PASS | WARNING | FAIL |
| --- | --- | --- | --- | --- | --- |
| YT-01 | Skippable In-Stream fit | Medium | 16:9, ≥12s (15–30s), Target CPV/CPA, View Rate ≥15% | View Rate 10–15% or length <12s | View Rate <10% or wrong bid type |
| YT-02 | Non-Skippable fit | Medium | 16:9, ≤60s, Target CPM, message complete | Length untested | Message cut off / wrong objective |
| YT-03 | Bumper fit | Low | Exactly 6s, Target CPM, single message, brand visible | Multi-message in 6s | >6s or no brand presence |
| YT-04 | Shorts format | High | 9:16 1080×1920, sound-on, CTA timed, creator-like | Repurposed 16:9 without recut | No vertical asset for Shorts demand |
| YT-05 | Demand Gen present & set up | High | DG live with audience signals + product feed | DG live but thin signals | Eligible account running no DG |
| G-DG1 | Demand Gen multi-format assets | High | DG includes BOTH video AND image assets | Video only (missing ~20% uplift) | No assets diversity |
| G-DG2 | VAC migration status | Critical | All VACs migrated to Demand Gen | Migration in progress | VAC still active (deprecated, force-migrate) |
| G-DG3 | Demand Gen frequency-cap loss | High | Former freq-capped VACs have a replacement strategy (Video Frequency Groups alpha or manual monitoring) | Frequency monitored ad hoc | Former VAC relied on freq caps, no replacement |
| YT-CTV | CTV setup | Medium | CTV creative tuned (large text, simple visuals), QR shoppability where used | CTV running, creative not TV-optimized | CTV creative unreadable on TV |

## Creative Quality

| ID | Check | Severity | PASS | WARNING | FAIL |
| --- | --- | --- | --- | --- | --- |
| YT-06 | Hook (first 5s) | High | Attention captured ≤5s, brand/benefit early | Slowish open | Title card / logo-only / dead intro |
| ABCD | ABCD compliance | High | Attention + Branding + Connection + Direction all present | One pillar weak | Two+ pillars missing |
| YT-07 | Production quality | Medium | HD 1080p+, clear audio, captions, strong end screen | Captions missing OR weak end screen | Low-res / poor audio |
| YT-08 | Creative volume | Medium | ≥3 distinct video variations, mixed lengths, refreshed 4–8 wks | 2 variations or stale >8 wks | 1 creative / never refreshed |
| YT-09 | Aspect coverage | Medium | Both 9:16 and 16:9 cuts available | One ratio only | Cannot serve a present surface |

## Audience Targeting

| ID | Check | Severity | PASS | WARNING | FAIL |
| --- | --- | --- | --- | --- | --- |
| YT-10 | Targeting strategy | High | Appropriate mix (Custom Intent / In-Market / Affinity / Customer Match / Placement) for funnel stage | Single broad layer | No deliberate targeting |
| YT-11 | Remarketing setup | Medium | Prospecting vs retargeting split; converters excluded from prospecting | Split exists, no exclusions | One blended campaign |
| YT-12 | Frequency management | Medium | Caps set to goal (3–5/wk awareness, 1–2/wk DR; TF ~4/wk) | Caps default/untuned | No frequency control where supported |

## Measurement

| ID | Check | Severity | PASS | WARNING | FAIL |
| --- | --- | --- | --- | --- | --- |
| YT-13 | Metric instrumentation | High | View-through + core video metrics tracked | Partial tracking | View-through not tracked |
| YT-14 | Attribution model | High | Data-driven attribution; not judged on last-click | Last-click used as primary | No conversion attribution |
| YT-15 / G-CTV1 | CTV measurement | High | CTV uses Google Ads conversion tracking / GA4 (NOT Floodlight) | CTV active, measurement unverified | CTV relying on Floodlight (won't capture conversions) |

## Deprecated (priors — confirm before stating as fact)

- **Video Action Campaigns** — reported fully deprecated ~April 2026, replaced by
  Demand Gen. Flag any remaining VAC (G-DG2).
- **Overlay ads** — discontinued (April 2023 prior).
- **Rule-based attribution** (first click, linear, time decay, position-based) — auto-
  upgraded to data-driven attribution.
- **DV360 lifetime frequency caps** — max period reportedly reduced to 30 days
  (Feb 2025 prior).
