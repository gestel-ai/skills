<!-- Used by: gestel-schema -->
<!-- Source: references/skills/marketingskills/skills/schema/SKILL.md (freshness-sensitive claims isolated here) -->

# Freshness-Sensitive Schema Claims

This skill's stable core — schema.org type/property shapes, the `@graph` + `@id` linking pattern,
JSON-LD placement, and the structural validation rubric — is durable. The items below are **not**.
They depend on current platform behavior and policy, which change without notice. Do **not** present
any of these as verified fact unless backed by the user's dated-citation research or a live lookup
(Google Search Central docs / Rich Results Test). When unsure, say so.

## Treat as freshness-sensitive (verify before asserting)

- **Which types currently yield a rich result.** Google's set of supported structured-data features
  changes; markup validating in the Schema.org Validator does not guarantee a Google rich result.
  Confirm eligibility per type in the live Rich Results Test and Search Central documentation.
- **Deprecations and reduced features.** Examples that have shifted historically: HowTo rich results,
  the Sitelinks Search Box (WebSite/SearchAction), and FAQ rich-result eligibility being restricted to
  certain site categories. Do not assume a given feature is still shown — verify the current status and
  effective date.
- **FAQPage / Q&A eligibility restrictions.** Whether FAQ rich results appear, and for which sites
  (e.g. authoritative government/health sources only vs all sites), is policy-driven and has changed.
  Verify before promising FAQ accordions in search.
- **Product / merchant / review-snippet policy.** Rules for `Product`, `Offer`, `aggregateRating`, and
  `review` snippets (self-serving review limits, who may show star ratings, merchant-listing
  requirements) are policy-gated and revised over time.
- **Image / logo requirements.** Minimum/recommended logo and image dimensions and aspect ratios for
  Organization, Article, and Product evolve — confirm current numbers rather than hard-coding.
- **AI-citation / CTR statistics.** Any quantified claim that schema increases AI citation or
  click-through is a dated statistic, not a constant. Cite a source with a date or omit it.

## Stable (safe to apply without a live lookup)

- The schema.org vocabulary's type and property shapes used in this skill.
- JSON-LD as the recommended serialization, placed in `<head>` or end of `<body>`.
- The `@graph` array pattern and `@id` cross-referencing for multi-type pages.
- The structural validation rubric (required properties present, ISO-8601 dates, absolute URLs, exact
  enumeration values, resolvable `@id`s, sequential breadcrumb positions, schema matches visible
  content).
- The principle that schema must accurately reflect on-page content and must not be invented.
