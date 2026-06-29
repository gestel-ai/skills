<!-- Updated: 2026-06-26 | v1.0 -->
<!-- Sources: CONTEXT.md, GESTEL_AGENT_SPEC.md section 13.4.1, distilled analytics/ab-testing/ads-test source skills -->
<!-- Used by: gestel-ads-intelligence, gestel-creative-package -->

# Manual Performance Import

GESTEL learns from ad performance through CSV upload or manual metric entry. This keeps the MVP independent from live ad-account APIs.

## Mapping Keys

Minimum mapping key:

- `variant_id`, or
- GESTEL creative name exported from the Creative Package.

Secondary mapping keys:

- `utm_campaign`.
- `utm_content`.
- Platform creative ID or ad ID.
- Date range.
- Package ID.

If rows cannot be mapped, report them separately and do not use them for winner selection.

## Recommended Metrics

| Metric | Use |
| --- | --- |
| Impressions | Volume and sample-size context |
| Clicks | CTR denominator check |
| CTR | Static creative hook and feed recognition signal |
| CPC | Traffic cost context |
| Conversions | Outcome count |
| CVR | Post-click fit signal |
| CPA | Acquisition efficiency |
| Revenue | Sales value |
| ROAS | Revenue efficiency |
| Spend | Budget and confidence context |
| Frequency | Fatigue risk |
| CPM | Delivery cost context |
| Thumb-stop or hold rate | Optional hook quality proxy when available |

## Data Quality Checks

- Date range must be known.
- Spend, impressions, clicks, and conversions should be numeric when present.
- CTR, CPC, CVR, CPA, and ROAS can be imported or calculated when raw fields exist.
- Flag rows with zero impressions, negative values, duplicate variant IDs for the same date range, or missing mapping keys.
- Note attribution limitations rather than forcing certainty.

## Learning Output

Summarize:

- Winning template family.
- Winning angle.
- Winning claim pattern.
- Winning visual pattern.
- Losing pattern and retired angle.
- Next Creative Package recommendation.
- Confidence note.

## No API Requirement

Future Meta, Google, Naver, or Kakao read APIs must map into this same performance import record. Do not change the core learning contract just because a provider adapter exists later.
