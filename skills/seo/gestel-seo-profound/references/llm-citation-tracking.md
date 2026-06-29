<!-- Source: references/skills/claude-seo/extensions/profound/skills/seo-profound/SKILL.md + docs/PROFOUND-SETUP.md -->
<!-- Used by: gestel-seo-profound -->
<!-- Reference data. The provider feeds described here are a Boundary, not an assumed capability. -->

# LLM Citation-Tracking Playbook

Methodology for measuring and interpreting how often LLM assistants cite or
mention a brand. The continuous, dated, multi-platform version of this data is a
**commercial-provider** capability (Profound polls LLMs and publishes
time-series; SE Ranking and DataForSEO sample on demand). This file distills the
*interpretation method* so it works from a user-supplied export, a manual log, or
a one-shot sample — without assuming any provider, key, or live endpoint exists.

## 1. Metric definitions and formulas

Always state the **prompt set**, **platform**, and **window** alongside any rate;
a citation rate without them is uninterpretable.

- **Citation rate (per platform, per window)**
  `= answers mentioning/linking the brand ÷ total answers for the fixed prompt set`
  - "Mention" (brand named) and "citation" (brand linked/sourced) are different —
    track them separately if the data distinguishes them.

- **Share of Voice (SoV)**
  `= brand citations ÷ Σ citations across the tracked competitor set` (same prompts,
  same window). SoV depends entirely on which competitors are in the set — fix the
  set and version it.

- **Co-citation rate (brand X relative to you)**
  `= answers citing both you and X ÷ answers citing you`. High co-citation = X is
  your AI-era rival for that intent, even if it isn't a classic SEO competitor.

- **Win/loss by prompt**
  Per prompt: did the brand surface? If not, which brand(s) did. This is the
  actionable unit; the overall average hides which prompts to fix.

- **Trend delta**
  `WoW = rate(this week) − rate(last week)`; `MoM` analogously. Only valid if the
  prompt set and platform are identical across windows.

## 2. Sampling-noise floor (don't over-read small deltas)

LLM answers are stochastic; a small citation-rate change can be pure sampling
variance. Rough guidance for a binomial rate `p` over `n` prompts (or prompt×runs):

- Standard error `≈ sqrt(p·(1−p)/n)`. A delta smaller than ~2×SE is likely noise.
- Practical floors: with `n < 30` prompts, treat single-digit-point swings as
  noise. With `n ≥ 100`, ~3–4 point moves start to be meaningful.
- Increase `n` by (a) more prompts in the set or (b) multiple runs per prompt
  (LLMs vary run-to-run). Average across runs before computing a rate.
- If you cannot meet the floor, report the delta as **directional, not
  significant**, and say so.

## 3. Baseline-band alerting

Don't alert off the prior single point — alert off a band around a trailing mean:

- Baseline = trailing mean over a stable window (e.g. trailing 7 daily samples).
- Band = baseline ± k·(trailing standard deviation), k≈1.5–2.
- Flag a **drop/spike** only when the new value exits the band *and* the move
  clears the sampling-noise floor in §2.
- For every flagged move, attempt a cause and label it a hypothesis (see §6).
  Never assert a cause you can't evidence from the data or a dated external fact.

## 4. Prompt-set design (the foundation)

A citation rate is only as good as its prompt set. Build a fixed, versioned set
spanning the funnel; tag each prompt by **intent** and **funnel stage** so you can
read the rate by segment.

| Prompt type | Example shape | What it tests |
|---|---|---|
| Category / "best" | "best <category> tools for <use case>" | In the consideration set? |
| Problem / JTBD (unbranded) | "how do I <job the product does>" | Cited as a *solution*, not just by name |
| Comparison | "<brand> vs <competitor>", "alternatives to <X>" | Co-citation & positioning |
| Branded | "what is <brand>", "is <brand> good for <use case>" | Entity accuracy / how LLM describes you |
| Use-case / persona | "<category> for <industry/persona>" | Segment coverage |

Sizing rule of thumb: enough prompts per intent segment to clear the §2 floor for
that segment — commonly ≥10–20 prompts per segment, ≥50–100 total for stable
overall rates. Keep the set **frozen** across windows; changing it invalidates
trend deltas. Version it (v1, v2…) and never compare across versions as a trend.

## 5. Provider-free one-shot sampling procedure

When no export exists and the user agrees to a single sample:

1. Take the fixed prompt set from §4 (design it first if needed).
2. Run each prompt through the **single LLM available in this session**, or have
   the user paste responses from the assistants they care about. Optionally run
   each prompt 2–3× to dampen run-to-run variance.
3. For each prompt record: brand surfaced (y/n), prominence (cited/linked vs.
   mere mention vs. absent), competitors co-cited, and whether the brand
   description was accurate/current.
4. Compute citation rate overall and per intent segment, and a co-citation tally.
5. Label the entire result **"one sample at <date>, <model> — not a tracked
   time-series."** Do not draw a trend from one sample, and do not present it as
   what a continuous provider would report.

This yields a real, defensible snapshot and a prompt-level gap list without any
paid feed — the gap list is the actionable output even from `n=1` window.

## 6. Diagnosis → fix-lever mapping

| Observed pattern | Likely cause | Fix lever (route to owning skill) |
|---|---|---|
| Invisible on **unbranded category/problem** prompts | Not in LLM's solution corpus for that intent | Discovery/category content, comparison & listicle presence, citable assets → content/GEO skills |
| Cited on branded but **described inaccurately/stale** | Entity ambiguity / outdated public facts | Entity clarity, fresh canonical facts, schema, About/Wikipedia-class sources → GEO/site skills |
| A **competitor consistently co-cited** where you're absent | They own that intent's sources | Win those specific prompts: targeted content + co-citation sources |
| Cited but **never linked/sourced** | Mentioned, not used as a source | More extractable, quotable, self-contained passages → `gestel-blog-geo` |
| Strong on one platform, weak on another | Platform sources differ (e.g. Perplexity vs AI Overviews) | Platform-specific source presence; triangulate with the right provider |

## 7. Provider triangulation (all feeds are a Boundary unless user-supplied)

| Need | Provider | Status in this skill |
|---|---|---|
| Continuous time-series, ChatGPT+Perplexity depth, alerts | Profound (paid) | **Boundary** — needs user export or configured adapter |
| One-shot SoV across all platforms, keyword-gap | SE Ranking AI visibility (paid) | Route to adapter if configured |
| Google AI Overviews / AI Mode presence | DataForSEO AI tools (paid) | Route to adapter if configured |
| Page-level citability | (none — heuristic) | `gestel-blog-geo`, local-only |

The feeds are complementary, not redundant: trend tracking vs. single-shot SoV
vs. AI-Overviews coverage answer different questions. None is assumed connected.

## 8. Original routing (from source, attribution)

The upstream `seo-profound` extension exposed these provider commands. They are
recorded for provenance and are **not** invocable here without the paid key/API:

- `citations <brand>` — current citation rate per LLM + 30-day trend.
- `prompts <brand>` — top prompts that surface / fail to surface the brand.
- `competitors <brand>` — brands co-cited for the same prompts.
- `alerts <brand>` — spike/drop alerts vs. a 7-day baseline.

This skill reproduces the *analysis* each command implies (citation rate, prompt
win/loss, co-citation, baseline-band alerts) from supplied data, not the live
polling that produced it.
