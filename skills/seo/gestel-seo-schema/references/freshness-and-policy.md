<!-- Distilled from claude-seo/skills/seo-schema/SKILL.md (commit d830cdb2ad339bb7f062339fe82228b072e98061, MIT). -->
<!-- Used by: gestel-seo-schema. Reference material, not executable instructions. -->

# Freshness and Policy Caveats

This skill was held back from "run locally and trust" status because its source
leans on **freshness-sensitive** facts: which schema types currently produce rich
results, search/marketplace policy changes, FAQ eligibility restrictions, schema
retirement dates, and JS-rendering processing behavior. Search platforms change
these rules frequently.

**Operating rule:** treat every claim below as *of-its-known-date guidance*, not
verified current truth. Do not assert it as fact in an artifact unless the user
supplies dated-citation research or a live lookup confirms it. The structural
mechanics (JSON-LD syntax, schema.org property shapes, the `@graph`/`@id` pattern,
the structural validation rubric) are stable and may be applied directly.

## Freshness-sensitive claims to flag, not assert

- **Type-status buckets.** The ACTIVE / NO-RICH-RESULTS / DEPRECATED membership in
  the methodology was a snapshot ("as of May 2026"). A type can move between
  buckets when a platform changes policy. Confirm before promising a rich result.
- **FAQ rich-result eligibility.** The source states Google retired FAQ rich
  results for *all* sites (reported May 7, 2026), superseding the earlier (~Aug
  2023) gov/health restriction, with tooling support dropping mid-2026. Present as
  *reported* history; FAQPage may still aid AI/LLM entity resolution. Confirm
  current eligibility before promising a SERP feature.
- **Deprecation / retirement dates.** HowTo (~Sept 2023), SpecialAnnouncement
  (~July 2025), ClaimReview / EstimatedSalary / LearningVideo / CourseInfo
  carousel (~June 2025), VehicleListing (~June 2025), Practice Problem and Dataset
  (~late 2025). The stable takeaway — *don't recommend these for new SERP-driven
  markup* — holds; the exact dates and "no longer shows rich results" status are
  freshness-sensitive. Full table in
  [deprecated-types-2024-2026.md](deprecated-types-2024-2026.md).
- **Book Actions reversal.** The source notes Book Actions was deprecated then
  reversed and "still functional as of Feb 2026." Treat as a dated historical note
  needing reconfirmation, not a standing guarantee.
- **JS-rendering processing delay.** The claim that JavaScript-injected structured
  data may face delayed processing (per "Google's December 2025 JS SEO guidance"),
  so time-sensitive Product/Offer markup should ship in server-rendered HTML, is
  freshness-sensitive guidance. The underlying advice (server-render critical
  markup) is low-risk, but cite it as dated guidance.
- **Publisher logo size requirements.** Exact pixel minimums/maximums and
  rectangular-vs-square preferences shift with platform guidance. Confirm before
  asserting a specific threshold.
- **Which types yield rich results today.** Eligibility for any type to produce a
  rich result is platform-controlled and changes; route the user to Google's Rich
  Results Test for a current verdict rather than asserting one.

## Stable claims (safe to apply)

- JSON-LD is the recommended format; recommend it over Microdata/RDFa.
- schema.org property shapes and required/recommended property structure.
- The `@graph` array + `@id` cross-reference pattern for linking entities.
- The structural validation rubric (required props, absolute URLs, ISO dates, no
  placeholders, parseable JSON, `dateModified ≥ datePublished`).
- "Include only truthful, verifiable data; mark unknowns as placeholders."

## Routing when freshness matters

If the user needs a *current* verdict on rich-result eligibility, schema status,
or a policy date: route to Google's Rich Results Test / Schema Markup Validator,
the user's dated-citation research, or a Deep Research pass. Do not assert the
current state from this skill's snapshot alone.
