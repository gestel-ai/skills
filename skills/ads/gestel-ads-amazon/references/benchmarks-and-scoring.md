<!-- Used by: gestel-ads-amazon -->
<!-- Distilled from claude-ads/skills/ads-amazon/SKILL.md (MIT, commit 283d9d49) -->
<!-- Thresholds are a dated snapshot. Treat as heuristics, not verified live
     platform facts — gate freshness-sensitive numbers per SKILL Boundaries. -->

# Amazon Ads — Thresholds & Health Score

## Pass / Warning / Fail thresholds

| Metric | Pass | Warning | Fail |
|--------|------|---------|------|
| ACOS (vs margin-derived target) | Within ±10% of target | 10–25% over | >25% over |
| TACOS trend (90d) | Decreasing | Flat | Increasing |
| Auto / Manual mix | Both active per ASIN | Only Manual or only Auto | Single campaign / ASIN |
| Negative keywords on Auto | Manual ASIN keywords added | Some missing | None |
| Search-term harvest cadence | Weekly | Monthly | Ad-hoc |
| Branded campaign ACOS | <5% | 5–15% | >15% |
| Dynamic bidding strategy | Up-and-Down on converters, Down-Only on learners | Mixed inconsistently | All campaigns same strategy |
| Sponsored Brands video tested | Active on top 10 ASINs | Active on 1–3 ASINs | Not tested |
| Brand Analytics accessed | Weekly | Monthly | Never |

These cutoffs are a starting rubric. The ACOS row is only meaningful once a
contribution margin (or explicit target ACOS) is supplied; without it, report
the ASIN as "directional only."

## Category weights

| Category | Weight |
|----------|--------|
| Campaign Structure & Portfolios | 15% |
| Search-Term Harvesting & Negatives | 25% |
| ACOS / TACOS Discipline | 20% |
| Bid & Budget Management | 15% |
| Sponsored Brands | 10% |
| Sponsored Display | 10% |
| Brand Analytics & Reporting | 5% |

## Health score (0–100)

1. Score each category 0–100 from its checklist in `amazon-ads-framework.md`
   (share of checks at Pass, with Warning ≈ half credit, Fail ≈ 0).
2. Weight each category score by the table above and sum to a 0–100 total.
3. Assign a grade band (A ≥ 90, B 80–89, C 70–79, D 60–69, F < 60). Bands are a
   presentation convenience, not a platform standard.

### Report block

```text
Amazon Ads Health Score: XX/100 (Grade: X)

Campaign Structure:      XX/100  ████████░░  (15%)
Search-Term Harvesting:  XX/100  ██████████  (25%)
ACOS / TACOS Discipline: XX/100  █████████░  (20%)
Bid & Budget Mgmt:       XX/100  ████████░░  (15%)
Sponsored Brands:        XX/100  ███████░░░  (10%)
Sponsored Display:       XX/100  ███████░░░  (10%)
Brand Analytics:         XX/100  █████░░░░░  (5%)
```

Always attach: the data window each category was scored on, which categories had
insufficient data (scored conservatively rather than asserted), and any
freshness limit on the underlying thresholds.
