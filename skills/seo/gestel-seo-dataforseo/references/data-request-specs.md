<!-- Updated: 2026-06-28 | v1.0 -->
<!-- Used by: gestel-seo-dataforseo -->

# DataForSEO Request Spec Catalog

This catalog is a **specification of what to ask for**, not a fetch mechanism.
Use it in two ways:

1. **Interpret a supplied export.** When the user pastes or uploads data, match
   it to a row below to know which fields to expect and how to read them.
2. **Emit a request spec.** When a question needs live data the user does not
   yet have, hand them the exact endpoint, parameters, expected fields, and cost
   tier so they can run it through *their own* DataForSEO adapter / MCP server /
   dashboard and bring the result back.

GESTEL never calls these endpoints itself. There is no credential, no live MCP
connection, and no cost-metering script in this skill. See the Boundaries
section of `SKILL.md`.

## Locale defaults (state them in every spec)

- `location_code = 2840` (United States) unless the user gives a market.
- `language_code = en` unless the user gives a language.
- `device = desktop`, `depth = 100` for SERP unless told otherwise.
- Always echo the locale you assumed so the user can correct it before spending
  credits. Wrong locale = wasted credits + misleading rankings.

## Field discipline

Request only SEO-relevant fields. DataForSEO's full responses are large; a
trimmed field set (the upstream extension claims ~75% smaller responses) saves
tokens and money. When emitting a spec, list the minimal fields you actually
need rather than "everything".

## Cost tiers (approximate, USD, verify against the user's current rate card)

| Tier | Endpoint family | Approx. per call |
| --- | --- | --- |
| Cheap | SERP single query | $0.001 - 0.003 |
| Cheap | Keyword volume / difficulty / intent (per keyword) | $0.0005 - 0.002 |
| Medium | Backlink summary | $0.002 - 0.005 |
| Medium | Backlink list / anchors / referring domains | $0.005 - 0.01 |
| Expensive | On-page crawl / Lighthouse (per page) | $0.01 - 0.05 |
| Expensive | AI optimization (ChatGPT scraper, LLM mentions) | ~$0.01 |

**5x multiplier warning:** image/organic SERP queries that use `site:` or
`filetype:` operators are billed at ~5x. Flag this before recommending a
filtered query.

These numbers are stale-prone. Present them as planning estimates, never as
the user's actual bill, and tell the user to confirm against their own pricing.

## Endpoint specs

### SERP

| Job | MCP tool(s) | Key params | Expected fields | Tier |
| --- | --- | --- | --- | --- |
| Google organic SERP | `serp_organic_live_advanced` | keyword, `se` (google/bing/yahoo), location_code, language_code, device, depth | rank, url, title, description, domain, featured snippet, AI-overview refs, People-Also-Ask | Cheap |
| Google Images SERP | `serp_google_images_live_advanced` | keyword, depth (max 700, billed per 100), search_param | position, title, alt text, source page url, image url, domain | Cheap (5x if `site:`/`filetype:`) |
| YouTube search | `serp_youtube_organic_live_advanced` | keyword, location_code | video title, channel, views, upload date, description, url | Cheap |
| YouTube video deep-dive | `serp_youtube_video_info_live_advanced`, `..._comments_...`, `..._subtitles_...` | video_id | metadata, top comments, transcript | Cheap-Medium |

### Keyword research

| Job | MCP tool(s) | Key params | Expected fields | Tier |
| --- | --- | --- | --- | --- |
| Keyword ideas / suggestions / related | `dataforseo_labs_google_keyword_ideas`, `..._keyword_suggestions`, `..._related_keywords` | seed keyword, location_code, language_code, limit | keyword, volume, CPC, competition, difficulty, trend | Cheap |
| Search volume | `kw_data_google_ads_search_volume` | keywords[], location_code, language_code | keyword, monthly volume, CPC, competition, monthly trend | Cheap |
| Difficulty | `dataforseo_labs_bulk_keyword_difficulty` | keywords[], location_code | keyword, difficulty 0-100 | Cheap |
| Intent | `dataforseo_labs_search_intent` | keywords[], location_code | keyword, intent (info/nav/commercial/transactional), confidence | Cheap |
| Trends over time | `kw_data_google_trends_explore` | keywords[], date_from, date_to, location_code | time series, direction, seasonality | Cheap |

### Domain & competitor

| Job | MCP tool(s) | Key params | Expected fields | Tier |
| --- | --- | --- | --- | --- |
| Backlink profile | `backlinks_summary`, `backlinks_backlinks`, `backlinks_anchors`, `backlinks_referring_domains`, `backlinks_bulk_spam_score`, `backlinks_timeseries_summary` | target, limit | total backlinks, referring domains, domain rank, spam score, top anchors, new/lost over time, dofollow ratio | Medium |
| Competitors | `dataforseo_labs_google_competitors_domain`, `..._domain_rank_overview`, `..._bulk_traffic_estimation` | target | competitor domains, keyword overlap %, est. traffic, domain rank | Medium |
| Ranked keywords | `dataforseo_labs_google_ranked_keywords`, `..._relevant_pages` | target, limit, location_code | keyword, position, url, volume, traffic share, SERP features | Medium |
| Domain/backlink intersection | `dataforseo_labs_google_domain_intersection`, `backlinks_domain_intersection` | domains[] (2-20) | shared keywords with per-domain positions, shared backlink sources, unique keywords | Medium |
| Bulk traffic estimate | `dataforseo_labs_bulk_traffic_estimation` | domains[] | est. organic traffic, traffic cost, top keywords | Cheap-Medium |
| Subdomains | `dataforseo_labs_google_subdomains` | target, location_code | subdomain, ranked-keyword count, est. traffic, organic cost | Medium |
| Top searches mentioning domain | `dataforseo_labs_google_top_searches` | target, location_code | query, volume, domain position, SERP features, traffic share | Medium |

### Technical / on-page

| Job | MCP tool(s) | Key params | Expected fields | Tier |
| --- | --- | --- | --- | --- |
| On-page analysis | `on_page_instant_pages`, `on_page_content_parsing`, `on_page_lighthouse` | url | status codes, meta tags, content size, timing, broken links, on-page checks, parsed text + word count, Lighthouse perf/a11y/best-practices/SEO + Core Web Vitals | Expensive |
| Tech stack | `domain_analytics_technologies_domain_technologies` | target | technology, version, category (CMS/analytics/CDN/framework) | Cheap-Medium |
| WHOIS | `domain_analytics_whois_overview` | target | registrar, creation/expiry, nameservers, registrant (if public) | Cheap |

### Content & business

| Job | MCP tool(s) | Key params | Expected fields | Tier |
| --- | --- | --- | --- | --- |
| Content analysis | `content_analysis_search`, `content_analysis_summary`, `content_analysis_phrase_trends` | keyword or url | content matches w/ quality score, sentiment, readability, phrase trends | Medium |
| Business listings | `business_data_business_listings_search` | keyword, location | name, description, category, address, phone, domain, rating, review count, claimed status | Medium |

### AI visibility / GEO

| Job | MCP tool(s) | Key params | Expected fields | Tier |
| --- | --- | --- | --- | --- |
| ChatGPT search scrape | `ai_optimization_chat_gpt_scraper` (+ `..._locations`) | query, location_code, language_code | ChatGPT answer content, cited sources/urls, referenced domains | Expensive |
| LLM mention tracking | `ai_opt_llm_ment_search`, `..._top_domains`, `..._top_pages`, `..._agg_metrics`, `..._cross_agg_metrics` (+ `ai_opt_llm_ment_loc_and_lang`, `ai_optimization_llm_models`) | keyword, location_code, language_code | mention count, top cited domains/pages w/ frequency, mention trends, cross-model visibility | Expensive |

## Utility lookups (no dedicated job, but worth knowing)

Location and language lookups, supported-LLM lists, and filter-option helpers
exist upstream (e.g. `ai_optimization_chat_gpt_scraper_locations`,
`ai_opt_llm_ment_loc_and_lang`, `ai_optimization_llm_models`). When a user's
adapter exposes them, use them to resolve location/language codes before
spending on the main call. GESTEL does not maintain its own copy of these
lookup tables.
