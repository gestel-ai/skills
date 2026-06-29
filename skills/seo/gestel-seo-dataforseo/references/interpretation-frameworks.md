<!-- Updated: 2026-06-28 | v1.0 -->
<!-- Used by: gestel-seo-dataforseo -->

# SEO Data Interpretation Frameworks

How to read each DataForSEO-shaped dataset once you have it (from a user export
or a provider adapter). These frameworks are provider-independent: they apply to
any SERP/keyword/backlink/on-page/GEO export with comparable columns, not only
to DataForSEO's exact schema.

## Organic SERP

Given rank + url + title + description + domain + SERP-feature flags:

- **Difficulty read from the page, not just a score.** Count how many of the top
  10 are high-authority domains, how many are exact-match-intent pages, and
  whether the result is dominated by aggregators/marketplaces. A "Medium"
  difficulty number means little if positions 1-8 are all DR90 incumbents.
- **SERP-feature surface.** Note featured snippet owner, AI-overview references,
  and People-Also-Ask questions. PAA questions are free H2/FAQ ideas; the
  snippet owner shows the format Google currently rewards (list, table, 40-60
  word paragraph).
- **Intent match.** If the ranking pages are guides but the user's page is a
  product page (or vice-versa), the gap is intent, not links. Recommend matching
  the dominant page type before chasing backlinks.

## Image SERP

Given position + title/alt + source page url + image url + domain:

- **Domain dominance:** rank the top 10 domains by number of image positions
  held. Concentrated dominance = hard to break in; fragmented = opportunity.
- **Alt-text / title patterns:** extract the recurring tokens in top-ranking
  images; these are the descriptors Google associates with the query.
- **Format distribution:** infer WebP vs JPEG vs PNG from the image-url
  extension across the top results; recommend matching the prevailing format.
- **Opportunity gap:** keywords where the user already has organic rankings but
  zero image presence are the highest-ROI image targets.

## Keyword research (the volume / difficulty / intent triad)

Never act on one column alone. Combine:

- **Volume** = ceiling of demand. High volume with high difficulty and your weak
  authority = a long-term play, not a quick win.
- **Difficulty** = effort to rank. Prioritize the volume-x-(low difficulty)
  quadrant for near-term wins.
- **Intent** = whether the click converts. A transactional keyword at lower
  volume often beats an informational keyword at higher volume for revenue.
- **Trend / seasonality** = timing. Rising-trend keywords deserve content before
  the peak; seasonal ones need a publish-by date.

Cluster the output by intent and topic before recommending; a flat list of 50
keywords is not a strategy. Map each cluster to one page/pillar.

## Backlink profile

Given totals + referring domains + domain rank + spam score + anchors +
new/lost time series:

- **Referring domains > raw backlink count.** 500 links from 10 domains is
  weaker than 200 links from 150 domains. Lead with referring-domain count.
- **Spam score / toxicity:** a high share of high-spam referring domains is a
  risk signal, not an asset; flag for potential disavow review.
- **Anchor distribution:** over-optimized exact-match anchors look manipulative;
  a natural profile is mostly branded + URL + generic anchors.
- **Velocity (new vs lost):** steady gain = healthy; a spike of low-quality new
  links or a cliff of lost links both warrant explanation.
- **Dofollow ratio:** context only; a 100% dofollow profile is itself unnatural.

## Competitor & intersection analysis

- **Keyword overlap %** identifies true SERP competitors (often different from
  the user's named business competitors).
- **Domain intersection** across 2-20 domains surfaces "everyone ranks but us"
  keywords (table-stakes gaps) and "only one competitor ranks" keywords
  (contestable wedges).
- **Backlink intersection** surfaces link sources that link to multiple
  competitors but not the user — the highest-probability outreach targets.
- **Traffic estimation** is directional; treat as relative ordering between
  domains, not absolute visitor counts.

## On-page / technical

- Triage in priority order: indexability/status codes > Core Web Vitals (LCP,
  INP, CLS) > metadata/titles > content depth/word count > broken links.
- Lighthouse SEO and performance scores are diagnostics, not the goal; map each
  low sub-score to a concrete fix (e.g. low LCP -> image weight, render-blocking
  resources).
- Cross-reference parsed word count and structure against the SERP's dominant
  page depth before declaring "thin content".

## GEO / AI visibility

- **YouTube is a GEO lever.** Among content signals, YouTube mentions show the
  strongest observed correlation with AI citations (reported ~0.737 in the
  source material). Treat video presence and transcript coverage as part of an
  AI-visibility plan, not just an organic-search afterthought. Verify any
  specific correlation figure against a current source before asserting it as
  fact — it is freshness-sensitive.
- **ChatGPT-scrape read:** capture which sources the model cites for the target
  query; the cited domains are the de-facto GEO competitive set.
- **LLM mention workflow:** (1) search mentions of the brand/keyword, (2) top
  cited domains for the topic, (3) top cited pages, (4) aggregate metrics /
  trend, then (5) cross-model comparison to see how visibility differs across
  ChatGPT / Claude / Perplexity. The gap between "pages that rank in Google" and
  "pages LLMs cite" is the GEO opportunity.

## Confidence and freshness

- Label every conclusion's data source: **live/provider-supplied** vs
  **user-supplied export** vs **static reasoning**.
- SERP positions, AI-overview presence, LLM citation share, pricing, and
  marketplace/robots policies are all freshness-sensitive. Do not present a
  dated export as the current state without saying when it was captured.
- When sample is thin (few keywords, one location, a single crawl), report
  directionally and say what additional pull would firm it up.
