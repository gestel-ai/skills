<!-- Updated: 2026-06-28 | v1.0 -->
<!-- Provenance: distilled from marketingskills/skills/ab-testing/references/sample-size-guide.md (commit 8bfcdffb655f16e713940cd04fb08891899c47db, MIT) -->
<!-- Used by: gestel-ads-intelligence -->

# Sample Size And Confidence Guide

Use this to decide whether an observed difference between imported Creative
Package variants is trustworthy, and to size the *next* test before GESTEL
recommends it. GESTEL does not run live platform experiments here — it reads
already-collected CSV/manual metrics and plans the next pack. So this guide has
two jobs:

1. **Read-back check** — given the impressions/clicks/conversions a variant
   already received, was the gap big enough to believe, or is it noise?
2. **Forward planning** — given a baseline rate and the lift you want to detect,
   how many impressions/clicks must the next variant accumulate before its
   result is callable?

## Required Inputs

1. **Baseline rate** — current CTR (hook signal) or CVR (post-click fit).
2. **Minimum detectable effect (MDE)** — smallest relative change worth acting
   on. Set from business impact and what past packs have realistically moved.
3. **Significance level** — usually 95% (less than 5% chance the gap is random).
4. **Power** — usually 80% (chance of catching a real effect of size MDE).

For static creatives the "denominator" depends on which signal you are judging:

- CTR / thumb-stop differences → use **impressions per variant**.
- CVR / CPA differences → use **clicks (or sessions) per variant**.

## Sample Size Quick Reference

Sample is **per variant**, at 95% confidence / 80% power.

### Baseline 1%

| Lift to detect | Per variant | Total (2 variants) |
| --- | --- | --- |
| 5% (1% → 1.05%) | 1,500,000 | 3,000,000 |
| 10% (1% → 1.1%) | 380,000 | 760,000 |
| 20% (1% → 1.2%) | 97,000 | 194,000 |
| 50% (1% → 1.5%) | 16,000 | 32,000 |
| 100% (1% → 2%) | 4,200 | 8,400 |

### Baseline 3%

| Lift to detect | Per variant | Total |
| --- | --- | --- |
| 5% | 480,000 | 960,000 |
| 10% | 120,000 | 240,000 |
| 20% | 31,000 | 62,000 |
| 50% | 5,200 | 10,400 |
| 100% | 1,400 | 2,800 |

### Baseline 5%

| Lift to detect | Per variant | Total |
| --- | --- | --- |
| 5% | 280,000 | 560,000 |
| 10% | 72,000 | 144,000 |
| 20% | 18,000 | 36,000 |
| 50% | 3,100 | 6,200 |
| 100% | 810 | 1,620 |

### Baseline 10%

| Lift to detect | Per variant | Total |
| --- | --- | --- |
| 5% | 130,000 | 260,000 |
| 10% | 34,000 | 68,000 |
| 20% | 8,700 | 17,400 |
| 50% | 1,500 | 3,000 |
| 100% | 400 | 800 |

### Baseline 20%

| Lift to detect | Per variant | Total |
| --- | --- | --- |
| 5% | 60,000 | 120,000 |
| 10% | 16,000 | 32,000 |
| 20% | 4,000 | 8,000 |
| 50% | 700 | 1,400 |
| 100% | 200 | 400 |

If you need an exact figure, the closed form is
`n = (1.96 + 0.84)^2 × 2 × p × (1 − p) / (p × MDE_relative)^2`
where `p` is the baseline rate.

## Reading Back An Already-Collected Result

When the CSV is already in hand, do not compute a fresh test — instead compare
what each variant *received* against the table:

- Find the row for the winner's baseline rate and the relative gap you observed.
- If both variants exceeded the "per variant" cell for that gap → the
  difference is likely real. Label the winner.
- If either variant is below it → the difference is **directional only**. Say so
  in the confidence note and recommend re-running the next pack to accumulate
  more volume before retiring the loser.

## Duration / Volume Planning For The Next Pack

```text
Required impressions = sample-per-variant × number of variants
Days needed          = required impressions / (daily impressions per variant × % of delivery exposed)
```

Minimum runtime regardless of math:

- **1 full week** to absorb day-of-week variation.
- Span at least one pay-cycle boundary for e-commerce product photos.

Maximum: avoid 4–8 weeks-plus on one pack — novelty fades, frequency rises, and
other packs are starved. Re-pack instead.

## Multiple Variants

| Variants | Sample multiplier |
| --- | --- |
| 2 (A/B) | 1× |
| 3 | ~1.5× |
| 4 | ~2× |
| 5+ | Cut the field; comparisons multiply false positives |

## When You Can Never Reach The Sample

Common for low-spend GESTEL accounts. Options, in order of preference:

1. Raise the MDE — only claim large effects (≥20–50% lift).
2. Combine similar product packs to pool volume.
3. Judge an upstream signal with more events (CTR before CVR).
4. Decide qualitatively from Review-Gate and pattern evidence, and **say the
   call is qualitative** in the confidence note.
5. Run the pack longer — accept slower learning, not false certainty.

Dropping to 90% confidence is a last resort; if used, flag it explicitly.

## Common Mistakes

- Calling a winner before either variant clears the sample cell ("peeking").
- Using a site-wide average instead of the specific pack's baseline rate.
- Comparing variants whose date ranges or spend differ — normalize or flag.
- Splitting volume across too many variants at once.
- Reporting a CTR winner as a *conversion* winner — different denominators.

## Quick Decision Frame

```text
Daily impressions per variant: _____
Baseline rate (CTR or CVR):    _____
MDE I care about:              _____
Sample needed per variant:     _____   (from tables)
Days to reach it:              sample / daily-per-variant = _____

> 60 days  → pick an alternative above
30–60 days → only for high-impact packs
< 14 days  → feasible
< 7 days   → run a full week anyway
```
