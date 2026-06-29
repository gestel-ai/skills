# GESTEL Skills

Public agent skills for marketing — a library of 121 self-contained skills
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
| Media | 3 | Image, short-form video, and visual moodboard generation planning. |
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

Run the same core checks CI enforces before publishing changes. See the
"Validation" section of [AGENTS.md](AGENTS.md) for the full suite and expected
output.

```bash
# Agent guidance wrapper stays a thin import
test "$(cat CLAUDE.md)" = "@AGENTS.md"

# Plugin manifest is GESTEL and every skill path resolves (expect: OK <count>)
node - <<'NODE'
const fs = require('fs');
const path = require('path');
const manifest = JSON.parse(fs.readFileSync('.claude-plugin/plugin.json', 'utf8'));
if (manifest.name !== 'GESTEL') throw new Error('plugin manifest name must be GESTEL');
let bad = 0;
for (const skillPath of manifest.skills || []) {
  if (!fs.existsSync(path.join(skillPath, 'SKILL.md'))) { console.log('MISSING', skillPath); bad++; }
}
console.log(bad ? `FAIL ${bad}` : `OK ${manifest.skills.length}`);
NODE

# Markdown lint (expect 0 errors)
pnpm dlx markdownlint-cli2 'skills/**/*.md'

# Promptfoo eval configs are current
uv run scripts/promptfoo_skill_evals.py --check

# Self-containment: no non-provenance runtime deps on the upstream clone (expect 0)
grep -rn "references/skills/\|references/source-repos/" skills/**/SKILL.md \
  | grep -viE "distill|provenance|source path|upstream|notice|commit|licen|merged|narrowed|source map" \
  | wc -l

# Old naming has not returned (expect no output). The first letter of each
# token is bracketed so this command does not match its own appearance here.
rg -n "[G]estel|[p]roduct-engineering|[G]ESTEL-skills" README.md skills.sh.json .claude-plugin .github skills

# Discoverable by the Vercel Labs skills CLI
npx skills add . --list
```

The final command verifies that the repository is discoverable by the Vercel
Labs `skills` CLI and that every skill in the manifest resolves.
