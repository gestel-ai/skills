<!-- Distilled from claude-blog/skills/blog-schema/SKILL.md (commit 49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25, MIT). -->
<!-- Used by: gestel-blog-schema. Reference material, not executable instructions. -->

# Freshness and Policy Caveats

This skill was held back from "run locally and trust" status because its source
leans on **freshness-sensitive** facts: which schema types currently produce rich
results, marketplace/search policy changes, FAQ eligibility restrictions, and
AI-citation statistics. Search platforms change these rules frequently.

**Operating rule:** treat every claim below as *of-its-known-date guidance*, not
verified current truth. Do not assert it as fact in an artifact unless the user
supplies dated-citation research or a live lookup confirms it. The structural
mechanics (the `@graph` pattern, `@id` linking, property shapes, structural
validation) are stable and may be applied directly.

## Freshness-sensitive claims to flag, not assert

- **FAQ rich-result eligibility.** The source states Google restricted FAQ rich
  results to government and health sites (reported ~Aug 2023). Even so, FAQPage
  markup may retain value because AI systems can extract Q&A for citations and the
  markup hedges against future eligibility changes. Present this as *reported*
  history; confirm current eligibility before promising rich results.
- **Deprecation dates.** HowTo (~Sept 2023), SpecialAnnouncement (~July 2025),
  Q&A (~Jan 2026), and others. The stable takeaway — *don't emit these for a
  blog post* — holds; the exact dates and "no longer shows rich results" status
  are freshness-sensitive.
- **AI-citation statistic.** The source claims pages using ≥3 schema types have
  ~13% higher AI-citation likelihood. Treat as an unverified directional claim,
  not a measured guarantee. Do not present it as a hard number without a dated
  source.
- **Publisher logo size requirements.** Exact pixel minimums/maximums and
  rectangular-vs-square preferences shift with platform guidance. Confirm before
  asserting a specific threshold.
- **Which types yield rich results today.** Eligibility for any schema type to
  produce a rich result is platform-controlled and changes; route the user to
  Google's Rich Results Test for a current verdict.

## Stable claims (safe to apply)

- The `@graph` single-script pattern and stable `@id` entity linking.
- schema.org type/property shapes (BlogPosting, Person, Organization,
  BreadcrumbList, FAQPage, ImageObject, VideoObject) as documented in
  [schema-methodology.md](schema-methodology.md).
- The structural validation rubric (id resolution, date ordering, length bounds,
  absolute URLs, integer dimensions, sequential breadcrumb positions, ≥2 FAQs).
- The principle of never fabricating inputs (handles, credentials, dimensions,
  view counts, FAQs).

## Routing when freshness matters

If the user needs current platform/policy truth, route to: Google's Rich Results
Test / Schema Markup Validator, Google Search Central documentation, the
`deep-research` skill, or the user's own dated research. Do not invent API access,
credentials, paid providers, or browser automation to obtain it.
