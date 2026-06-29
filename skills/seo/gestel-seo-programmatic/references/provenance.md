<!-- Generated for the gestel-seo-programmatic active-skill migration -->
<!-- Sources: references/source-repos/MANIFEST.md, source path listed below -->
<!-- Used by: gestel-seo-programmatic -->

# Provenance

This skill is a local standardization of license-compatible source material. It is
self-contained: all methodology lives in this skill's own `SKILL.md`, and the skill
works if the top-level `references/` tree is deleted. This file is a provenance note
only — nothing here is a runtime dependency. The skill does not copy provider
credentials, a paid data connection, any upstream scraper/generator script, or an
installer.

## Source Map

- Source path: `references/skills/claude-seo/skills/seo-programmatic/SKILL.md`
- Upstream path: `references/source-repos/claude-seo/skills/seo-programmatic/SKILL.md`
- Commit: `d830cdb2ad339bb7f062339fe82228b072e98061`
- License: MIT (`references/source-repos/claude-seo/LICENSE`; source skill ships its
  own `LICENSE.txt`, © 2026 AgriciDaniel, <https://github.com/AgriciDaniel/claude-seo>)
- Copied support docs (filenames preserved): none — the source skill directory
  contained only `SKILL.md` and `LICENSE.txt`; it had no `references/` or `evals/`
  directory to copy. All portable methodology was distilled into this skill's
  `SKILL.md`.

### Related source commits (provenance only, no runtime dependency)

- claude-ads: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- claude-blog: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- claude-seo: `d830cdb2ad339bb7f062339fe82228b072e98061`
- marketingskills: `8bfcdffb655f16e713940cd04fb08891899c47db`

## Local Changes

- Converted the source into a project-local skill with trigger-focused frontmatter,
  a two-mode loop (plan a set vs. audit an existing set), and explicit near-miss
  routing to other gestel-seo / gestel-content skills.
- Migrated the full portable methodology into `SKILL.md`: the data-source
  assessment and duplicate/near-duplicate flagging, the template-engine planning
  (static vs. dynamic blocks, injection points, conditional logic, supplementary
  value) and review checklist, the URL pattern catalog and URL rules, the
  internal-linking automation model (hub/spoke, related items, breadcrumbs,
  cross-linking, anchor/density), the thin-content quality-gate table and the
  uniqueness-percentage calculation, the standalone-value test, the safe-vs-penalty
  page-type lists, the progressive-rollout discipline, and the canonical / sitemap /
  index-bloat policy.
- Converted the deferral reason (live-research / freshness-sensitive platform-policy
  facts) into an explicit Boundary. The source's dated, specific claims about
  Google's Scaled Content Abuse and site-reputation-abuse enforcement history —
  named spam updates, dated penalty waves, claimed percentage reductions, exact
  effective dates — are no longer asserted as current fact; they are flagged as
  freshness-sensitive and routed to the user's dated research or a live lookup. The
  stable gates and thresholds are retained as methodology.
- Converted everything implying live execution (connecting to APIs/DBs, Search
  Console pulls, paid keyword/SERP data, bulk page generation, CMS/sitemap
  publishing) into Boundaries and cross-skill routes. No credentials, paid
  providers, or upstream scripts are inlined or assumed present.
- Added explicit data-source labeling, freshness honesty, untrusted-data handling,
  and an Output Contract consistent with other GESTEL skills.
