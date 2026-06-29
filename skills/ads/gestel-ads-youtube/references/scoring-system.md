<!-- Updated: 2026-06-28 | v1.0 -->
<!-- Used by: gestel-ads-youtube -->

# YouTube Health Score — Scoring System

Self-contained scoring method for gestel-ads-youtube. No dependency on the top-level
`references/` tree.

## Weighted Scoring Algorithm

```text
S_total = Σ(C × W_sev × W_cat) / Σ(W_sev × W_cat over applicable checks) × 100
```

- `C` = result coefficient: **PASS 1.0**, **WARNING 0.5**, **FAIL 0**.
- `W_sev` = severity multiplier of the individual check.
- `W_cat` = category weight (below).
- **N/A** checks are dropped from BOTH numerator and denominator — never scored as fail.
- Result: a 0–100 Health Score.

## Severity Multipliers

| Severity | Multiplier | Criteria |
| --- | --- | --- |
| Critical | 5.0 | Immediate revenue/data loss risk. Remediation urgent. |
| High | 3.0 | Significant performance drag. Fix within ~7 days. |
| Medium | 1.5 | Optimization opportunity. Fix within ~30 days. |
| Low | 0.5 | Best practice, minor impact. Nice to have. |

## Per-Check Points

| Result | Points earned |
| --- | --- |
| PASS | Full severity × category weight |
| WARNING | 50% of full points |
| FAIL | 0 points |
| N/A | Excluded from total possible |

## Category Weights (YouTube)

| Category | Weight | Rationale |
| --- | --- | --- |
| Creative Quality | 30% | Skip-heavy surface; the first 5s and ABCD drive performance |
| Campaign Setup | 25% | Format fit, Demand Gen migration, multi-format, CTV setup |
| Audience Targeting | 25% | Targeting mix, prospect/retarget split, frequency strategy |
| Measurement | 20% | View-through, DDA, Brand Lift, CTV/Floodlight gap |

Per-check severities live in [youtube-audit.md](youtube-audit.md).

## Grading Thresholds

| Grade | Score | Label | Action |
| --- | --- | --- | --- |
| A | 90–100 | Excellent | Minor optimizations only |
| B | 75–89 | Good | Some improvement opportunities |
| C | 60–74 | Needs Improvement | Notable issues need attention |
| D | 40–59 | Poor | Significant problems present |
| F | <40 | Critical | Urgent intervention required |

## Quick Wins Logic

```text
IF severity in {Critical, High} AND estimated_remediation_time < 15 minutes
THEN flag as "Quick Win"
SORT Quick Wins by (severity × estimated_impact) DESC
```
