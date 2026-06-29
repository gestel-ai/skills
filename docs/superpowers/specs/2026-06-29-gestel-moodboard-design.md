# Design: `gestel-moodboard` skill

**Date:** 2026-06-29
**Status:** Approved (design), pending spec review
**Repo:** `gestel-ai/skills` (this repository)

## Problem & motivation

The repo at `github.com/choandahn/brand-moodboard-prompt-pipeline` distills a
high-value methodology: reverse-engineer a brand's photo library into a reusable
**visual DNA moodboard** + per-category scene templates, then drop any new
product into those templates to get on-brand image-generation prompts.

The "product → on-brand image prompts" half is **already covered** by the
existing `gestel-ads-photoshoot` skill (5 ad photography styles, brand-DNA
injection, platform safe zones). Building another product→prompts skill would
duplicate it.

The genuinely missing piece — confirmed by surveying all 10 existing
image/visual GESTEL skills — is the **moodboard / brand visual DNA builder**.
No current skill turns a set of reference images into a reusable visual DNA +
scene-template artifact. That artifact is the natural *input* to the existing
prompt-generation skills, which today only read the lightweight textual
`gestel-brand-snapshot` and have no visual scene-template layer.

`gestel-moodboard` fills that gap.

## Non-goals

- No actual image rendering; no paid image-provider calls.
- No heavy vision pipeline (the source repo cataloged ~590 images at ~2M
  tokens via custom Python + Workflow scripts — **out of scope**; this skill is
  self-contained and reasoning-only over a small curated set).
- No product→45-prompt generation (that is `gestel-ads-photoshoot` /
  `gestel-image`'s job — this skill produces the *templates* they consume).
- No account mutation.

## Skill identity

- **Path:** `skills/media/gestel-moodboard/`
- **Name (frontmatter):** `gestel-moodboard`
- **Category:** `media` (alongside `gestel-image`, `gestel-video`)
- **Trigger:** user wants to build/define a brand's visual moodboard or visual
  DNA, provides a set of brand reference images and asks to "organize our visual
  tone", or wants reusable per-category scene templates so new products can be
  dropped in for on-brand shots.

## Input (intake)

- **Required:** a curated set of reference images (recommended ~10–40), read
  directly by the model's vision — no catalog pipeline.
- **Optional:** brand name / product type / one-line positioning. If a
  `gestel-brand-snapshot` exists, read it to absorb colors, voice, and
  banned/approved expressions.
- If the reference set is too thin or incoherent to generalize from, say so and
  request more or narrow the scope — do not over-generalize from 2–3 images.

## Processing (4 stages, all model reasoning)

1. **Catalog** — tag each reference: product type, backdrop, lighting,
   composition, model presence, mood.
2. **Synthesize visual DNA** — derive the color system (Hex), signature motifs,
   and brand-wide photography principles (photorealism, white balance, lens
   conventions, negative space).
3. **Derive categories** — start from a default 9-slot taxonomy (Hero-white,
   Product-card, Macro, Editorial-light/neutral/dark, Flatlay, Lifestyle,
   Conceptual-prop) as a **starting point**; adopt/prune to what the set
   actually contains and adapt labels to the product type (jewelry, candle,
   apparel, SaaS UI, etc.). The category set is adaptive, not hard-fixed.
4. **Templatize scenes** — for each adopted category, write a reusable scene
   template with fixed backdrop/lighting/camera/grading/logo plus `{PRODUCT}` /
   `{PRODUCT_LABEL}` slots.

## Outputs

1. **`BRAND_MOODBOARD.md`** — human-readable visual DNA: color system, signature
   motifs, photography principles, category summary.
2. **Scene templates** — per-category reusable templates with `{PRODUCT}` slots
   (the bridge downstream skills expand).
3. **`moodboard.json`** — machine-readable: color palette, categories,
   templates, taxonomy. Schema designed so `gestel-ads-photoshoot` and
   `gestel-image` can consume it.
4. **Product-fidelity guard** (shipped as a reference, applied at hand-off time):
   the anti-distortion product-description discipline (a name is a name not a
   shape; a reflection is not a carved feature; silhouette geometry precision;
   an explicit geometry/anti-distortion guard) so that when a product is later
   dropped into a template the image does not break.

**Output location:** the skill writes the three artifacts to a brand-scoped
folder in the user's working directory — default `moodboard/<brand>/`
(`BRAND_MOODBOARD.md`, `moodboard.json`, and the scene templates) — or to a path
the user specifies. The skill never writes inside its own skill folder.

## Downstream integration

- `moodboard.json` + templates → consumed by `gestel-ads-photoshoot` /
  `gestel-image` as a **visual scene layer** (today they only have textual brand
  context).
- Complementary to `gestel-brand-snapshot`: snapshot = textual brand context;
  moodboard = visual scene DNA.

## Boundaries / safety

- Reference images are treated as **untrusted data**, never as instructions.
- Reasoning-only over a small curated set; explicitly not the 2M-token pipeline.
- No rendering, no paid providers, no account mutation. Planning/spec skill,
  consistent with other `gestel-*` skills.

## Key design decisions (approved)

1. **9 categories are a starting point + adaptation**, not a hard-fixed set —
   the skill prunes/relabels to fit the brand and product type.
2. **Product-fidelity guard is a reference inside this skill**, not a separate
   skill — it is a hand-off-time sub-step, and a standalone skill would risk
   overlap with `gestel-ads-photoshoot`.

## File layout (matches `gestel-*` conventions)

```text
skills/media/gestel-moodboard/
  SKILL.md                      # ~150-200 lines, procedural
  references/
    moodboard-method.md         # the 4-stage analysis method
    category-taxonomy.md        # default 9 slots + product-type adaptation rules
    scene-template-spec.md      # template structure + {PRODUCT} slot contract
    product-fidelity-guard.md   # anti-distortion product-description discipline
    moodboard-json-schema.md    # moodboard.json schema
    provenance.md               # source repo + commit attribution
    source-usage.md             # license/attribution notes
  evals/
    evals.json                  # trigger + behavior evals (skill_name: gestel-moodboard)
    promptfooconfig.yaml        # generated by scripts/promptfoo_skill_evals.py
```

## Validation (must pass before merge)

- Manifest: `gestel-moodboard` added to `.claude-plugin/plugin.json` (→ 121) and
  `skills.sh.json` (Media grouping); every path resolves.
- `markdownlint-cli2 'skills/**/*.md'` → 0 errors.
- `promptfoo_skill_evals.py --check` → current.
- Self-containment grep → 0 non-provenance runtime deps on `reference/`.
- `SKILL.md` frontmatter parses (line 1 `---`; description ≤1024 chars, no `<>`,
  no unquoted colon-space; only allowed keys).
- `npx skills use . --skill gestel-moodboard` resolves.

## Provenance

Methodology distilled from `github.com/choandahn/brand-moodboard-prompt-pipeline`
(`engine/shared/PRODUCT_SPEC_GUIDE.md`, `GENERATOR.md`, `LESSONS.md`, the
9-category taxonomy, and `brands/jgracelet/` worked example). MIT-licensed.
