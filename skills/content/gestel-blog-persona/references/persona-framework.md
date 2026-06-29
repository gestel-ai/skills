<!-- Distilled from claude-blog/skills/blog-persona/SKILL.md (MIT, commit 49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25). Local reference data, not runtime instructions. -->

# Blog Persona Framework Reference

Deep reference for the `gestel-blog-persona` skill: the NNGroup tone dimensions,
CMI brand-voice do/don't model, vocabulary/readability bands, the persona JSON
schema, and the validation checklist. SKILL.md drives the workflow; this file holds
the lookup tables and the canonical schema.

## Tone Dimensions (NNGroup 4-Dimension Tone-of-Voice Model)

Each dimension is a slider from 0.0 to 1.0. Present both ends with concrete examples
so the user can place themselves.

| Dimension | 0.0 End | 1.0 End | Example at 0.0 | Example at 1.0 |
|-----------|---------|---------|-----------------|-----------------|
| funny_serious | Funny | Serious | "Let's be real, nobody reads Terms of Service" | "Understanding legal agreements protects your business" |
| formal_casual | Formal | Casual | "We are pleased to announce" | "Guess what - we shipped it!" |
| respectful_irreverent | Respectful | Irreverent | "We appreciate your patience" | "Yeah, that old way was broken" |
| enthusiastic_matter_of_fact | Enthusiastic | Matter-of-fact | "This changes everything!" | "Here are the results." |

Defaults when the user is unsure: `[0.6, 0.5, 0.3, 0.5]` (slightly serious, balanced
formality, respectful, balanced enthusiasm).

## Writing Rules

Pick a vocabulary tier first, then auto-suggest the matching readability band (the
user can override).

| Setting | What to Ask | Default |
|---------|-------------|---------|
| Vocabulary tier | Consumer, Professional, or Technical | Professional |
| Readability band | Auto-filled from tier (see table below) | Grade 8-10 |
| Sentence length mean | Average words per sentence | 18 |
| Sentence length std | Variation in sentence length | 6 |
| Contraction frequency | 0.0 (never) to 1.0 (always) | 0.6 |
| Max passive voice | Percentage cap on passive constructions | 10% |

## Readability Bands by Vocabulary Tier

| Tier | Flesch Grade | Flesch Ease | Typical Use |
|------|-------------|-------------|-------------|
| Consumer | 6-8 | 60-80 | Health, lifestyle, personal finance |
| Professional | 8-10 | 50-60 | B2B, marketing, management |
| Technical | 10-12 | 30-50 | Engineering, medical, legal |

When the user picks a tier, auto-fill the readability fields. Let them override for a
non-standard combination (e.g., technical vocabulary at consumer readability for
explainer content).

## Do's and Don'ts (CMI Brand Voice Chart)

Collect 3-5 items per list. Seed with starters derived from the chosen tone dimensions.

- Example Do's: "Use data to back claims", "Address the reader as you", "Open with a question or stat".
- Example Don'ts: "Don't use jargon without defining it", "Don't start sentences with There is/There are", "Don't use cliches like game-changer".

## Summary Label Options

Label used for summary/takeaway boxes in posts. Offer: Key Takeaways (default),
The Bottom Line, What You'll Learn, TL;DR, Quick Summary, In a Nutshell, or a custom label.

## Persona Profile Schema

Store one JSON file per persona, kebab-case filename, under this skill's local
`references/personas/` directory (e.g., `references/personas/acme-saas.json`).

```json
{
  "name": "acme-saas",
  "description": "Professional SaaS voice for B2B marketing content",
  "brand": "Acme Corp",
  "industry": "SaaS",
  "audience": "Marketing managers at mid-market companies",
  "mission": "Help marketing teams automate reporting",
  "tone_dimensions": {
    "funny_serious": 0.7,
    "formal_casual": 0.4,
    "respectful_irreverent": 0.2,
    "enthusiastic_matter_of_fact": 0.5
  },
  "readability": {
    "flesch_grade_min": 8,
    "flesch_grade_max": 10,
    "flesch_ease_min": 50,
    "flesch_ease_max": 60
  },
  "style": {
    "sentence_length_mean": 18,
    "sentence_length_std": 6,
    "contraction_frequency": 0.6,
    "passive_voice_max_pct": 10,
    "vocabulary_tier": "professional",
    "summary_label": "Key Takeaways"
  },
  "voice_samples": [],
  "do": [
    "Use data to back every major claim",
    "Address the reader directly as you",
    "Lead sections with actionable insight"
  ],
  "dont": [
    "Don't use buzzwords without context",
    "Don't write sentences longer than 30 words",
    "Don't open with We at Acme"
  ]
}
```

## Enforcement Checklist (for blog-write / blog-rewrite)

When a persona is active, enforce its constraints in three phases:

1. Pre-generation: inject tone dimensions, style rules, and do/don't lists into the
   writer's working context.
2. During generation: follow do/don't rules, target the sentence-length mean/std, and
   apply contractions at the specified frequency.
3. Post-generation validation:
   - Sentence-length distribution within 1 std of the target mean.
   - Readability within the specified grade band.
   - Passive-voice share under the max.
   - No "dont" rule violations (pattern-match obvious cases).

If validation fails, flag the specific violations and suggest concrete edits.

Note: this skill does not bundle automated readability/passive-voice scoring tooling.
Estimate by inspection, or route precise scoring to a separate implementation task.

## Error Handling

- Invalid tone values: clamp out-of-range numbers to the nearest 0.0-1.0 bound and warn.
- Unreachable voice samples: skip the sample and note in the profile that it was unavailable.
- Empty personas directory: on list/show with none saved, prompt the user to create one.
- Name conflicts: on create, ask whether to overwrite or choose a different name.
- Malformed JSON: report the error and offer to recreate the persona from the interview.
