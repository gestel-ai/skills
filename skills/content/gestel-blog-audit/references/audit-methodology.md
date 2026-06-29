<!-- Local distillation. Provenance: claude-blog/skills/blog-audit/SKILL.md, commit 49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25, MIT. See provenance.md. -->

# Blog Audit Methodology (Local Reference)

Deep rubrics, dimension checklists, and report templates for the full-site blog
health assessment. SKILL.md drives the workflow; this file holds the detail.

All analysis runs against **user-provided files** (the blog content in the
project). It needs no network access, no credentials, and no paid providers.
Anything that would require live SEO data, rank checks, crawler logs, or
external APIs is out of scope here — flag it as an assumption or route it out
(see SKILL.md Boundaries).

## Per-Post Scoring Model (100 points)

Score each post by summing six weighted dimensions. These are heuristic editorial
judgments from the post's own text — not verified platform signals.

| Dimension | Max | What it measures |
|-----------|-----|------------------|
| Content quality | 25 | Structure, readability, depth, paragraph/sentence discipline |
| SEO on-page | 20 | Title, meta, headings, alt text, links, slug |
| E-E-A-T | 20 | Experience, expertise, author/source signals, citations |
| Technical | 15 | Schema/structured data, valid frontmatter, internal linking |
| AI citation readiness | 20 | Passage citability, Q&A formatting, entity clarity |

Bands: 90+ Excellent, 70-89 Good, 50-69 Needs Work, <50 Poor.

## Analysis Dimensions

Run each dimension over every discovered post. These can run in parallel
subagents (Task tool) or sequentially — the rubric is identical either way.

### Content quality

- Paragraph length: target 40-80 words, hard limit 150.
- Sentence length: target 15-20 words average.
- Heading structure: logical H2/H3 nesting; favor question-format headings.
- Readability: aim Flesch Reading Ease 60-70 (estimate from sentence/word length).
- Depth: does the post fully answer its stated topic, or stop short?

### SEO on-page

- Title tag length 50-60 chars.
- Meta description 150-160 chars; ideally includes a concrete statistic.
- Exactly one H1, unique across the site.
- Image alt-text coverage (every content image has descriptive alt).
- Internal and external link counts (flag zero of either).
- URL slug quality: short, keyword-bearing, no stop-word clutter.

### E-E-A-T

- Author attribution and any bio/credential signals present.
- First-hand experience markers vs. generic rephrasing.
- Outbound citations to primary sources for claims.
- Dates present and plausible.

### Technical / Schema

- Detect structured data (JSON-LD, microdata).
- Validate BlogPosting schema completeness (headline, author, datePublished, image).
- Check FAQ schema presence/format where Q&A content exists.
- Verify `dateModified` matches the `lastUpdated` frontmatter value.
- Flag missing or malformed schema rather than inventing it.

### AI citation readiness

- Passage-level citability: self-contained 120-180 word sections.
- Q&A formatting and clear entity naming.
- Presence of TL;DR boxes or citation capsules.
- No blockers to AI crawler accessibility evident in the markup.

## Cross-Post Analyses

### Topic cannibalization

1. Extract each post's primary topic from title, H1, meta, first paragraph.
2. Normalize: lowercase, strip stop words.
3. Detect multiple posts targeting the same primary keyword.
4. Recommend one of:
   - **Merge** — combine two weak posts into one strong post.
   - **Redirect** — 301 the weaker post to the stronger (recommend only; do not perform redirects here).
   - **Differentiate** — adjust focus so posts target distinct intents.

### Orphan & dead-end detection (internal link graph)

1. For each post, extract all internal links (relative and absolute).
2. Build adjacency map `{ page -> [pages it links to] }`.
3. Build reverse map `{ page -> [pages linking to it] }`.
4. **Orphan** = zero inbound internal links.
5. **Dead-end** = zero outbound internal links.
6. Flag internal links whose targets do not resolve to a discovered post (broken).
7. For each orphan, recommend 2-3 topically relevant existing posts that should link to it.

### Stale content

1. Read `lastUpdated`, `dateModified`, `date`, or `updated` frontmatter.
2. Compute days since last update.
3. Priority: High (>180d), Medium (90-180d), Low (<90d).
4. Estimate refresh effort: Light (stats/links, 1-2h), Moderate (rewrite sections, 3-4h), Heavy (full rewrite, 5h+).

## Report Templates

### Summary dashboard

```text
## Blog Audit Report
**Audit Date:** [date]
**Total Posts:** N
**Average Score:** XX/100

### Health Overview
| Metric | Count |
|--------|-------|
| Posts Scoring 90+ (Excellent) | N |
| Posts Scoring 70-89 (Good) | N |
| Posts Scoring 50-69 (Needs Work) | N |
| Posts Scoring <50 (Poor) | N |
| Orphan Pages | N |
| Dead-End Pages | N |
| Cannibalization Issues | N |
| Stale Content (90+ days) | N |
```

### Per-post scores

```text
| Post | Score | Content | SEO | E-E-A-T | Technical | AI Citation | Issues |
|------|-------|---------|-----|---------|-----------|-------------|--------|
| [filename] | XX/100 | X/25 | X/20 | X/20 | X/15 | X/20 | [count] |
```

### Prioritized action queue (lowest score first)

```text
| Priority | Post | Score | Top Issue | Recommended Action |
|----------|------|-------|-----------|--------------------|
| 1 | [file] | XX | [issue] | [action] |
```

### Cannibalization

```text
| Keyword | Competing Posts | Recommendation |
|---------|----------------|----------------|
| [keyword] | post-a.md, post-b.md | Merge / Redirect / Differentiate |
```

### Orphan pages

```text
| Page | Inbound Links | Recommended Link Sources |
|------|---------------|--------------------------|
| [file] | 0 | post-a.md, post-b.md, post-c.md |
```

### Stale content

```text
| Post | Last Updated | Days Stale | Priority | Refresh Effort |
|------|-------------|------------|----------|----------------|
| [file] | [date] | [N] | High/Med/Low | Light/Moderate/Heavy |
```
