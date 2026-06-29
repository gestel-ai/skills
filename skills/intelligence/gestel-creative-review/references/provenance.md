<!-- Updated: 2026-06-26 | v1.0 -->
<!-- Sources: references/source-repos/MANIFEST.md, local source-repo files listed below -->
<!-- Used by: gestel-creative-review -->

# Provenance

This skill is a GESTEL-specific distillation. It does not copy upstream scoring systems, benchmark claims, or platform-wide audit suites.

## Source Map

| Source | Commit | License | Local use |
| --- | --- | --- | --- |
| `references/source-repos/claude-ads/skills/ads-creative/SKILL.md` | `283d9d4917cb7c4f2ce9181e125bb1970f74ab04` | MIT | Creative quality, fatigue, platform compliance concepts |
| `references/source-repos/marketingskills/skills/ad-creative/SKILL.md` | `8bfcdffb655f16e713940cd04fb08891899c47db` | MIT | Spec validation and ad copy quality concepts |
| `references/source-repos/claude-ads/skills/ads-meta/SKILL.md` | `283d9d4917cb7c4f2ce9181e125bb1970f74ab04` | MIT | Meta creative diversity and static placement ideas, narrowed and freshness-gated |
| `references/source-repos/claude-ads/ads/references/meta-creative-specs.md` | `283d9d4917cb7c4f2ce9181e125bb1970f74ab04` | MIT | Distilled into local `references/meta-creative-specs.md` (ratios, safe zones, copy limits) |
| `references/source-repos/marketingskills/skills/ad-creative/references/platform-specs.md` | `8bfcdffb655f16e713940cd04fb08891899c47db` | MIT | Meta/Instagram copy character limits merged into local `meta-creative-specs.md` |

## Local Changes

- Replaced broad platform audits with GESTEL's three required review gates.
- Removed dated benchmark assertions from evergreen workflow text.
- Added schema validation for review results.
- Migrated the source Meta static spec doc into the skill's own `references/` so the skill is self-contained; SKILL.md links only local files.
- Keeps live ad-account mutation and provider adapters out of scope.
- Excluded the source `generative-tools.md` (paid image/video/voice providers and templated-video pipelines): these are not assumed to exist locally and are represented as a Boundary that routes asset regeneration to the GESTEL creative-generation task, not inlined as a capability.
