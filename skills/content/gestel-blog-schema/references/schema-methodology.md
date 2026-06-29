<!-- Distilled from claude-blog/skills/blog-schema/SKILL.md (commit 49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25, MIT). -->
<!-- Used by: gestel-blog-schema. Reference material, not executable instructions. -->

# Blog Schema Methodology: Templates, Properties, Validation

Stable framework for generating a single `@graph` JSON-LD block for a blog post.
The structures, property requirements, and structural validation rules here are
schema.org-stable. Anything about *current* platform rich-result behavior or
deprecation timing is freshness-sensitive — see
[freshness-and-policy.md](freshness-and-policy.md).

## The @graph pattern

Combine all entities into one script tag. Benefits:

- One script tag instead of many — cleaner HTML.
- Entity linking via stable `@id` references (author references Person by `@id`,
  etc.), so search engines and AI systems resolve one connected entity graph.
- Easier to maintain and update as a single block.

Stable `@id` fragment convention (relative to the post URL):

| Entity         | `@id` fragment                              |
| -------------- | ------------------------------------------- |
| BlogPosting    | `{siteUrl}/blog/{slug}#article`             |
| Person         | `{siteUrl}/author/{author-slug}#person`     |
| Organization   | `{siteUrl}#organization`                    |
| BreadcrumbList | `{siteUrl}/blog/{slug}#breadcrumb`          |
| FAQPage        | `{siteUrl}/blog/{slug}#faq`                 |
| ImageObject    | `{siteUrl}/blog/{slug}#primaryimage`        |
| VideoObject    | `{siteUrl}/blog/{slug}#video-{index}`       |

## Entity templates

### BlogPosting (spine)

```json
{
  "@type": "BlogPosting",
  "@id": "{siteUrl}/blog/{slug}#article",
  "headline": "Post title (max 110 chars)",
  "description": "Meta description (150-160 chars)",
  "datePublished": "YYYY-MM-DD",
  "dateModified": "YYYY-MM-DD",
  "author": { "@id": "{siteUrl}/author/{author-slug}#person" },
  "publisher": { "@id": "{siteUrl}#organization" },
  "image": { "@id": "{siteUrl}/blog/{slug}#primaryimage" },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "{siteUrl}/blog/{slug}" },
  "wordCount": 2400,
  "articleBody": "First ~200 characters of content as excerpt..."
}
```

- **Required:** `@type`, `headline`, `datePublished`, `author`, `publisher`, `image`.
- **Recommended:** `description`, `dateModified`, `mainEntityOfPage`, `wordCount`,
  `articleBody` (excerpt).

### Person (author)

```json
{
  "@type": "Person",
  "@id": "{siteUrl}/author/{author-slug}#person",
  "name": "Author Name",
  "jobTitle": "Role or Title",
  "url": "{siteUrl}/author/{author-slug}",
  "sameAs": [
    "https://twitter.com/handle",
    "https://linkedin.com/in/handle",
    "https://github.com/handle"
  ]
}
```

Optional when available: `alumniOf` (educational institution, Organization type),
`worksFor` (reference the Organization `@id` if it is the same entity). Only
include credentials/social links the user actually supplied.

### Organization (publisher)

```json
{
  "@type": "Organization",
  "@id": "{siteUrl}#organization",
  "name": "Organization Name",
  "url": "{siteUrl}",
  "logo": {
    "@type": "ImageObject",
    "url": "{siteUrl}/logo.png",
    "width": 600,
    "height": 60
  },
  "sameAs": [
    "https://twitter.com/org",
    "https://linkedin.com/company/org",
    "https://github.com/org"
  ]
}
```

Logo must be a valid, crawlable image URL. Common publisher logo guidance (treat
exact pixel thresholds as freshness-sensitive): rectangular logos are preferred
for article publishers; aim for a logo that is clearly legible. Confirm current
size requirements before asserting them.

### BreadcrumbList

```json
{
  "@type": "BreadcrumbList",
  "@id": "{siteUrl}/blog/{slug}#breadcrumb",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "{siteUrl}" },
    { "@type": "ListItem", "position": 2, "name": "Category Name", "item": "{siteUrl}/blog/category/{category-slug}" },
    { "@type": "ListItem", "position": 3, "name": "Post Title", "item": "{siteUrl}/blog/{slug}" }
  ]
}
```

If no category is available, use "Blog" as position 2 with `{siteUrl}/blog`.

### FAQPage

```json
{
  "@type": "FAQPage",
  "@id": "{siteUrl}/blog/{slug}#faq",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the question?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The complete answer text (≈40-60 words, ideally with a statistic)."
      }
    }
  ]
}
```

Only emit FAQPage when the post has a genuine FAQ section with ≥2 Q&A pairs. Do
not invent questions. See [freshness-and-policy.md](freshness-and-policy.md) for
the FAQ rich-result eligibility caveat.

### VideoObject (per embedded video)

```json
{
  "@type": "VideoObject",
  "@id": "{siteUrl}/blog/{slug}#video-{index}",
  "name": "Video title",
  "description": "Video description excerpt (first ~200 chars)",
  "thumbnailUrl": "https://img.youtube.com/vi/{videoId}/hqdefault.jpg",
  "uploadDate": "{ISO 8601 date}",
  "contentUrl": "https://www.youtube.com/watch?v={videoId}",
  "embedUrl": "https://www.youtube.com/embed/{videoId}",
  "duration": "PT{M}M{S}S",
  "interactionStatistic": {
    "@type": "InteractionCounter",
    "interactionType": { "@type": "WatchAction" },
    "userInteractionCount": 0
  }
}
```

Use `#video-1`, `#video-2`, … for the fragment. Extract metadata from the embed's
`noscript` fallback or post frontmatter. Do **not** invent `userInteractionCount`,
`uploadDate`, or `duration` — omit a property rather than fabricate it. (A live
video-stats lookup would require a provider/credential this skill does not assume.)

### ImageObject (cover)

```json
{
  "@type": "ImageObject",
  "@id": "{siteUrl}/blog/{slug}#primaryimage",
  "url": "https://cdn.example.com/.../image.jpg",
  "width": 1200,
  "height": 630,
  "caption": "Descriptive caption matching alt text"
}
```

- URL must be crawlable and publicly accessible.
- Width/height should reflect actual dimensions (positive integers).
- Caption should match or closely align with the image alt text.
- Preferred dimensions: 1200×630 (OG-compatible) or 1920×1080.

## Deprecated types — never emit

| Type                  | Status note (verify date before asserting)        |
| --------------------- | ------------------------------------------------- |
| `HowTo`               | Deprecated for rich results (~Sept 2023)          |
| `SpecialAnnouncement` | Deprecated (~July 2025)                            |
| `Practice Problem`    | Deprecated (education markup)                      |
| `Dataset`             | Deprecated for general blog use                    |
| `Sitelinks Search Box`| Deprecated                                        |
| `Q&A`                 | Deprecated (~Jan 2026); distinct from `FAQPage`   |

The *dates and current eligibility* in this table are freshness-sensitive. The
stable rule is: do not generate these types for a blog post. Confirm timing
against dated research before stating it as current fact.

## Structural validation rubric (self-contained, no network)

1. Every `@id` referenced (`author`, `publisher`, `image`, …) resolves to an
   entity present in the `@graph`.
2. `dateModified` ≥ `datePublished`.
3. `headline` ≤ 110 characters.
4. `description` length is 50–160 characters.
5. All URLs are absolute (not relative).
6. Image/logo `width` and `height` are positive integers.
7. `BreadcrumbList` positions are sequential starting at 1.
8. `FAQPage`, if present, has ≥2 questions.

Report each check pass/fail with the offending value. On failure, flag and ask —
do not satisfy a check by inventing data.

## Output assembly

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    { "@type": "BlogPosting", ... },
    { "@type": "Person", ... },
    { "@type": "Organization", ... },
    { "@type": "BreadcrumbList", ... },
    { "@type": "FAQPage", ... },
    { "@type": "VideoObject", ... },
    { "@type": "ImageObject", ... }
  ]
}
</script>
```

Output forms: embedded HTML (paste into `<head>` or before `</body>`), standalone
JSON (CMS schema field / API injection), or an MDX component if the project uses
MDX. Recommend the user verify the result in Google's Rich Results Test or the
Schema Markup Validator — those tools check live eligibility; this skill checks
structure.
