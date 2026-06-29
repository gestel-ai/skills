<!-- Distilled from claude-seo/skills/seo-schema/SKILL.md (commit d830cdb2ad339bb7f062339fe82228b072e98061, MIT). -->
<!-- Used by: gestel-seo-schema. Reference material, not executable instructions. -->

# Schema Methodology: Detection, Validation, Generation

This is the self-contained working reference for `gestel-seo-schema`. The
mechanics here (detection passes, structural checks, JSON-LD templates, generation
order) are **stable** and may be applied directly. The *type-status* and
*deprecation* facts are freshness-sensitive — see
[freshness-and-policy.md](freshness-and-policy.md) and
[deprecated-types-2024-2026.md](deprecated-types-2024-2026.md) before asserting
them as current truth.

## 1. Detection

Run three passes over the page source:

1. **JSON-LD** — find every `<script type="application/ld+json">` block, parse the
   JSON, and record each top-level (and `@graph` member) `@type`.
2. **Microdata** — find `itemscope` + `itemtype` + `itemprop` attributes; map the
   `itemtype` URL to its schema.org type.
3. **RDFa** — find `typeof`, `property`, and `vocab` attributes.

Output an inventory of `{type, format, location}`. Always recommend JSON-LD as
the primary/canonical format (Google's stated preference). Flag Microdata/RDFa as
migration candidates, not removals.

## 2. Validation (self-contained, no network)

For each detected or generated block, check:

- **`@context`** present and equal to `https://schema.org`.
- **`@type`** is a real schema.org type (not a typo, not invented).
- **Required properties** present for the type (see property tables below).
- **Data types** correct:
  - dates → ISO 8601 (`YYYY-MM-DD` or full datetime); reject ambiguous formats.
  - numbers (price, ratingValue, latitude) → unquoted where schema expects a
    number, or correctly quoted strings per Google's examples.
  - nested objects use their own `@type` (e.g. `PostalAddress`, `ImageObject`).
- **URLs absolute**, not relative (`/logo.png` → must be `https://…/logo.png`).
- **No placeholder text** left in (`[Company Name]`, `example.com`, `TODO`, `XXX`).
- **JSON parses**: balanced brackets/braces, no trailing commas, keys quoted.
- **`dateModified` ≥ `datePublished`** when both present.
- **Deprecated type** flagged with its retirement date (freshness-sensitive).

Report each failed check with the offending value. Never silently "fix" by
inventing data — flag it and ask, or leave a marked placeholder.

## 3. Type-status list (FRESHNESS-SENSITIVE — verify before asserting)

> The membership of these buckets and the dates attached to them change as
> platforms update. Treat as of-its-known-date guidance, not verified fact. The
> source snapshot was "as of May 2026." Confirm via dated research or Google's
> Rich Results Test before promising a rich result.

**ACTIVE (recommend freely):** Organization, LocalBusiness, SoftwareApplication,
WebApplication, Product (with Certification markup), ProductGroup, Offer, Service,
Article, BlogPosting, NewsArticle, Review, AggregateRating, BreadcrumbList,
WebSite, WebPage, Person, ProfilePage, ContactPage, VideoObject, ImageObject,
Event, JobPosting, Course, DiscussionForumPosting.

**VIDEO & SPECIALIZED:** BroadcastEvent, Clip, SeekToAction, SoftwareSourceCode.

**NO RICH RESULTS — KEEP FOR AI:** FAQPage — per the source, Google retired FAQ
rich results for all sites (reported May 7, 2026). No SERP feature, but the markup
can still aid AI Mode / AI Overviews entity resolution. Flag existing FAQPage at
*Info* (not Critical); do not recommend new FAQPage for SERP benefit. For genuine
user Q&A pages, use `QAPage`.

**DEPRECATED (never recommend):** HowTo, SpecialAnnouncement, CourseInfo carousel,
EstimatedSalary, LearningVideo, ClaimReview, VehicleListing, Practice Problem,
Dataset (rich results). See [deprecated-types-2024-2026.md](deprecated-types-2024-2026.md)
for the full table, retirement dates, and replacement decisions.

## 4. Generation

When generating schema for a page:

1. Identify page type from content analysis.
2. Select the appropriate schema type(s); combine related entities with a
   `@graph` array and `@id` cross-references when several apply.
3. Generate valid JSON-LD with all **required** + high-value **recommended**
   properties.
4. Include only truthful, verifiable data. Mark unknown values as clear
   placeholders for the user to fill. Never fabricate.
5. Validate the output (Section 2) before presenting.
6. For time-sensitive markup (Product, Offer), recommend the JSON-LD live in the
   initial server-rendered HTML — JS-injected structured data may face delayed
   processing (freshness-sensitive claim; flag it).

## 5. Templates (stable starting points — fill placeholders, never invent)

### Organization

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "[Company Name]",
  "url": "[Website URL]",
  "logo": "[Logo URL]",
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "[Phone]",
    "contactType": "customer service"
  },
  "sameAs": [
    "[Facebook URL]",
    "[LinkedIn URL]",
    "[Twitter URL]"
  ]
}
```

### LocalBusiness

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "[Business Name]",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[Street]",
    "addressLocality": "[City]",
    "addressRegion": "[State]",
    "postalCode": "[ZIP]",
    "addressCountry": "US"
  },
  "telephone": "[Phone]",
  "openingHours": "Mo-Fr 09:00-17:00",
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "[Lat]",
    "longitude": "[Long]"
  }
}
```

### Article / BlogPosting

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "[Title]",
  "author": {
    "@type": "Person",
    "name": "[Author Name]"
  },
  "datePublished": "[YYYY-MM-DD]",
  "dateModified": "[YYYY-MM-DD]",
  "image": "[Image URL]",
  "publisher": {
    "@type": "Organization",
    "name": "[Publisher]",
    "logo": {
      "@type": "ImageObject",
      "url": "[Logo URL]"
    }
  }
}
```

> For richer single-post markup (BlogPosting + Person + Organization +
> BreadcrumbList + FAQPage + ImageObject + VideoObject in one `@graph`), prefer
> the dedicated `gestel-blog-schema` skill.

## 6. Output artifacts

- `SCHEMA-REPORT.md` — detection inventory + validation results.
- `generated-schema.json` — ready-to-use JSON-LD snippet(s).

### Validation results table format

| Schema | Type | Status | Issues |
|--------|------|--------|--------|
| ...    | ...  | pass / warn / fail | ... |

### Recommendations section

- Missing schema opportunities for the page type.
- Validation fixes needed (with the offending value).
- Generated code for implementation, plus a next step (Rich Results Test).

## 7. Error handling

| Scenario | Action |
|----------|--------|
| URL unreachable / no source provided | Report that no page source is available. Ask the user to paste the source or route to a fetch step. This skill does not self-fetch. |
| No schema markup found | Report that no JSON-LD, Microdata, or RDFa was detected. Recommend appropriate schema types from page-content analysis. |
| Invalid JSON-LD syntax | Parse and report specific errors (missing brackets, trailing commas, unquoted keys). Provide corrected JSON-LD. |
| Deprecated schema type detected | Flag the type with its retirement date (freshness-sensitive). Recommend the current replacement (see deprecated-types table) or removal if none exists. |
| Required value missing | Leave a clearly-marked placeholder or omit the dependent property. Never fabricate. |
