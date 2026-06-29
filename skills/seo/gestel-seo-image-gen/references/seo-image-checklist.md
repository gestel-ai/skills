# SEO Image Post-Generation & Markup Checklist

> Load on-demand after a spec is built or an image file already exists.
> The markup shapes (ImageObject, og:image) are stable conventions, but exact
> required/recommended fields and platform dimensions are freshness-sensitive —
> verify against live schema.org and platform docs before asserting current rules.

## 1. Alt Text

Write descriptive, keyword-rich alt text for every asset:

- A full descriptive sentence (not a keyword list), ~10-125 characters.
- Use topic keywords naturally; describe what is shown AND its relevance.
- For charts/infographics, include the key data point.

Good: `Marketing team reviewing AI search citation metrics on a dashboard`
Bad: `seo ai marketing image optimization visual`

## 2. SEO-Friendly File Naming

Rename to a descriptive, hyphenated, lowercase pattern:

```text
keyword-description-WIDTHxHEIGHT.webp
e.g. ai-search-traffic-dashboard-1200x630.webp
```

Avoid `IMG_1234.png`, spaces, underscores, and stop-word noise.

## 3. WebP / AVIF Conversion (local, optional)

Only if an image file already exists AND ImageMagick 7 (`magick`, fallback `convert`)
is installed locally. Verify the binary exists first; this step transforms an existing
file and does not create images.

```bash
magick input.png -quality 85 output.webp                                          # WebP (~25-30% smaller than JPEG)
magick input.png -quality 80 output.avif                                          # AVIF (~50% smaller than WebP)
magick input.png -resize 1200x630^ -gravity center -extent 1200x630 og-image.png # OG-safe crop
magick input.png -strip output.png                                               # strip EXIF (keeps embedded SynthID/C2PA)
```

## 4. File Size Targets

Approximate budgets for page speed (confirm against current Core Web Vitals guidance):

- Hero images: under ~200KB (some sources push to ~500KB for full-bleed heroes).
- Inline images: under ~150KB.
- Thumbnails / favicons: under ~100KB.
Pick the resolution tier accordingly; do not ship 4K assets where 1K reads fine.

## 5. Schema Markup (ImageObject)

Suggest `ImageObject` schema pointing at the new asset:

```json
{
  "@type": "ImageObject",
  "url": "https://example.com/images/keyword-description.webp",
  "width": 1200,
  "height": 630,
  "caption": "Descriptive caption with target keyword"
}
```

Width/height must match the actual rendered pixels. Treat required vs recommended
fields as schema.org-version-dependent.

## 6. Open Graph & Social Meta Tags

For OG/social previews, remind the user to wire the meta tags:

```html
<meta property="og:image" content="https://example.com/images/og-image.webp" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:image:alt" content="Descriptive alt text" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:image" content="https://example.com/images/og-image.webp" />
```

The 1200x630 / `summary_large_image` conventions are widely used but
platform-controlled — verify current requirements before asserting them as fixed.

## 7. Content Credentials Awareness

Generated images may carry an invisible SynthID watermark (non-removable) and, on
some Pro tiers, C2PA Content Credentials. Use `-strip` to drop EXIF for size without
removing these. Disclose AI provenance where the publishing context requires it.

## Cross-Skill Handoffs

- Audit findings from `gestel-seo-audit` / image-audit work identify missing or
  low-quality OG/social/hero images — feed those into a generation plan here.
- After generation, `gestel-blog-schema` (or schema work) can consume the asset via
  the `ImageObject` snippet above.
- Brand presets/voice from `gestel-brand-snapshot` can constrain palette, style refs,
  and domain mode before constructing the brief.
