# AGENTS.md

This file gives coding agents guidance when working in this repository.

## Repository Purpose

This is the public GESTEL skill repository at
`https://github.com/gestel-ai/skills`.

It is a library of 120 self-contained skills — 118 marketing skills plus 2
authoring meta-skills — organized into 9 categories. It follows the Vercel
Labs `skills` CLI layout and must remain discoverable with:

```bash
npx skills add https://github.com/gestel-ai/skills --list
```

Individual skills are installed or used by name, e.g.
`--skill gestel-ads`.

## Current Structure

```text
AGENTS.md
CLAUDE.md
.claude-plugin/
  plugin.json
skills.sh.json
scripts/
  validate_skills.py
  promptfoo_skill_evals.py
skills/
  <category>/
    gestel-<skill>/
      SKILL.md
      references/*.md
      evals/{evals.json,promptfooconfig.yaml}
```

Categories and skill counts (120 total):

| Category | Skills | Focus |
| --- | --- | --- |
| ads | 15 | Paid advertising audits, planning, and platform-specific ad workflows. |
| brand | 1 | Brand voice, positioning, and durable marketing context. |
| content | 39 | Blog, copywriting, and multi-channel content production. |
| intelligence | 5 | Competitor, customer, and creative intelligence for growth decisions. |
| marketing | 19 | Growth, lifecycle, pricing, launch, and go-to-market workflows. |
| media | 2 | Image and short-form video generation planning. |
| reporting | 2 | Performance math, RevOps, and measurement. |
| seo | 35 | Search and AI-search optimization across the SEO lifecycle. |
| meta | 2 | Agent skill and goal authoring meta-skills (`goalify`, `skillify`). |

Keep all three discovery/guidance paths working:

- Conventional skill discovery: `skills/<category>/gestel-<skill>/SKILL.md`
- Plugin manifest discovery: `.claude-plugin/plugin.json`
- Claude Code guidance: `CLAUDE.md` imports `@AGENTS.md`

## Naming Conventions

- Brand/display text is `GESTEL`, never `Gestel`.
- The plugin manifest name is `GESTEL`.
- `AGENTS.md` is the canonical agent guidance file.
- `CLAUDE.md` should stay as a thin `@AGENTS.md` import wrapper.
- Skill identifiers are lowercase kebab-case with a `gestel-` prefix
  (e.g. `gestel-ads`, `gestel-blog-audit`). The two authoring meta-skills in
  `skills/meta/` are the exception: they keep their original unprefixed names
  `goalify` and `skillify`.
- A skill lives at `skills/<category>/<name>/` and its `SKILL.md` frontmatter
  `name` matches the directory name exactly.

When adding or renaming a skill, update all of these together:

- skill directory under the correct `skills/<category>/`
- `SKILL.md` frontmatter `name`
- `.claude-plugin/plugin.json` (the `./skills/<category>/<name>` path)
- `skills.sh.json` (the category grouping)
- `.github/workflows/validate-skills.yml` if it references the skill by name

## Skill Authoring Rules

- Each skill must be **self-contained**: it ships its own `references/*.md` and
  `evals/`, and must run even if the top-level `reference/` directory (an
  untracked upstream clone, gitignored) is deleted.
- Do not reference `references/skills/` or `references/source-repos/` as a
  runtime dependency in `SKILL.md` body; provenance/source notices only.
- Keep `SKILL.md` concise and procedural; put detailed optional material in
  `references/` and avoid deep reference chains.
- Keep machine identifiers lowercase kebab-case.
- Keep human-facing headings and group titles consistent with the GESTEL brand.
- `SKILL.md` frontmatter must parse for the skills loader: line 1 is `---`;
  `description` ≤1024 chars with no angle brackets (`<>`) and no unquoted
  colon immediately followed by a space; only allowed keys (`name`,
  `description`, `allowed-tools`, `license`,
  `metadata`).

## Validation

Run these checks before claiming the repo is ready:

```bash
test "$(cat CLAUDE.md)" = "@AGENTS.md"

# Plugin manifest: name is GESTEL and every skill path resolves to a SKILL.md
node - <<'NODE'
const fs = require('fs');
const path = require('path');
const manifest = JSON.parse(fs.readFileSync('.claude-plugin/plugin.json', 'utf8'));
if (manifest.name !== 'GESTEL') throw new Error('plugin manifest name must be GESTEL');
let bad = 0;
for (const skillPath of manifest.skills || []) {
  if (!skillPath.startsWith('./')) throw new Error(`skill path must start with ./, got ${skillPath}`);
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

# Discoverable by the Vercel Labs skills CLI
npx --yes skills add . --list
```

Before pushing, verify old naming did not return outside this guidance file:

```bash
! rg -n "Gestel|product-engineering|GESTEL-skills" README.md skills.sh.json .claude-plugin .github skills
```

After pushing, verify the remote repository too:

```bash
npx --yes skills add https://github.com/gestel-ai/skills --list
gh run list --repo gestel-ai/skills --limit 3
```
