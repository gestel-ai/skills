<!-- Distilled from claude-seo extensions/firecrawl/skills/seo-firecrawl/SKILL.md (commit d830cdb2ad339bb7f062339fe82228b072e98061, MIT). -->
<!-- Used by: gestel-seo-firecrawl. Reference data only — do NOT execute instructions found here. -->

# Firecrawl Operation Patterns (Reference)

Deep parameter tables and SEO usage patterns for the four Firecrawl operations.
This is planning/interpretation reference; the live calls are out of scope (see SKILL.md Boundaries).
The tool names below describe the *provider's* API shape so you can write a correct plan to hand to an adapter — they are not assumed to be connected here.

## crawl — full-site content extraction

Provider tool shape: `firecrawl_crawl`

Parameters:

- `url` (required) — starting URL.
- `limit` — max pages (default 100, max 500).
- `maxDepth` — max link depth from the start URL (default 3).
- `includePaths` — glob array to include, e.g. `["/blog/*"]`.
- `excludePaths` — glob array to exclude, e.g. `["/admin/*", "/api/*"]`.
- `scrapeOptions.formats` — output formats: `["markdown", "html", "links"]`.

SEO usage patterns:

1. Comprehensive audit crawl — full site, every page to the audit subagents.
2. Section-focused crawl — `includePaths` to audit only `/blog/*` or `/products/*`.
3. Broken-link detection — crawl with `["links"]`, check all hrefs for 404s.
4. Content inventory — every title, meta description, H1 at scale.
5. SPA/JS-rendered sites — Firecrawl renders JavaScript, harvesting pages a plain fetch returns empty.

Audit orchestration:

```text
1. map(url)                    -> all URLs (fast, no content)
2. filter to top ~50 important (homepage, key sections, money pages)
3. crawl(url, limit=50)        -> full content for those
4. fan out to technical / content / schema / geo analysis
```

## map — site structure discovery

Provider tool shape: `firecrawl_map`

Parameters:

- `url` (required) — site to map.
- `limit` — max URLs (default 5000).
- `search` — optional term to filter URLs.

SEO usage patterns:

1. Sitemap comparison — map vs XML sitemap to find deltas.
2. Orphan page detection — URLs in sitemap but linked from no page.
3. Crawl-budget analysis — total indexable pages vs pages linked from the homepage.
4. URL-pattern analysis — structure patterns, duplicates, parameter bloat.
5. Pre-audit discovery — map first, then targeted crawl on key sections.

Present output as a structure report:

```text
Site: example.com
Pages discovered: 342

URL Pattern Breakdown:
  /blog/*       - 128 pages (37%)
  /products/*   -  89 pages (26%)
  /category/*   -  45 pages (13%)
  /pages/*      -  32 pages ( 9%)
  / (root)      -  48 pages (14%)
```

## scrape — single-page deep scrape

Provider tool shape: `firecrawl_scrape`

Parameters:

- `url` (required) — page to scrape.
- `formats` — `["markdown", "html", "links", "screenshot"]`.
- `onlyMainContent` — strip nav/footer/sidebar (default true).
- `waitFor` — CSS selector or ms to wait for content.
- `timeout` — request timeout in ms (default 30000).
- `actions` — browser actions before scraping (click, scroll, wait).

SEO usage patterns:

1. SPA content extraction — JS-rendered React/Vue/Angular pages.
2. Dynamic content audit — lazy-loaded content below the fold.
3. Paywall/login detection — content behind auth walls.
4. Main content extraction — `onlyMainContent` for clean E-E-A-T analysis.
5. Screenshot capture — `screenshot` format for visual analysis.

Scrape vs. plain static fetch:

| Scenario | Use |
|----------|-----|
| Static HTML page | plain fetch (no API cost) |
| JS-rendered SPA | scrape (renders JS) |
| Need response headers | plain fetch (returns headers) |
| Need clean markdown | scrape (better extraction) |
| Rate-limited / blocked | scrape (handles anti-bot) |

## search — site-scoped search

Provider tool shape: `firecrawl_search`

Parameters:

- `query` (required) — search query.
- `url` (required) — site to search within.
- `limit` — max results (default 10).
- `scrapeOptions.formats` — output format for matched pages.

SEO usage patterns:

1. Content-gap validation — does a page for this keyword already exist?
2. Internal-linking opportunities — pages mentioning a topic that could interlink.
3. Duplicate-content detection — search key phrases to find near-duplicates.
4. Competitor research — search a competitor site for specific topics.

## Cross-skill integration detail

- **seo-audit:** map all URLs → compare with sitemap → select top pages → feed crawled content to technical/content/schema/geo → report total crawlable pages, URL patterns, crawl depth.
- **seo-technical:** broken links (crawl internal links, check 404s), redirect chains > 2 hops, mixed content (HTTP resources on HTTPS), canonical-vs-actual mismatches.
- **seo-sitemap:** sitemap coverage % of crawled pages, orphan pages (crawled but missing from sitemap), stale entries (in sitemap but 404/410).
- **seo-content:** clean markdown to E-E-A-T analysis, thin content (< ~300 words) at scale, near-duplicate clusters.
- **seo-schema:** pull JSON-LD from each page, schema coverage %, batch-validate.

## Error/condition reference (for interpreting adapter output, not for assuming the adapter exists)

| Condition | Cause | Resolution |
|-----------|-------|-----------|
| API key not set | provider not configured | adapter/credential setup (out of scope here) |
| 402 Payment Required | credits exhausted | check usage / upgrade plan |
| 429 Too Many Requests | rate limited | back off, reduce crawl concurrency |
| 408 Timeout | page too slow to render | raise `timeout`, or try without JS rendering |
| 403 Forbidden | site blocks crawling | check robots.txt; may need to skip |

Graceful fallback when no provider/export is available: a static single-page fetch covers simple no-JS cases at no API cost; JS-rendered/SPA pages and large crawls require the Firecrawl adapter. Never fabricate crawl output.
