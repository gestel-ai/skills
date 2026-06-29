<!-- Updated: 2026-06-28 | v1.0 -->
<!-- Provenance: distilled from marketingskills/skills/ab-testing/references/test-templates.md and claude-ads/skills/ads-test/SKILL.md (MIT) -->
<!-- Used by: gestel-ads-intelligence -->

# Creative Test And Learning Templates

Templates for turning imported static-ad performance into a documented learning
loop and a next-pack test plan. These are output shapes for GESTEL — they never
publish, pause, or mutate a live campaign; they produce the brief for the next
Creative Package.

## Hypothesis Shapes

Use either form; both isolate a single conceptual change.

```text
Because [observed pattern from mapped variants],
we believe [next template family / angle / slot change]
will improve [primary metric: CTR / CVR / ROAS]
for [audience or placement],
while monitoring [guardrail metric: frequency / CPA].
```

```text
IF we [change one variable: template family / claim pattern / visual treatment]
THEN [metric] will [increase/decrease] by [estimated %]
BECAUSE [reasoning grounded in the imported data or Review-Gate evidence].
```

### Hypothesis Quality Checklist

- [ ] Single conceptual variable (not a color tweak plus a headline tweak).
- [ ] Specific metric named (not "performance").
- [ ] Estimated effect size stated — needed to size the next test.
- [ ] Baseline pulled from the mapped variant, not a site-wide average.
- [ ] Win / loss / inconclusive criteria written before the pack ships.

## Next-Pack Test Brief

```markdown
## Creative Package Test: [name]

### Hypothesis
[Because… / IF…THEN…BECAUSE… form above]

### Design
| Element | Value |
| --- | --- |
| Variable changed | [template family / angle / claim / visual / CTA] |
| Control | [current winning or baseline variant_id] |
| Variant(s) | [proposed pack item(s)] |
| Primary metric | [CTR / CVR / CPA / ROAS] |
| Guardrail | [frequency, CPA, Review-Gate status] |
| Diversity check | [Entity-ID cluster score target ≥8/10] |

### Required Volume
| Metric | Value |
| --- | --- |
| Baseline rate | [X%] |
| MDE | [X%] |
| Sample per variant | [N — from sample-size-guide.md] |
| Est. impressions/day per variant | [N] |
| Est. days to call | [N], minimum 7 |

### Success Criteria
- Winner: [primary metric] improves by [X%]+ and clears the sample cell.
- Guardrail: frequency stays below threshold; no new Review-Gate failure.
- Inconclusive: re-pack or pool volume; do not retire the loser yet.
```

## Learning / Results Record

```markdown
## Creative Learning: [date range]

### Import summary
- Rows imported / mapped / unmapped: [a / b / c]
- Date range, spend coverage, attribution caveats: [...]

### Winner vs loser (by variant_id)
| variant_id | template family | angle | claim | visual | impr | CTR | CVR | CPA | ROAS | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Patterns
- Winning template family: [...]
- Winning angle / claim / visual: [...]
- Retired or risky pattern: [...]
- Possible Review-Gate explanation for losers: [...]

### Why we think this happened
[Plain-language reasoning. Note attribution and sample-size limits.]

### Next pack
[Reference the Next-Pack Test Brief above.]
```

## Winning-Pattern Playbook Entry

When a pattern wins with adequate volume, record it so the insight compounds:

```markdown
| Pattern | Evidence (variant_ids, lift, confidence) | Apply to | Status |
| --- | --- | --- | --- |
| Social-proof badge near CTA lifts CTR | v_104 vs v_101, +18%, real | all product packs | promoted |
| Problem-led headline beats feature-led | v_207 vs v_203, +12%, directional | skincare line | re-test |
```

## Hypothesis Bank

Keep a backlog so the next import always has a test queued:

```markdown
| ID | Observation | Hypothesis (one line) | Est. impact | Status |
| --- | --- | --- | --- | --- |
| H1 | Static feed CTR flat across pack | New template family > color swaps | High | next |
| H2 | Frequency rising, CTR falling | Fresh visual treatment resets fatigue | Med | backlog |
```

## Prioritization Scorecard (ICE)

Score each candidate next-pack idea 1–10 on each axis; run highest first.

| Idea | Impact | Confidence | Ease | ICE = avg |
| --- | --- | --- | --- | --- |
| [A] | | | | |
| [B] | | | | |

- **Impact** — how much it could move the primary metric.
- **Confidence** — how strongly the imported data supports it (not gut).
- **Ease** — how fast a compliant pack can be produced and measured.
