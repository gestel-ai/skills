<!-- Used by: gestel-seo-unlighthouse -->
<!-- Distilled domain methodology. The upstream source's references/ folder was empty;
     this file exists so the skill is self-contained if the top-level references/ tree is removed. -->

# Site-wide Lighthouse / Core Web Vitals methodology

Reference for interpreting a **multi-page lab audit** (the kind Unlighthouse produces). This
document is methodology only — it does not run anything. See the parent SKILL.md Boundaries:
the crawl + Lighthouse run depends on missing upstream scripts and is out of scope here.

## 1. What a multi-page audit actually is

Unlighthouse (MIT) discovers a site's routes from `sitemap.xml` plus an internal-link crawl,
runs Lighthouse on each route, and aggregates the results into an interactive HTML report and a
machine-readable `ci-result.json`. Key behaviors to remember when reading its output:

- It **samples by route pattern**. By default it groups similar paths and audits a
  representative sample rather than every near-identical URL, so a `/blog/*` score may stand in
  for hundreds of posts.
- Scores are **lab data**: one synthetic Lighthouse run per route, under throttling. Not real
  users.
- Default form factor is **mobile** with simulated throttling (≈4× CPU slowdown, slow-4G). This
  matches Google's mobile-first indexing. Desktop is an optional second pass.
- The aggregate `score.performance` / `score.accessibility` / `score.bestPractices` / `score.seo`
  are **medians across audited routes**; per-route detail lives in `ci-result.json`.

When to reach for this instead of single-URL PageSpeed Insights:

- Large sites where PSI's free field quota (25k queries/day) won't cover every URL.
- Offline / CI / restricted environments needing repeatable lab measurement.
- Post-deploy site-wide regression checks.

## 2. Lab vs field — get this right first

| | Lab (Lighthouse / Unlighthouse) | Field (CrUX / PSI field) |
|---|---|---|
| Source | one synthetic, throttled run | real users, 28-day rolling p75 |
| Metrics | FCP, Speed Index, LCP, **TBT**, CLS (+ TTI) | LCP, **INP**, CLS, TTFB, FCP |
| Responsiveness | approximated by **TBT** | measured directly by **INP** |
| Use | debugging, regression detection, pre-launch | the actual ranking/UX signal |
| Ranking signal? | **No** | **Yes** (Google uses field CWV) |

Rules:

- Never claim a Google ranking impact from lab numbers. Confirm in field (CrUX) first — route to
  the `seo-google` PSI/CrUX skill for that.
- A clean lab **TBT** does not guarantee a good field **INP**; INP captures real interactions
  (clicks, taps, keypresses) that a single lab load never exercises.
- A single lab run is noisy. If only one run is available, say so; trends across runs/deploys are
  more trustworthy than any single score.

## 3. Core Web Vitals thresholds

| Metric | Good | Needs improvement | Poor | Notes |
|---|---|---|---|---|
| **LCP** | ≤ 2.5 s | 2.5–4.0 s | > 4.0 s | largest above-the-fold element paint |
| **INP** | ≤ 200 ms | 200–500 ms | > 500 ms | field only; replaced FID March 2024 |
| **CLS** | ≤ 0.1 | 0.1–0.25 | > 0.25 | unitless; layout instability |
| **FCP** (lab/field support) | ≤ 1.8 s | 1.8–3.0 s | > 3.0 s | first content paint |
| **TBT** (lab) | ≤ 200 ms | 200–600 ms | > 600 ms | lab proxy for responsiveness |
| **Speed Index** (lab) | ≤ 3.4 s | 3.4–5.8 s | > 5.8 s | visual completeness |

Field metrics are reported at the **75th percentile** of real users — a page passes a metric
only when p75 is in the "good" band.

## 4. Lighthouse Performance score weighting (v10 / v11)

The Performance score (0–100) is a weighted blend of five lab metrics:

| Metric | Weight |
|---|---|
| **TBT** | 30% |
| **LCP** | 25% |
| **CLS** | 25% |
| **FCP** | 10% |
| **Speed Index** | 10% |

Implications:

- TBT + LCP + CLS = **80%** of the score. Fix those three before touching FCP/SI.
- Score bands (apply to every category): **90–100 green** (good), **50–89 orange** (needs
  improvement), **0–49 red** (poor).
- The score is non-linear: moving from 40→50 is far easier than 90→95. Prioritize lifting red
  pages out of red, not polishing green pages.

## 5. LCP-subpart decomposition (slow-LCP diagnosis)

LCP is the sum of four consecutive phases. Find the dominant one, fix that:

| Phase | What it is | Healthy share | Typical fix |
|---|---|---|---|
| 1. **TTFB** | server + network to first byte | ≤ ~40% of LCP | caching, CDN, faster backend, edge rendering |
| 2. **Resource load delay** | gap before the LCP image starts loading | < ~10% | `preload` / `fetchpriority="high"`, avoid JS-injected or CSS-`background-image` LCP, put it in initial HTML |
| 3. **Resource load time** | downloading the LCP image | ≤ ~40% | compress, modern format (AVIF/WebP), responsive `srcset`, right dimensions |
| 4. **Element render delay** | loaded → painted | < ~10% | remove render-blocking CSS/JS, reduce hydration wait, inline critical CSS |

Most real LCP problems concentrate in **TTFB** (phase 1) and **render delay** (phase 4). A large
**load delay** almost always means the LCP element is discovered late by the browser.

## 6. Route-pattern triage (prioritization)

A site-wide audit is a *pattern* problem, not a list of URLs.

1. **Bucket** audited routes by template: home, `/blog/*`, `/product/*`, category, landing, etc.
2. **Pick the worst representative** per bucket (lowest category score / worst metric).
3. **Weight** each finding: `severity_band × number_of_URLs_the_pattern_covers × inverse_effort`.
   A template-level fix (one change, thousands of pages) almost always outranks a one-off page fix.
4. **Fix the template once**, then re-audit the representative to confirm the lift before
   declaring the pattern fixed.

## 7. Per-category audit checklists

### Performance

- Which of TBT / LCP / CLS is dragging the score (use the §4 weights).
- Render-blocking CSS/JS in the critical path.
- Hero/LCP image: preloaded? right size/format? `fetchpriority`?
- JS bundle size and main-thread work (drives TBT).
- Lazy-load below-the-fold images and offscreen iframes.

### Accessibility

- Color contrast ≥ 4.5:1 (normal text) / 3:1 (large text).
- Every meaningful image has `alt`; decorative images `alt=""`.
- Form controls have labels; interactive elements are reachable/named.
- Logical heading order (one `h1`, no skipped levels); valid ARIA.

### Best Practices

- HTTPS everywhere, no mixed content.
- No browser console errors.
- No deprecated/insecure APIs.
- Images served at correct aspect ratio and resolution.

### SEO

- Unique, present `<title>` and meta `description` per page.
- `<meta name="viewport">` present.
- Links are crawlable (`<a href>`, not JS-only).
- `robots`/`robots.txt` not blocking indexable pages.
- Canonical correct; `hreflang` correct for multilingual; structured data valid
  (for schema work route to `gestel-blog-schema`).

## 8. Reading `ci-result.json`

- Top-level aggregate: `score.performance`, `score.accessibility`, `score.bestPractices`,
  `score.seo` — medians across audited routes.
- Per-route array: each route carries its own four scores plus the underlying metric values
  (LCP, TBT, CLS, FCP, …). Use these to build the per-pattern table and to find the worst pages.
- When you only have screenshots or pasted numbers, reconstruct the same structure manually:
  per-pattern median scores + the worst representative's failing metrics.
