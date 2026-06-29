<!-- Sources: references/source-repos/MANIFEST.md, source path listed below -->
<!-- Used by: gestel-schema -->

# Provenance

This skill is a local standardization of license-compatible source material. It does not copy upstream
runtime scripts, provider adapters, generated assets, or hidden credential assumptions.

## Source Map

- Source path: `references/skills/marketingskills/skills/schema/SKILL.md`
  - Upstream path: `references/source-repos/marketingskills/skills/schema/SKILL.md`
  - Commit: `8bfcdffb655f16e713940cd04fb08891899c47db`
  - License: MIT
  - Notice: `references/source-repos/marketingskills/NOTICE`
- Supporting reference copied (filename preserved):
  `references/skills/marketingskills/skills/schema/references/schema-examples.md`

## Local Changes

- Converted the source into a project-local skill (`gestel-schema`) with trigger-focused frontmatter
  (triggers, near-miss exclusions, and the no-credentials / no-paid-provider / no-live-mutation /
  no-upstream-scripts boundary inline).
- Distilled the source methodology (initial assessment, core principles, type-selection table,
  `@graph` linking, validation/testing, implementation patterns) into the SKILL body so the skill is
  self-contained.
- Copied the source's full JSON-LD example library to `references/schema-examples.md` (filename
  preserved) and linked it from SKILL.md.
- Isolated the source's freshness-sensitive rich-result/eligibility/policy claims into
  `references/freshness-and-policy.md` and converted the single "can't verify locally" gap (live Google
  rich-result support) into an explicit Boundary.
- Moved source-specific usage limits into `references/source-usage.md`.
- Preserved the source as reference material rather than executable instructions.

## Related Source Repo Commits (attribution only)

These commits are recorded for the broader migration manifest; this skill draws only from
`marketingskills`.

- `claude-ads`: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- `claude-blog`: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- `claude-seo`: `d830cdb2ad339bb7f062339fe82228b072e98061`
- `marketingskills`: `8bfcdffb655f16e713940cd04fb08891899c47db`

This file is an attribution record only; the skill does not depend on the top-level `references/` tree
to run.
