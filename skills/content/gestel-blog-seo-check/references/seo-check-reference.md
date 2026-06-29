<!-- Used by: gestel-blog-seo-check -->
<!-- Distilled from claude-blog/skills/blog-seo-check/SKILL.md (commit 49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25, MIT) -->

# Blog SEO Check — Threshold Reference

This file holds the **numeric thresholds and rationale** behind the SKILL.md
checklist. Every value here is a **dated default that may be stale**, not current
ground truth. SERP rendering, social-card specs, crawler policies, and truncation
behavior change without notice. Use these as starting points, label them as dated
when you apply them, and tell the user that confirming current behavior requires
their own date-stamped research or a live lookup. Read the **Boundaries** section
of SKILL.md before relying on any number here.

## Freshness-sensitive (re-verify before asserting)

### Title tag

- **Default window:** ~40-60 characters. The real limit is a *pixel width* in the
  SERP, not a character count, and the cutoff has shifted across redesigns. 40-60
  chars is a safe historical proxy.
- Primary keyword in the first half; at least one power word; no critical meaning
  lost at the truncation point; specific, not generic.

### Meta description

- **Default window:** ~150-160 characters. Google has shown both shorter (~120) and
  longer (~300) snippets at different times and frequently rewrites descriptions
  entirely. Treat 150-160 as a conservative default, not a guarantee of display.
- One natural keyword instance, one concrete statistic, a benefit close, an implied
  action verb.

### og:image

- **Default spec:** at least 1200x630 px, ~1.91:1 aspect, absolute URL. Platform
  minimums and recommended ratios change; verify against the current platform docs
  if exact dimensions matter.

### Twitter / X Card

- **Default card type:** `summary_large_image` for blog posts.
- **Default field limits:** title under ~70 chars, description under ~200 chars.
  X has restructured card rendering multiple times; these limits are historical
  defaults. If the site has no X account, mark Twitter checks N/A.

### URL structure

- **Default path length:** under ~75 characters. This is an editorial/SEO heuristic,
  not an engine-enforced limit.
- Lowercase letters, numbers, hyphens only; keyword/variant in the slug; no date
  segments; minimal stop words; no `.html`/`.php` extension (clean URLs).

### External-link reachability and crawler policy

- Reachability requires an actual fetch — only verify if a live fetch is in scope;
  otherwise mark UNVERIFIED.
- Allowed AI/search crawler user-agents (e.g. GPTBot, ClaudeBot, PerplexityBot,
  Googlebot) and any robots/marketplace policy are platform-controlled and change;
  never assert current allow/deny state from memory.

## Editorial heuristics (semi-stable — guidance, not law)

- **Headings:** ~6-8 H2 sections for a standard post; ~60-70% of H2s phrased as
  questions; each heading under ~70 chars; primary keyword in 2-3 headings.
- **Internal links:** ~3-10 per post; ~5-10 per 2,000 words; spread across the post;
  descriptive anchors only.
- **Link anchors recorded per URL:** search engines have been observed to record only
  ~1-2 anchor texts per URL per page (dated finding) — the basis for the
  "link a given URL once in body content" dedup rule.
- **External links:** at least ~3 to authoritative sources; appropriate `rel` on
  sponsored/UGC; avoid needless competitor links.

## Stable method (safe to assert)

These do not depend on live platform behavior and can be checked with confidence:

- Exactly one H1; no skipped heading levels (H1 -> H2 -> H3).
- Descriptive anchor text — never "click here" / "read more".
- Canonical present, absolute, self-referencing, consistent trailing-slash.
- OG/Twitter tag *presence and internal consistency* (og:url matches canonical,
  og:type=article, og:title complements the title).
- Every content image has descriptive alt text; decorative images use empty alt.
- **FLOW evidence triple** for every public statistic: year anchor in prose before
  the stat + inline publisher-and-title citation + bottom source block with URL and
  `retrieved YYYY-MM-DD`. Drop or replace any statistic failing all three; never
  fabricate a source or retrieval date.
- Link deduplication: normalize URLs (strip trailing slash, query, fragment), keep
  the most descriptive anchor instance, exempt header/footer nav.

## Scoring and status

- Status vocabulary: **PASS / FAIL / WARN / N/A / UNVERIFIED**.
- Overall: count passes vs total applicable checks; label PASS / NEEDS WORK / FAIL.
- Link-dedup deduction: -1 point per duplicate URL in body content.
- Always separate UNVERIFIED checks (missing context) from FAIL checks (real issue).

## Converted-to-Boundary upstream feature

The source skill ended with an optional **"Live Performance Check (blog-google)"**
that called upstream `scripts/run.py` for a `google_auth` credential check and a
`pagespeed_check` PageSpeed/Lighthouse run, then appended CWV field data to the
report. That depends on hidden credentials, a paid/live provider, and upstream
runtime scripts that are not part of this self-contained skill. It is intentionally
**not** reproduced as a feature. If live performance / Core Web Vitals data is
wanted, treat it as a separately configured live-lookup adapter (out of scope here)
and continue the on-page audit without it.
