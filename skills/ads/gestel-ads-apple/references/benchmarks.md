<!-- Used by: gestel-ads-apple -->
<!-- Distilled from claude-ads/skills/ads-apple/SKILL.md (commit 283d9d4917cb7c4f2ce9181e125bb1970f74ab04, MIT). Attribution only — not a runtime dependency. -->

# Apple Ads Benchmarks & Platform-Change Snapshot

> **FRESHNESS WARNING.** Everything in this file is a **dated snapshot** carried
> over from the source skill (Apple Ads methodology, last source update April
> 2026). Apple Ads renames products, retires bid types, and shifts auction
> mechanics often. Treat every number, date, and "rolling out" claim below as a
> **starting hypothesis to verify**, not a current fact. Before stating any of
> these as live, confirm with user-provided dated research or a live lookup, and
> label the snapshot date when you cite it. See the Boundaries section of
> `SKILL.md`.

## Category benchmarks (2025–2026 snapshot)

| Category | Avg CPT | Avg TTR | Avg Install CVR | Target CPI |
|----------|---------|---------|-----------------|------------|
| Games | $0.50–$1.00 | 3–5% | 55–70% | $1.00–$3.00 |
| Health & Fitness | $1.50–$3.00 | 2–4% | 45–60% | $3.00–$8.00 |
| Productivity | $1.00–$2.50 | 2–3.5% | 50–65% | $2.00–$5.00 |
| Finance | $2.00–$5.00 | 1.5–3% | 40–55% | $5.00–$15.00 |
| Education | $1.00–$2.00 | 2–4% | 50–65% | $2.00–$6.00 |
| Shopping | $0.80–$2.00 | 2.5–4% | 45–60% | $2.00–$5.00 |
| Lifestyle | $0.80–$1.80 | 2–3.5% | 45–60% | $2.00–$5.00 |

## Country / region tiers (snapshot)

- **Tier 1** (US, UK, AU, CA, JP): CPT 2–3× above global average; highest LTV.
- **Tier 2** (DE, FR, KR, SG, HK): CPT 1–1.5× above global average.
- **Tier 3** (BR, IN, MX): CPT 30–60% below Tier 1; high volume, lower LTV.
- US is the highest-cost market; AMEI (Africa / Middle East / India) is the most
  cost-efficient and stable.
- International markets often deliver **3–5× better CPI** than the US with
  comparable LTV for subscription apps — a recurring optimization lever.

## Overall Search Results averages (2025 SplitMetrics snapshot)

| Metric | Search Results Average |
|--------|------------------------|
| TTR (Tap-Through Rate) | 9.7% |
| Conversion Rate | 66.2% |
| CPT (Cost Per Tap) | $2.25 |
| CPA (Cost Per Acquisition) | $3.76 |

## Placement types (TAP coverage) and benchmark CPT

| Placement | Where | Best for | Benchmark CPT |
|-----------|-------|----------|---------------|
| Search Results | Below search results | High intent, bottom funnel | $0.50–$3.00 |
| Search Tab | Top of Search tab | Discovery, mid funnel | $0.30–$1.50 |
| Today Tab | App Store home | Brand awareness | $1.00–$5.00 |
| Product Pages | Competitor / related app pages | Competitor conquesting | $0.50–$2.00 |

Placement TTR benchmarks: **>2.5%** for Search Results, **>1.5%** for Search Tab.
Tap→install conversion: **50–65%** for brand terms, **20–40%** for category terms.

## Platform-change snapshot (verify before asserting as current)

These are the source's freshness-sensitive claims. They are the *most* likely to
be stale. Do not present any of them as current without dated confirmation.

- **Rebrand:** "Apple Search Ads" renamed to **"Apple Ads"** (source: April 2025).
- **Maximize Conversions** auto-bidder: source says GA **February 26, 2026**.
  AI bidder using Search Match; sets per-query bids in real time. **Target CPA**
  (weekly-average target) replaces the deprecated **CPA Cap**. Recommended daily
  budget ≥ **5× target CPA**; two-week minimum learning period. Stated limitation:
  optimizes for **installs only**, not post-install events (no trial /
  subscription / ROAS optimization).
- **Creative Sets fully deprecated** — CPPs are the sole ad-variation mechanism.
  **CPP limit doubled to 70 per app** (source: October 2025).
- **AdAttributionKit dual attribution** (source: April 10, 2025): Apple Ads
  registered with AdAttributionKit (SKAN v1–3), so installs report through BOTH
  SKAN/AAK postbacks AND the AdServices API for the first time.
- **WWDC 2025 (session 221):** configurable attribution windows, overlapping
  re-engagement windows, attribution cooldowns, country codes in postbacks.
  Overlapping conversions need iOS 18.4+ and
  `EligibleForAdAttributionKitOverlappingConversions=YES` in `Info.plist`.
- **Deep links in CPPs** available on iOS/iPadOS 18+ (re-engagement testing).
- **Organic keywords assignable to CPPs** (source: WWDC 2025), bridging
  paid/organic optimization.
- **Multiple ads per query** (ID ASA-MA1, severity Medium): source says rolling
  out **March 2026** — up to 2 ads per search query (was 1). Changes competitive
  dynamics; re-evaluate bid strategy for increased competition.
- **Personalized Ads / privacy:** source cites Apple Q1 2022 internal data that
  **78% of App Store search volume** comes from devices with Personalized Ads
  off, and that opted-in vs opted-out conversion is nearly identical (62.1% vs
  62.5%). Implication carried forward: prefer **creative-based targeting**
  (CPP↔keyword-theme alignment) over demographic audience filters.

## Source citations (as given by the source skill — verify independently)

- CPP conversion lift (~8% games, ~6.6% non-gaming) and SoundCloud case study
  (58% CR increase, 39% CPI reduction): AppTweak CPP guide / case study.
- Personalized-Ads opt-out figure: 9to5Mac on iOS 15 ATT data, citing Apple Q1
  2022 internal data.
- AdAttributionKit / WWDC25 session 221: Apple Developer video + Singular recap.
- Search Results averages: SplitMetrics 2025.
