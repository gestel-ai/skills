<!-- Used by: gestel-moodboard -->

# Category Taxonomy — default 9 slots + adaptation rules

The category set is **adaptive**. The default 9 slots are a *starting point*, not
a fixed schema. Adopt the ones the reference set actually contains, prune the
ones it does not, and relabel to the product type.

## Default 9-slot taxonomy

| Slot | Intent | Typical signals |
| --- | --- | --- |
| `hero-white` | Clean seamless-white hero packshot | White/seamless backdrop, even light, product centered |
| `product-card` | Catalog/e-commerce card shot | Neutral backdrop, 3/4 angle, soft shadow, crisp detail |
| `macro` | Close-up texture/detail | Tight crop, shallow depth of field, material focus |
| `editorial-light` | Bright editorial scene | Airy daylight, soft props, generous negative space |
| `editorial-neutral` | Mid-tone editorial scene | Neutral/stone palette, balanced contrast |
| `editorial-dark` | Moody editorial scene | Dark backdrop, directional light, high contrast |
| `flatlay` | Top-down arranged composition | Overhead view, props fanned with intentional spacing |
| `lifestyle` | In-context aspirational scene | Environment, implied use, product as hero in a scene |
| `conceptual-prop` | Stylized concept with props | Sculptural staging, color blocking, art-directed |

## Adaptation rules

1. **Adopt only what the set supports.** A category needs at least one or two
   catalog rows behind it. Do not adopt a slot the brand never shoots.
2. **Prune empties.** If the set has no dark editorial frames, drop
   `editorial-dark`. A 5-category moodboard for a tight brand is healthier than a
   padded 9.
3. **Relabel to the product type.** Rename slots to the brand's language —
   jewelry "macro" might become `gemstone-macro`; SaaS UI might replace
   `flatlay` with `dashboard-grid`; apparel might add `on-model` distinct from
   `lifestyle`.
4. **Split or merge when the evidence says so.** If the set clearly has two
   distinct white-hero looks, split them; if `editorial-light` and
   `editorial-neutral` are indistinguishable in this set, merge them.
5. **Add net-new categories** the default list misses when a recurring look has
   no home (e.g. `ingredient-flatlay` for beauty, `texture-swatch` for textiles).
6. **Keep labels lowercase kebab-case** so they map cleanly into `moodboard.json`
   category keys.

## Product-type starting hints

- **Jewelry / watches** — favor `macro`, `hero-white`, `conceptual-prop`,
  `lifestyle` (on-wrist/on-hand).
- **Candles / home / beauty** — favor `editorial-*`, `flatlay`,
  `ingredient-flatlay`, `lifestyle`.
- **Apparel** — favor `on-model`, `lifestyle`, `product-card`, `flatlay`.
- **SaaS / digital UI** — replace photo slots with `hero-screen`,
  `dashboard-grid`, `feature-spot`, `in-context-device`.

These are hints, not rules. The catalog from Stage 1 is the authority on which
categories are real for this brand.
