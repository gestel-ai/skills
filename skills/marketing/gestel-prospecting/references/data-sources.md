<!-- Distilled from marketingskills/skills/prospecting/references/data-sources.md (MIT, commit 8bfcdffb). -->
<!-- Tool-integration adapters (Apollo/Clay/ZoomInfo/etc.) and the github-prospects.js CLI are NOT bundled in this skill. -->
<!-- Treat every named provider below as an external, often paid, capability the user must already have. -->

# Prospecting Data Sources

Tool selection guide for prospecting across all three branches.

These are descriptions of provider categories and trade-offs, not installed tools. This skill ships no provider adapters, no API keys, and no extraction scripts. When a provider is named, assume the user must already have access; if they don't, route to a separate adapter/implementation task instead of inventing access.

---

## Tool selection by goal

| Goal | Primary tools | Notes |
|------|--------------|-------|
| **Build initial firmographic list (B2B / SaaS)** | Apollo, ZoomInfo, Clay | Apollo for breadth, ZoomInfo for enterprise + intent, Clay for custom workflows |
| **Decision-maker mapping** | LinkedIn Sales Navigator (manual), Apollo, ZoomInfo | Sales Nav is the gold standard. Never bulk scrape it. |
| **Tech stack qualification (SaaS)** | BuiltWith, Wappalyzer | BuiltWith has wider coverage + paid plans for bulk; Wappalyzer is lighter + free for small use |
| **Funding signals (SaaS)** | Crunchbase, Pitchbook | Crunchbase free tier sufficient for early signals; Pitchbook for deeper investor data |
| **Email pattern discovery** | Hunter, Snov, Apollo | Pattern guessing — followed by verification |
| **Email deliverability verification** | Truelist, Hunter, NeverBounce, ZeroBounce | Always verify before adding to outreach lists |
| **Visitor identification (warm intent)** | RB2B, Clearbit Reveal | Anonymous traffic → company identification |
| **Intent data** | ZoomInfo Intent, 6sense, Bombora | Pre-warmed signals; mid-market+ pricing |
| **Trigger event monitoring** | Google Alerts, Feedly, LinkedIn Sales Nav alerts | Free options are sufficient for most |
| **Local business discovery** | Google Maps (manual), Yelp, Facebook Pages | Browser-assisted, not bulk-extracted |

---

## Apollo

**Use for**: General B2B / SaaS firmographic + contact data. Best starting point if you don't already have a list.

**Strengths**: large database, strong filtering UI (industry, size, technologies, signals), integrated email + LinkedIn finder, pay-as-you-go and tiered plans.

**Watch out for**: data freshness varies — re-verify before scoring as "Hot"; email accuracy ~60–80% — always validate; bulk export limits apply.

External paid provider — not bundled in this skill.

---

## Clay

**Use for**: Multi-source enrichment, waterfall lookups, custom scoring logic. When list quality matters more than list size.

**Strengths**: waterfall logic (Apollo → ZoomInfo → Clearbit fallback), 100+ data provider integrations, AI-powered enrichment, custom columns + scoring formulas.

**Watch out for**: per-credit pricing can spike on large lists; complexity overhead — easy to over-engineer workflows.

External paid provider — not bundled in this skill.

---

## ZoomInfo

**Use for**: Enterprise B2B + intent data. Mid-market+ buyer profiles.

**Strengths**: enterprise-grade firmographic depth, intent signals, best-in-class for >$50K ACV B2B.

**Watch out for**: expensive ($15K+/yr starter), overkill for SMB, typically multi-year contracts.

External paid provider — not bundled in this skill.

---

## Clearbit

**Use for**: Email → company enrichment, anonymous visitor identification (Clearbit Reveal).

**Strengths**: strong company enrichment, email lookup by domain, Reveal for company-level visitor ID, API-first.

**Watch out for**: bundled into HubSpot Breeze Intelligence post-2023 acquisition; standalone API pricing/access depends on tier.

External paid provider — not bundled in this skill.

---

## Hunter / Snov

**Use for**: Email pattern discovery + lightweight verification on small lists.

**Hunter**: domain-based email discovery, built-in deliverability verification, reasonable free tier.
**Snov**: email finder + drip campaigns, bulk verification, cheaper at scale.

**Watch out for**: both are pattern-guessing tools — always run results through a dedicated validator before outreach.

External providers — not bundled in this skill.

---

## Truelist

**Use for**: Email deliverability validation before adding contacts to outreach lists. Critical safety step.

**Strengths**: single-email sync verification + bulk async; returns `email_state` (ok / email_invalid / risky / unknown / accept_all) + `email_sub_state` (email_ok / is_disposable / is_role / unknown_error / failed_smtp_check) + did-you-mean typo suggestions; catches catch-all domains, role accounts, spam traps, disposable providers.

**Why this matters**: cold email reputation craters when bounce rates exceed 2%. Validating before sending is non-negotiable. Apollo/ZoomInfo/Hunter data is often 60–80% accurate — a validator catches the rest.

External paid provider — not bundled in this skill. If no validator is available, flag emails as unverified rather than asserting deliverability.

---

## LinkedIn Sales Navigator

**Use for**: Manual decision-maker discovery. Gold standard for B2B / SaaS but only as a research tool.

**Hard rules**: never bulk scrape (account ban risk is real and permanent); use as a research interface — open profiles, read, capture key data manually; verify the legitimacy of any tool claiming LinkedIn-overlap data before assuming compliance.

No API/MCP access at consumer level. Manual research only.

---

## BuiltWith / Wappalyzer

**Use for**: Tech stack qualification (SaaS branch).

**BuiltWith**: ~50K+ technologies tracked, API + bulk lookups (paid), historical data.
**Wappalyzer**: free browser extension, paid API, lighter coverage, faster for one-off lookups.

Cross-reference both for high-confidence tech stack signals. External providers — not bundled.

---

## Crunchbase

**Use for**: Funding signals (SaaS branch).

**Strengths**: free tier shows recent funding events; paid unlocks alerts and deep history; API access for paid users.

**Watch out for**: best coverage for VC-backed companies; self-reported data — verify amounts independently.

---

## GitHub (stargazers / forks / watchers)

**Use for**: Developer-intent prospecting. Stargazers/forks of competitor or category-defining repos are in-market signal, especially for dev-tool SaaS.

**Strengths**: public API (no scraping concerns), high signal quality, free with authenticated rate limit.

**Watch out for**: only ~5–20% of users publish email — pair with enrichment; very-popular repos (100K+ stars) are mostly noise; most prospects are individuals, so company attribution takes extra work.

> Boundary: the upstream skill referenced a bundled `github-prospects.js` CLI for pagination + enrichment + CSV output. That script is NOT present in this skill. Use the public GitHub API directly (or an MCP GitHub tool the user has) and route any "build me the CLI" request to an implementation task. Do not assume the CLI exists.

---

## Firecrawl / Browserbase (single-target site research)

**Use for**: Programmatically extracting content from a **prospect's own website** you already found via manual discovery. Not for scraping platforms.

**Firecrawl**: clean LLM-ready markdown, handles most JS-rendered sites — good for SMB website-status checks and B2B about/team page extraction.
**Browserbase**: real Chromium for JS-heavy pages, cookie dialogs, form submission, session state.

### Critical compliance line

- ✓ OK: extracting content from a single business's own website (`joescoffeeshop.com`) found through manual discovery.
- ✗ NOT OK: pointing them at `google.com/maps`, LinkedIn search, Yelp listings, or any platform whose ToS prohibits bulk extraction.

External providers — not bundled. This skill does not run browser automation itself; if a task needs live rendering or extraction, route to the appropriate browser/adapter task.

---

## RB2B / Clearbit Reveal

**Use for**: Identifying anonymous site visitors as warm intent signals.

**Strengths**: pixel-based visitor → company identification; high intent; Slack/email alerts.

**Watch out for**: privacy/GDPR considerations; person-level ID raises higher concern than company-level.

External providers — not bundled.

---

## Free / browser-only fallbacks

When the user has no paid tools, lean on: Google Search (exact name + city + role), LinkedIn (manual, no scraping), Crunchbase free tier, Wappalyzer extension, Hunter free tier, Google Maps (Local SMB), business websites + About pages, news/press releases via Google Alerts.

Slower than tooled-up workflows, but produces high-quality smaller lists.

---

## Sequencing recommendations

A typical full-stack workflow (adapt to the tools the user actually has):

1. Define ICP from product-marketing context (no tools needed)
2. Initial list from Apollo or ZoomInfo (firmographic filter)
3. Enrich with Clay (waterfall: tech stack, funding, trigger events)
4. Decision-maker mapping in LinkedIn Sales Nav (manual)
5. Email pattern discovery with Hunter or Apollo's built-in
6. Email validation with a deliverability validator before final list
7. Hand off to cold-email work for outreach copy
