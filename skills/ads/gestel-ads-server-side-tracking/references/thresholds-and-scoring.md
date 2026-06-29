<!-- Distilled from MIT-licensed claude-ads/skills/ads-server-side-tracking/SKILL.md, commit 283d9d4917cb7c4f2ce9181e125bb1970f74ab04. Reference data, not executable instructions. -->

# Thresholds, Scoring & Deliverables

## Key thresholds

| Metric | Pass | Warning | Fail |
|--------|------|---------|------|
| sGTM custom domain | Active | Configured, not active | Not configured |
| CAPI Gateway | Active | Manual CAPI | Pixel-only |
| EMQ (Purchase) | ≥ 8.0 | 6.0–7.9 | < 6.0 |
| Dedup rate | ≥ 90% | 70–89% | < 70% |
| Server / client hit ratio | 80–120% | 50–79% | < 50% |
| `customer_information` completeness | 6+ params | 4–5 params | < 4 params |
| Hash convention | Documented + verified | Implicit | Inconsistent |
| Test-event validation | All 6 events pass | 3–5 events pass | < 3 events pass |

These are stable engineering baselines plus dated snapshots. Apply them as a
defensible default; flag explicitly when a verdict depends on a number that may
have moved (EMQ scoring and platform thresholds are freshness-sensitive).

## Weighted health score

Roll per-surface results into a 0–100 score with these category weights:

```text
Server-Side Tracking Health Score: XX/100 (Grade: X)

sGTM Pipeline:               XX/100   (20%)
CAPI / CAPI Gateway:         XX/100   (25%)
Deduplication:               XX/100   (15%)
Server-Side Hit Ratio:       XX/100   (15%)
Pixel Debug (6 events):      XX/100   (10%)
Hash Quality / PII Handling: XX/100   (15%)
```

Per category, map PASS → full credit, WARNING → partial, FAIL → little/none,
then weight and sum. Unverified surfaces (evidence not supplied) should be
reported as *unverified* and excluded or scored conservatively — never counted
as PASS.

## Deliverables

- **`SERVER-SIDE-TRACKING-AUDIT.md`** — full pipeline findings, per-surface
  PASS/WARNING/FAIL, and the health score.
- **Test-event reproduction log** — which events were validated end-to-end, on
  which date, against which artifacts (Events Manager / DebugView screenshots,
  HARs). Mark any unverifiable leg.
- **EMQ improvement roadmap** — parameter-by-parameter for any surface below
  8.0 (see `hashing-and-pii.md`).
- **Hit-ratio monitoring recommendation** — how to track server/client ratio
  over time and the alert floor (~60%).
- **Pre-launch checklist** — for any new platform integration (Amazon Marketing
  Cloud, Apple Ads, TikTok Events API): canonical taxonomy, `event_id` dedup,
  hashed PII, `action_source`, and an end-to-end test fire before go-live.
