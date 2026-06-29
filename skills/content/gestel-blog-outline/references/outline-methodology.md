<!-- Distilled from claude-blog/skills/blog-outline/SKILL.md (MIT, commit 49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25). -->
<!-- Reference material for gestel-blog-outline. Not executable instructions. -->

# Blog Outline Methodology

A blog outline is a **skeleton only**: heading hierarchy, per-section word-count
targets, FAQ slots, visual-placement markers, and content-gap notes. It is a
lighter artifact than a full content brief — it does **not** include deep
statistics research, full competitive analysis, or finished image suggestions.
The output is meant to be handed off to a downstream "write" step.

## Inputs to gather

1. **Topic or target keyword** (required).
2. **Target keyword** — the exact phrase to rank for, if different from the topic.
3. **Search intent** — Informational, Commercial, or Transactional.

If only a topic is given, infer a plausible keyword and intent from context and
state the inference explicitly.

## Competitive / SERP analysis

The structure should be informed by how the current top results are organized.
This requires either (a) live search results, or (b) competitor data the user
provides (pasted SERP snippets, exported headings, screenshots, competitor URLs
with extracted outlines). For each of the top ~5 results, capture:

- **Heading structure** — which H2/H3 topics are covered.
- **Content length** — approximate word count.
- **Visual elements** — charts, images, videos, infographics.
- **FAQs** — FAQ sections or "People Also Ask" coverage.
- **Unique angles** — what makes each result distinct.
- **Gaps** — what is missing or weak across the set.

Then compile a summary of common patterns and missed opportunities. If no live
lookup and no user-provided competitor data are available, build the outline
from stable editorial judgment for the topic/intent and clearly flag that the
SERP-informed parts are assumptions, not verified competitive data.

## Outline output template

```text
# Outline: [Topic]

## Title Suggestions
1. [Primary title - 40-60 chars, front-loaded keyword, power word]
2. [Alternative title - different angle]
3. [Alternative title - question format]

## Target Parameters
- Primary keyword: [keyword]
- Search intent: [Informational/Commercial/Transactional]
- Target word count: [X,XXX] words
- H2 sections: [6-8]
- Target reading level: Flesch 60-70

---

## Outline

### H2: [Section Title - Question Format] (~300-400 words)
- Answer-first opener: [What stat or fact should open this section?]
- Key points to cover:
  - [Point 1]
  - [Point 2]
  - [Point 3]
- H3: [Subsection] (only if the topic warrants subdivision)
  - [What this subsection covers]
- Key statistic to find: [What data point would strengthen this section?]
- Chart suggestion: [Bar/Line/Donut/None] - [What data to visualize]
- Image placement: [Yes/No] - [Description of recommended image]

### H2: [Section Title] (~300-400 words)
[... repeat for 6-8 sections ...]

### FAQ Section (3-5 items)
1. [Question from People Also Ask] - [Brief answer direction]
2. [Question from People Also Ask] - [Brief answer direction]
3. [Question from SERP / topic analysis] - [Brief answer direction]

### Conclusion (~100-150 words)
- Key takeaways to summarize
- Call to action direction

---

## Internal Linking Zones
- Link TO from this post: [Existing content that should be referenced]
- Link FROM to this post: [Existing content that should link here]

## Content Gaps to Exploit
1. [What competitors miss that this post should cover]
2. [Unique angle or original perspective to include]
3. [Format advantage - visuals, depth, or structure competitors lack]
```

## Heading and structure heuristics

- 60-70% of H2 headings should be in question format.
- Each H2 should have a clear answer-first paragraph prompt.
- Add H3 subsections only where the topic genuinely warrants subdivision.
- Per-section word-count targets must sum to the overall post target.
- Chart-type suggestions should be diverse — avoid repeating the same type.
- Image-placement markers should be distributed evenly across the post.

## Content-gaps pass

After the outline, add a dedicated content-gaps analysis:

1. List 3-5 topics or angles that all top-ranking competitors miss.
2. Identify opportunities for original data, case studies, or perspectives.
3. Note format advantages this post can have (more or better visuals, clearer
   structure, deeper coverage of a specific subtopic).

## Saving

Save the outline to `outlines/[slug]-outline.md` (or a user-specified path),
creating the `outlines/` directory if it does not exist. Note that the outline
is ready for a downstream blog-writing step to consume.
