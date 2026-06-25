# AGENTS.md

This file gives coding agents guidance when working in this repository.

## Repository Purpose

This is the public GESTEL skill repository at
`https://github.com/gestel-ai/skills`.

It follows the Vercel Labs `skills` CLI layout and must remain installable with:

```bash
npx skills add https://github.com/gestel-ai/skills --skill product-engineering
```

## Current Structure

```text
AGENTS.md
CLAUDE.md
.claude-plugin/
  plugin.json
skills/
  product-engineering/
    SKILL.md
skills.sh.json
```

Keep both discovery paths working:

- Conventional skill discovery: `skills/product-engineering/SKILL.md`
- Plugin manifest discovery: `.claude-plugin/plugin.json`
- Claude Code guidance: `CLAUDE.md` imports `@AGENTS.md`

## Naming Conventions

- Brand/display text is `GESTEL`, never `Gestel`.
- The plugin manifest name is `GESTEL`.
- `AGENTS.md` is the canonical agent guidance file.
- `CLAUDE.md` should stay as a thin `@AGENTS.md` import wrapper.
- The public skill identifier is `product-engineering`.
- The skill directory is `skills/product-engineering/`.
- The `SKILL.md` frontmatter `name` is `product-engineering`.
- Do not reintroduce `gestel-product-engineering` unless the public install
  name is intentionally changed.

When renaming a skill, update all of these together:

- skill directory
- `SKILL.md` frontmatter `name`
- `.claude-plugin/plugin.json`
- `skills.sh.json`
- README install and validation examples
- `.github/workflows/validate-skills.yml`

## Skill Authoring Rules

- Keep `SKILL.md` concise and procedural.
- Put detailed optional material in `references/`, scripts in `scripts/`, and
  reusable output assets in `assets/` only when they are actually needed.
- Keep reference files linked directly from `SKILL.md`; avoid deep reference
  chains.
- Do not add extra docs inside a skill folder unless they directly support skill
  execution.
- Keep machine identifiers lowercase kebab-case.
- Keep human-facing headings and group titles consistent with the GESTEL brand.

## Validation

Run these checks before claiming the repo is ready:

```bash
test "$(cat CLAUDE.md)" = "@AGENTS.md"

node - <<'NODE'
const fs = require('fs');
const path = require('path');
const manifest = JSON.parse(fs.readFileSync('.claude-plugin/plugin.json', 'utf8'));
if (manifest.name !== 'GESTEL') throw new Error('plugin manifest name must be GESTEL');
for (const skillPath of manifest.skills || []) {
  if (!skillPath.startsWith('./')) throw new Error(`skill path must start with ./, got ${skillPath}`);
  const skillFile = path.join(skillPath, 'SKILL.md');
  if (!fs.existsSync(skillFile)) throw new Error(`missing ${skillFile}`);
}
NODE

npx --yes skills add . --list
npx --yes skills use . --skill product-engineering >/tmp/product-engineering.txt
curl -fsSL https://skills.sh/schemas/skills.sh.schema.json -o /tmp/skills.sh.schema.json
npx --yes ajv-cli@latest validate --spec=draft2020 --strict=false -s /tmp/skills.sh.schema.json -d skills.sh.json
```

Before pushing, also verify old naming did not return outside this guidance
file:

```bash
! rg -n "Gestel|gestel-product-engineering|GESTEL-skills" README.md skills.sh.json .claude-plugin .github skills
```

After pushing, verify the remote repository too:

```bash
npx --yes skills add https://github.com/gestel-ai/skills --list
gh run list --repo gestel-ai/skills --limit 3
```
