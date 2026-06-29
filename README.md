# GESTEL Skills

Public agent skills for marketing — a library of 120 self-contained skills
covering paid ads, content, SEO, brand, growth, and measurement, plus
authoring meta-skills.

This repository follows the Vercel Labs `skills` CLI layout and exposes the
skills through both conventional skill discovery and plugin manifest discovery.

## Skills

The library is organized into 9 categories:

| Category | Skills | Focus |
| --- | --- | --- |
| Ads | 15 | Paid advertising audits, planning, and platform-specific ad workflows. |
| Brand | 1 | Brand voice, positioning, and durable marketing context. |
| Content | 39 | Blog, copywriting, and multi-channel content production. |
| Intelligence | 5 | Competitor, customer, and creative intelligence for growth decisions. |
| Marketing | 19 | Growth, lifecycle, pricing, launch, and go-to-market workflows. |
| Media | 2 | Image and short-form video generation planning. |
| Reporting | 2 | Performance math, RevOps, and measurement. |
| SEO | 35 | Search and AI-search optimization across the SEO lifecycle. |
| Meta | 2 | Agent skill and goal authoring meta-skills (`goalify`, `skillify`). |

Each skill is self-contained: a procedural `SKILL.md` plus its own
`references/` support material and `evals/`. Skills do not depend on any
top-level clone of upstream source material to run.

## Install

Browse the full catalog, then install or use individual skills by name:

```bash
# List every skill in the library
npx skills add https://github.com/gestel-ai/skills --list

# Install a specific skill (replace with any name from --list)
npx skills add https://github.com/gestel-ai/skills --skill gestel-ads

# Use a skill without installing it
npx skills use https://github.com/gestel-ai/skills --skill gestel-ads
```

## Local Validation

Run these checks before publishing changes:

```bash
npx skills add . --list
```

This verifies that the repository is discoverable by the Vercel Labs `skills`
CLI and that every skill in the manifest resolves.
