<!-- Local support doc for gestel-blog-chart. -->
<!-- Distilled from claude-blog blog-chart SKILL.md and blog/references/visual-media.md -->
<!-- Upstream commit 49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25, MIT. Reference only, not runtime instructions. -->

# Chart Styling, Construction, and QA Reference

Deep reference for hand-authoring dark-mode-compatible inline SVG charts for
blog posts. All techniques here are plain SVG/JSX markup an agent can write
directly from user-provided data — no scripts, libraries, providers, or
credentials are required or assumed.

## Styling Rules (Non-Negotiable)

Every chart must render correctly on both dark and light backgrounds. Drive all
ink off `currentColor` and never paint a background on the root SVG.

```text
Text elements:     fill="currentColor"
Grid lines:        stroke="currentColor" opacity="0.08"
Axis lines:        stroke="currentColor" opacity="0.3"
Background:        transparent (no fill on root SVG)
Subtitle text:     fill="currentColor" opacity="0.45"
Source text:       fill="currentColor" opacity="0.35"
Label text:        fill="currentColor" opacity="0.8"
```

### Color Palette (works on dark and light)

| Color | Hex | Use Case |
|-------|-----|----------|
| Orange | `#f97316` | Primary / highest value |
| Sky Blue | `#38bdf8` | Secondary / comparison |
| Purple | `#a78bfa` | Tertiary / special category |
| Green | `#22c55e` | Quaternary / positive indicator |

For text placed inside a colored shape: `fill="white"` with `fontWeight="800"`.

## Standard SVG Shell (HTML)

```xml
<svg
  viewBox="0 0 560 380"
  style="max-width: 100%; height: auto; font-family: 'Inter', system-ui, sans-serif"
  role="img"
  aria-label="Chart description with key data point"
>
  <title>Chart Title</title>
  <desc>Description for screen readers with all key data points and source</desc>

  <!-- Chart content -->

  <text x="280" y="372" text-anchor="middle" font-size="10" fill="currentColor" opacity="0.35">
    Source: Source Name (Year)
  </text>
</svg>
```

## JSX/MDX Shell (camelCase attributes)

```jsx
<svg
  viewBox="0 0 560 380"
  style={{maxWidth: '100%', height: 'auto', fontFamily: "'Inter', system-ui, sans-serif"}}
  role="img"
  aria-label="Chart description"
>
  <title>Chart Title</title>
  <desc>Description for screen readers</desc>

  {/* Chart content */}

  <text x="280" y="372" textAnchor="middle" fontSize="10" fill="currentColor" opacity="0.35">
    Source: Source Name (Year)
  </text>
</svg>
```

## JSX Attribute Conversion (Required for MDX)

| HTML | JSX |
|------|-----|
| `stroke-width` | `strokeWidth` |
| `stroke-dasharray` | `strokeDasharray` |
| `stroke-linecap` | `strokeLinecap` |
| `text-anchor` | `textAnchor` |
| `font-size` | `fontSize` |
| `font-weight` | `fontWeight` |
| `font-family` | `fontFamily` |
| `class` | `className` |
| `style="..."` | `style={{...}}` |

## Chart Type Construction

### Horizontal Bar Chart

Best for: percentage improvements, single-metric comparisons.

1. Chart area: x=80, y=40, width=440, height=280.
2. Bar height: `chartHeight / dataCount - gap` (gap=8).
3. Bar width: `(value / maxValue) * chartWidth`.
4. Position: `y = chartY + index * (barHeight + gap)`.
5. Category label right-aligned at x=75; value label at the bar end.
6. Source text centered at the bottom.

### Grouped Bar Chart

Best for: before/after, A vs B comparisons.

1. Groups along the Y axis, bars within each group.
2. Two colors (primary + secondary) for the two series.
3. Legend at top: colored square + label per series.
4. Gap between groups > gap within groups.

### Donut Chart

Best for: parts of whole, market share.

1. Center cx=280, cy=180, outer radius=140, inner radius=80.
2. Compute arc segments from cumulative angles.
3. Each segment: `<path d="M... A... L... A... Z" fill="color" />`.
4. Center text: total or key label.
5. Legend below: color squares + labels + values.

### Line Chart

Best for: trends over time.

1. X axis: evenly spaced time periods.
2. Y axis: value range with 4-5 grid lines.
3. Grid lines: `stroke="currentColor" opacity="0.08"`.
4. Points: `<circle cx=... cy=... r="4" fill="color" />`.
5. Connector: `<polyline points="..." fill="none" stroke="color" strokeWidth="2" />`.
6. Optional area fill below the line at `opacity="0.1"`.

### Lollipop Chart

Best for: ranked factors, correlations.

1. Horizontal orientation (bar-like, but ending in a circle).
2. Thin stem: `stroke="currentColor" opacity="0.15" strokeWidth="1"`.
3. Marker: `<circle r="6">` with fill color.
4. Value label beside the circle; categories left-aligned on the Y axis.

### Area Chart

Best for: distribution, cumulative data.

1. Like a line chart with a filled region below.
2. Area: `<path d="M... L... L... Z" fill="color" opacity="0.15" />`.
3. Line on top: `stroke="color" strokeWidth="2" fill="none"`.
4. Grid lines drawn behind the area.

### Radar Chart

Best for: multi-dimensional scoring (5-7 axes).

1. Center cx=280, cy=190.
2. Concentric grid polygons (3-4 levels).
3. Axis endpoints at equal angles.
4. Plot each value proportionally along its axis.
5. Connect points: `fill="color" opacity="0.2" stroke="color"`.
6. Label each axis at the outer edge.

## Output Format (Wrap Every Chart)

**HTML:**

```html
<figure>
  <svg viewBox="0 0 560 380" style="max-width: 100%; height: auto; font-family: 'Inter', system-ui, sans-serif" role="img" aria-label="[description]">
    <title>[Chart Title]</title>
    <desc>[Full description with data points for screen readers]</desc>
    <!-- chart content -->
    <text x="280" y="372" text-anchor="middle" font-size="10" fill="currentColor" opacity="0.35">
      Source: [Source Name] ([Year])
    </text>
  </svg>
</figure>
```

**MDX:**

```mdx
<figure className="chart-container" style={{margin: '2.5rem 0', textAlign: 'center', padding: '1.5rem', borderRadius: '12px'}}>
  <svg viewBox="0 0 560 380" style={{maxWidth: '100%', height: 'auto', fontFamily: "'Inter', system-ui, sans-serif"}} role="img" aria-label="[description]">
    <title>[Chart Title]</title>
    <desc>[Full description]</desc>
    {/* chart content with camelCase attributes */}
    <text x="280" y="372" textAnchor="middle" fontSize="10" fill="currentColor" opacity="0.35">
      Source: [Source Name] ([Year])
    </text>
  </svg>
</figure>
```

## Common Pitfalls

| Mistake | Impact | Fix |
|---------|--------|-----|
| `fill="#111827"` on text | Invisible in dark mode | Use `fill="currentColor"` |
| `rect fill="white"` background | Bright flash in dark mode | Remove or make transparent |
| `stroke-width` in MDX | Compilation error | Use `strokeWidth` |
| `class` in MDX | Compilation error | Use `className` |
| Same chart type twice in a post | Visual monotony | Enforce chart-type diversity |
| No `role="img"` | Accessibility failure | Always include |
| No source attribution | Trust issue | Always cite the data source |

## Quality Checklist (Verify Before Returning)

- [ ] No hardcoded text colors (all `currentColor`).
- [ ] No white/light backgrounds (transparent or none).
- [ ] Source attribution text present at the bottom.
- [ ] `role="img"` and `aria-label` present on `<svg>`.
- [ ] `<title>` and `<desc>` present inside `<svg>`.
- [ ] Chart type not already used in this post.
- [ ] If MDX: all attributes camelCased (no hyphens in attribute names).
- [ ] Data values match the source data exactly (no invented numbers).
- [ ] Only approved palette colors used.
- [ ] ViewBox is `0 0 560 380` (standard) or a justified alternative.
