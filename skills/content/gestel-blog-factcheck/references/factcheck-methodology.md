<!-- Distilled from claude-blog/skills/blog-factcheck/SKILL.md (commit 49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25, MIT). -->
<!-- Used by: gestel-blog-factcheck -->

# Fact-Check Methodology

Deep reference for `gestel-blog-factcheck`. Load before scoring. Everything here
is stable methodology — claim extraction, structural scoring, the evidence
triple, and report shape — and runs against local files. The only part that
needs live evidence is the optional factual match against a fetched/pasted
source page; that part is explicitly gated.

## 1. Claim model

For every data claim, capture:

| Field | Description |
|-------|-------------|
| claim_text | The exact sentence or phrase containing the statistic |
| value | The numeric value (e.g., "42%", "$1.2M", "3x") |
| attribution | Named source if present (e.g., "HubSpot", "Gartner 2025") |
| url | Cited URL if present (markdown link or parenthetical) |
| location | Heading or line number where the claim appears |

## 2. Claim extraction patterns

**Fully cited (highest priority — these are checkable):**

- `[Number]% [claim] ([Source], [Year])` — parenthetical citation
- `[claim] [Number]% ... [markdown link to source]` — inline link
- `According to [Source], [Number]...` — attribution lead

**Uncited statistics (flag for sourcing):**

- `[Number]% of [noun phrase]` — standalone percentage
- `[Number]x more/less/higher/lower` — multiplier claims
- `$[Number] [claim]` — dollar figures without attribution

**Weak signals (check surrounding context before extracting):**

- `studies show`, `research indicates`, `data suggests` + a nearby number
- `survey found`, `report reveals`, `analysis shows` + a nearby number
- Round numbers in isolation ("millions of users") — skip unless specific

## 3. The evidence triple (structural verification)

A claim is well-sourced only when all three are present. Score the structure
from the file alone — no fetching required:

1. **Year anchor in prose** — the claim states or implies *when* the data is from
   ("In a 2025 survey...", "...as of Q1 2025"). Stats without a date are
   suspect because they may be silently stale.
2. **Inline citation** — names the **publisher** and the **work/title**, not just
   a bare domain ("HubSpot's 2025 State of Marketing Report", not "a study").
3. **URL** — a resolvable link to the specific page carrying the number (ideally
   the subpage with the stat, not a homepage).

Record a fourth dimension at report time when a live fetch is used: the
**retrieval date** the source was accessed.

### Structural status (offline, always available)

| Status | Criteria |
|--------|----------|
| STRUCTURE-OK | Has year anchor + named inline citation + a plausible specific URL |
| PARTIAL-CITE | Has a URL or attribution but is missing the year anchor or names only a vague source |
| UNVERIFIED | No source URL provided for the claim |

STRUCTURE-OK is the **ceiling** until factual verification is done with real
evidence. It means "properly cited," not "confirmed true."

## 4. Factual verification scoring (only with live evidence)

Run this layer **only** when the user pasted the source content or an available
fetch tool returned the page. Never assign these scores from model memory.

| Score | Status | Criteria |
|-------|--------|----------|
| 1.0 | VERIFIED | Exact number found on the cited page in matching context |
| 0.7–0.9 | PARAPHRASE | Similar data, different wording/rounding/timeframe |
| 0.3–0.6 | WEAK | Page exists and is on-topic but the specific stat isn't visible |
| 0.0 | NOT FOUND | Cited page does not contain the claimed data anywhere |
| N/A | UNVERIFIED | No source URL provided |

**Scoring guidance:**

- "43%" when the source says "nearly half" → 0.8
- A "2024" claim when the source only has "2023" data → 0.7 (and flag freshness)
- A claim citing a homepage when the stat lives on a subpage → 0.3
- A 404 or unreachable URL → 0.0 (suggest web.archive.org)

**Fetch process discipline:**

- Fetch sequentially to avoid rate-limiting source sites.
- Cap at ~10 URLs per run; list the rest as SKIPPED.
- Paywalled → WEAK (0.5) with a paywall note. JS-rendered with minimal returned
  content → note it and do not over-score. PDF → flag for manual verification.

## 5. Freshness guard (the live-research boundary)

Some claims depend on facts that change over time: current platform rules, SEO
ranking behavior, marketplace/store/app-store policy, ad-platform limits, live
pricing, "largest/fastest/#1 as of today," and any "currently / now / latest"
phrasing. For these:

- A superficial source match is **not** sufficient to call them true; data ages.
- Mark them freshness-sensitive in the report and require **dated** evidence.
- Always record the retrieval date of any source consulted.
- If no dated, live-or-user-supplied evidence exists, the claim stays unconfirmed
  regardless of how authoritative the citation looks.

## 6. Report templates

### Verification Report: [Post Title]

```text
File: [path]
Claims found: [total]   Cited: [n]   Uncited: [n]
Factual verification: [performed against sources | NOT performed — structural only]
Verified: [n] | Paraphrase: [n] | Weak: [n] | Not Found: [n] | Structure-OK: [n] | Unverified: [n]
```

| # | Claim | Source URL | Score/Status | Notes |
|---|-------|-----------|--------------|-------|
| 1 | "73% of marketers..." | <https://example.com/report> | 1.0 VERIFIED | Exact match, section 3, retrieved 2026-06-28 |
| 2 | "5x ROI improvement" | <https://example.com/study> | 0.8 PARAPHRASE | Source says "nearly 5x" |
| 3 | "Platform allows X today" | <https://example.com> | STRUCTURE-OK / freshness | Policy claim — needs dated confirmation |
| 4 | "60% prefer video" | (none) | UNVERIFIED | Try: "video preference statistics 2025" |

### Recommended Actions (priority order)

1. Uncited stats that need a source URL (highest impact first).
2. NOT-FOUND / WEAK claims that need a replacement source.
3. Freshness-sensitive claims that need dated confirmation.
4. Claims whose source data may be outdated (year anchor older than ~2 years).

## 7. Evidence-triple cross-reference

The upstream `claude-blog` family treats the evidence triple (year anchor in
prose + inline citation with publisher and title + URL with retrieval date) as
the shared standard for citable claims. This skill applies that same triple as
its structural rubric. If a companion "flow"/citation-discipline skill exists in
the project, you may suggest it as a follow-up for rewriting weak citations; if
not present, just describe the manual fix. Never block the report on an
unavailable companion skill.
