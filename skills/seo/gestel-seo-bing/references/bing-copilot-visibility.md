<!-- Updated: 2026-06-28 | v1.0 -->
<!-- Used by: gestel-seo-bing -->
<!-- FRESHNESS: Copilot product surfaces and the Bing-index citation mechanism
     are dated snapshots from the source's 2024-2025 window. The eligibility
     logic and export-read patterns are stable; confirm product specifics with a
     live lookup before asserting as current. -->

# Bing index, Copilot citation eligibility, and export interpretation

## Why Bing visibility is its own job

Microsoft Copilot — across Bing Chat, Copilot in Edge/Windows, and Microsoft 365
Copilot's web grounding — draws its **web citations from the Bing index**. The
chain is: page in Bing index → eligible to be retrieved → eligible to be cited.
A page absent from the Bing index is structurally **uncitable** by Copilot no
matter how it performs in Google. So "AI search visibility outside Google" is
largely a function of Bing index presence and freshness.

## Copilot citation eligibility framework

Run these gates in order; the first failing gate is the thing to fix.

1. **Indexed in Bing?**
   - Check via `site:example.com/path` on Bing, or Bing Webmaster URL
     Inspection (user-run).
   - If absent → submit via IndexNow (see `indexnow-protocol.md`) and check for
     crawl blockers below.
2. **Discoverable quickly on publish/update?**
   - Is IndexNow wired to fire on publish and on meaningful update?
   - If not → set up IndexNow; organic crawl alone is too slow for launches.
3. **Crawlable / indexable by Bingbot?**
   - Not blocked by `robots.txt`, no `noindex` meta/header, not behind auth, not
     a JS-only render Bingbot can't resolve, canonical points to itself (or to
     the intended canonical).
   - If blocked → remove the blocker first; submitting a blocked URL is wasted.
4. **Fresh signal on change?**
   - When the page changes materially, re-ping IndexNow so the index reflects the
     version Copilot would cite.

### From "indexed" to "cited" (directional, not guaranteed)

Indexing is necessary but not sufficient. To improve the odds Copilot *picks*
the page as a citation:

- **Answer-shaped content:** clear question→answer structure, definitions, and
  self-contained claims a model can lift and attribute.
- **Extractable facts:** specific numbers, dates, named entities, and lists that
  read as citable statements rather than vague prose.
- **Freshness and accuracy:** outdated pages get superseded; keep dates and
  facts current and re-ping on update.
- **Authority signals on the topic:** corroborating internal links and inbound
  links (which Bing tracks — see below).

## Interpreting Bing Webmaster exports (the user pastes; you read)

The live Bing Webmaster Tools API (inbound links, crawl stats, search keywords,
competitor link compare) is a **Boundary** — it needs an API key and the
upstream client this skill does not have. Work from the user's pasted
export/CSV/screenshot only. Read patterns:

### Inbound / backlink data

- **Bing surfaces links Google's API doesn't.** Treat Bing's inbound-link list
  as **additive** to Google Search Console data, not a replacement — look for
  referring domains present in Bing but absent from GSC.
- **Competitor link comparison:** when the user provides their links and a
  competitor's, find referring domains the competitor has that the user doesn't
  → those are concrete outreach/placement targets.
- Weight by referring-domain diversity and relevance, not raw link count.

### Crawl-stat triage

- **Crawl errors:** prioritize by (a) is it a page you want indexed, and (b) is
  it a hard blocker (5xx, robots block, DNS) vs. soft (slow response). Hard
  blockers on important URLs come first.
- **Crawl frequency dropping** on key URLs can signal quality/freshness decay —
  pair with an IndexNow re-ping after fixing the underlying page.

### Search-keyword / impression reads

- High impressions + low clicks → title/snippet relevance or SERP-feature
  competition; a copy/meta fix (route to seo-audit / copy task), not an indexing
  fix.
- Keywords appearing in Bing but not Google (or vice versa) reveal index-coverage
  gaps worth a `site:` spot-check.
- **Only reason over numbers the user actually provided.** Never invent
  impression counts, positions, or link totals.

## Non-Google engine notes

- **One IndexNow ping reaches Bing, Yandex, Seznam (Czech), and Naver (Korea).**
  If the site has CZ or KR audiences, IndexNow is doubly worthwhile.
- **Google is intentionally out of scope** for IndexNow; Google indexing is
  sitemap- and crawl-driven and belongs to a separate SEO-Google task.

## Boundary reminder

Anything requiring a live Bing Webmaster API read, a login, or a real-time
`site:` result must come from the **user** (paste/screenshot) or a dedicated
adapter with its own credentials. This document provides the judgment to apply
to that data; it does not fetch it.
