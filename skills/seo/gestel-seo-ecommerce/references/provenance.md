<!-- Generated for the gestel-seo-ecommerce active-skill migration -->
<!-- Sources: references/source-repos/MANIFEST.md, source path listed below -->
<!-- Used by: gestel-seo-ecommerce -->

# Provenance

This skill is a local standardization of license-compatible source material. It
is self-contained: all methodology lives in this skill's own `SKILL.md` and local
`references/*.md`, and the skill works if the top-level `references/` tree is
deleted. This file is a provenance note only — nothing here is a runtime
dependency. The skill does not copy provider credentials, the DataForSEO Merchant
API connection, the upstream helper scripts, or any installer.

## Source Map

- Source path: `references/skills/claude-seo/skills/seo-ecommerce/SKILL.md`
- Upstream path: `references/source-repos/claude-seo/skills/seo-ecommerce/SKILL.md`
- Commit: `d830cdb2ad339bb7f062339fe82228b072e98061`
- License: MIT (`references/source-repos/claude-seo/LICENSE`; source skill ships
  its own `LICENSE.txt`, © 2026 AgriciDaniel, <https://github.com/AgriciDaniel/claude-seo>;
  original author credit: Matej Marjanovic, Pro Hub Challenge)
- Copied support docs (filenames preserved):
  - `references/marketplace-endpoints.md` — DataForSEO Merchant API endpoint,
    parameter, response-field, task/poll, rate-limit, and normalization tables.
  - `references/ucp-universal-commerce-protocol.md` — UCP audit criteria, profile
    shape, capability IDs, AP2 relationship, and audit posture tiers.
  - (Source had no `evals/` directory to copy.)

### Related source commits (provenance only, no runtime dependency)

- claude-ads: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- claude-blog: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- claude-seo: `d830cdb2ad339bb7f062339fe82228b072e98061`
- marketingskills: `8bfcdffb655f16e713940cd04fb08891899c47db`

## Local Changes

- Converted the source into a project-local skill with trigger-focused
  frontmatter and a two-mode loop (local audit vs. costed marketplace spec).
- Converted the paid **DataForSEO Merchant API** dependency and the upstream
  helper scripts — `scripts/render_page.py`, `scripts/parse_html.py`,
  `scripts/dataforseo_merchant.py`, `scripts/dataforseo_normalize.py`,
  `scripts/dataforseo_costs.py` (cost meter), and `scripts/ucp_check.py` — into
  Boundaries. None are inlined or assumed present; live execution routes to the
  user's own adapter or to user-supplied exports. This deferral reason
  (missing-runtime) is now an explicit Boundary.
- Migrated the full portable methodology into `SKILL.md`: the product on-page
  checklist and weighted scoring, the Product schema required/recommended fields,
  the seven validation rules and the schema scoring ladder, the marketplace
  pricing/seller/listing analysis frameworks, the cross-marketplace comparison,
  the organic-vs-Shopping keyword-gap typology, the UCP readiness audit, the
  cross-skill routing, the error/degradation handling, and the report template.
- Copied the deep DataForSEO Merchant endpoint tables and the UCP audit reference
  locally so the skill works after the top-level `references/` tree is deleted,
  and linked them from `SKILL.md`.
- Reframed all per-call costs, rate limits, schema requirements, and UCP spec
  details as dated snapshots requiring live verification; replaced the live cost
  meter with planning-only cost disclosure.
- Added explicit data-source labeling, freshness honesty, and untrusted-data
  handling consistent with other GESTEL skills.
- Preserved the source as reference material rather than executable instructions.
