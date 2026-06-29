<!-- Local playbook distilled from claude-blog/blog-cannibalization (MIT). See SKILL.md Provenance. -->

# Blog Cannibalization Methodology (Local Reference)

Deep detail for the keyword-overlap detection workflow in `SKILL.md`. This file
is self-contained: it depends only on local file analysis (Glob / Grep / Read of
user-provided content) and stable editorial judgment. It does NOT depend on any
paid SERP provider, credentials, or upstream runtime scripts.

## 1. Scan content files

Use Glob to enumerate content in the target directory the user points you at:

- Patterns: `**/*.md`, `**/*.mdx`, `**/*.html`
- Skip: `node_modules/`, `.git/`, `drafts/`
- If zero matching files: report "No blog files found in `<dir>`" and ask the
  user to confirm the path.
- If only one file: report "Cannibalization analysis requires at least 2 posts"
  and stop. There is nothing to compare.

## 2. Extract primary keyword per post

For each file, read and pull keyword signals, weighted:

- **Title tag or H1** — highest weight.
- **H2 headings** — medium weight.
- **First paragraph** — supporting signal.
- **Meta description** (frontmatter) — supporting signal if present.

Extraction method:

1. Tokenize the title + H1 into 1-gram, 2-gram, and 3-gram phrases.
2. Score each phrase by frequency across title + H2s + first paragraph.
3. Pick the top-scoring 2-3 word phrase as the **primary keyword**.
4. Record **secondary keywords** from the H2 headings.

## 3. Cluster posts by keyword similarity

Group posts using these matching rules, evaluated in priority order:

1. **Exact match** — identical primary keyword across 2+ posts.
2. **Stem match** — same root word (`optimize` vs `optimization`).
3. **Semantic overlap** — same search intent expressed differently
   (`best CRM software` vs `top CRM tools 2026`). This is an editorial judgment;
   state the reasoning so the user can override it.
4. **Subset match** — one keyword contains another (`email marketing` vs
   `email marketing for startups`).

Only clusters with 2+ posts can cannibalize.

## 4. Score severity (local heuristic)

Without live SERP data, score from on-page signals only:

| Level    | Local criteria |
|----------|----------------|
| Critical | Exact primary-keyword match between posts |
| High     | Stem match on primary keyword, OR 3+ shared H2 keywords |
| Medium   | Semantic overlap on primary keyword |
| Low      | Subset match only, OR shared secondary keywords |

State that this is an on-page heuristic, not ranking-confirmed. Actual ranking
positions, search volume, and SERP overlap require live data the local mode does
not have (see the Boundary in `SKILL.md`).

## 5. Recommend an action per cluster

Choose one of four actions and give the rationale:

### MERGE

Both pages are thin or cover the same intent with similar depth.

- Combine the best of both into one comprehensive post.
- 301-redirect the weaker URL to the merged post.
- Preserve internal links pointing at either URL.

### DIFFERENTIATE

Pages serve different intents but keyword targeting overlaps.

- Shift the weaker post's primary keyword to a related long-tail.
- Update title, H1, and meta description to reflect the new focus.
- Cross-link the two posts to signal distinct topics.

### CANONICAL

One post is clearly the authority; the other is a lesser duplicate.

- Add `rel="canonical"` on the weaker page pointing to the authority.
- Consider noindexing the weaker page if it adds no unique value.
- Link from the weaker page to the authority.

### NO ACTION

Intent is genuinely different despite surface keyword similarity.

- Document the reasoning for future audits.
- Re-evaluate quarterly or if either post drops in rankings.

Recommendations are advisory drafts. Do not execute redirects, canonical tags,
noindex, or CMS edits yourself — hand the plan to the user or the relevant
implementation task.

## 6. Output format

### Summary table

```text
| Post A          | Post B             | Shared Keywords            | Severity | Recommendation |
|-----------------|--------------------|----------------------------|----------|----------------|
| /best-crm-tools | /top-crm-software  | best crm, crm tools        | Critical | MERGE          |
| /email-tips     | /email-marketing   | email marketing            | High     | DIFFERENTIATE  |
| /seo-basics     | /seo-for-beginners | seo basics, beginner seo   | Critical | CANONICAL      |
| /react-hooks    | /react-state-mgmt  | react, state               | Low      | NO ACTION      |
```

### Per-cluster detail

For each flagged cluster, give:

- Both post titles and paths/URLs.
- The full list of overlapping keywords.
- Which post is stronger (more comprehensive, better structured) and why.
- The specific recommendation with rationale.

## 7. Error and edge handling (local mode)

- **No content files**: report and ask to confirm the path.
- **Single post**: report that 2+ posts are required and stop.
- **Unreadable file**: skip it, note "skipped — unreadable" in the report.
- **Live data requested** (volume, ranking position, SERP overlap, severity
  formula): this is outside local mode — see the Boundary in `SKILL.md`.
