# GESTEL Skills

Public agent skills for pragmatic product engineering.

This repository follows the Vercel Labs `skills` CLI layout:

```text
.claude-plugin/
  plugin.json
skills/
  product-engineering/
    SKILL.md
skills.sh.json
```

It supports both conventional skill discovery and plugin manifest discovery.

## Skills

### product-engineering

Guidance for building, reviewing, and refactoring application code with small
reversible changes, boring technology, simple architecture, semantic HTML, and
practical tests.

Use it when maintainability, delivery speed, and operational risk matter.

## Install

Install or inspect this repository with:

```bash
npx skills add https://github.com/gestel-ai/skills --list
npx skills add https://github.com/gestel-ai/skills --skill product-engineering
```

You can also use the skill without installing it:

```bash
npx skills use https://github.com/gestel-ai/skills --skill product-engineering
```

## Local Validation

Run these checks before publishing changes:

```bash
npx skills add . --list
npx skills use . --skill product-engineering >/tmp/product-engineering.txt
```

The first command verifies that the repository is discoverable by the Vercel
Labs `skills` CLI. The second verifies that the skill can be resolved into an
agent prompt.
