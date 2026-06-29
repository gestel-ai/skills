# Microsoft / Bing Ads Benchmarks

<!-- GESTEL local copy. Self-contained; no runtime dependency on the top-level references/ tree. -->
<!-- Extracted from the multi-platform benchmarks source; Microsoft section only. -->
<!-- FRESHNESS: every number here is a SNAPSHOT as of the source date (≈2026-04 to 2026-05). Treat as orientation, NOT current truth. Do not state any figure as the present-day benchmark without user-provided dated research or a live lookup. The user's own account numbers always override these. -->

## Core Performance (snapshot)

| Metric | Value | vs Google |
| --- | --- | --- |
| Average CPC | $1.20-$1.55 | 20-35% discount |
| Average CTR (search) | 2.83-3.1% | Higher than Google ~2.0% |
| Users click paid ads | 25% more often | vs Google users |
| Higher ROAS reported | 37% of advertisers | vs Google |

## Audit Thresholds (used by the 24-check framework)

These cut points drive the PASS / WARNING / FAIL bands in `microsoft-audit.md`.
The *bands* are the durable part; the absolute dollar/percent values are a
snapshot and should be re-grounded against the user's account.

| Metric | Pass | Warning | Fail |
| --- | --- | --- | --- |
| CTR (search) | ≥2.83% | 1.5-2.83% | <1.5% |
| CPC (search) | ≤$1.55 | $1.55-2.50 | >$2.50 |
| CPC vs Google | 20-40% lower | 10-20% lower | Same or higher |
| CVR vs Google | within 20% | 20-50% lower | >50% lower |
| Impression share (brand) | ≥80% | 60-80% | <60% |
| RSA assets | ≥8 headlines, ≥3 descriptions | 3-7 headlines / 2 descriptions | <3 headlines |
| Budget vs Google | 20-30% of Google spend | slightly over/under | >50% of Google budget |

## LinkedIn Profile Targeting & Copilot (snapshot — treat as unverified claims)

| Metric | Value (snapshot) |
| --- | --- |
| LinkedIn Profile Targeting CTR | ~16% greater than standard |
| LinkedIn Profile Targeting CVR | ~64% greater than standard |
| CPCs vs buying on LinkedIn Ads directly | ~30-70% cheaper |
| Copilot placement CTR | ~73% higher than traditional search |
| Copilot placement CVR | ~16% stronger than traditional search |

These lift figures are the most freshness-sensitive items in this file. Use them
only to motivate *evaluating* a lever (e.g. "is LinkedIn targeting enabled on B2B
campaigns?"), never as a promised outcome.

## Audience Demographics (directional, stable-ish)

- Skews affluent (~half in top-25% household income brackets).
- More educated than average (sizable share with degrees).
- Older age skew (35-65+ over-indexed).
- Desktop- and enterprise-heavy (Windows/Edge/Office ecosystem).

Treat demographic skew as a directional pattern for copy/landing-page guidance
(MS13), not a precise current statistic.
