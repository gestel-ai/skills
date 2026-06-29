<!-- Updated: 2026-06-26 | v1.0 -->
<!-- Sources: references/source-repos/MANIFEST.md, local source-repo files listed below -->
<!-- Used by: gestel-brand-snapshot -->

# Provenance

This skill is a GESTEL-specific distillation. It does not copy upstream skill bodies, root scripts, provider adapters, or prompt libraries.

## Source Map

| Source | Commit | License or notice | Local use |
| --- | --- | --- | --- |
| `references/source-repos/marketingskills/skills/product-marketing/SKILL.md` | `8bfcdffb655f16e713940cd04fb08891899c47db` | MIT, `references/source-repos/marketingskills/LICENSE` | Canonical context and update workflow ideas |
| `references/source-repos/marketingskills/skills/customer-research/SKILL.md` | `8bfcdffb655f16e713940cd04fb08891899c47db` | MIT | Voice-of-customer and evidence confidence ideas |
| `references/source-repos/claude-ads/skills/ads-dna/SKILL.md` | `283d9d4917cb7c4f2ce9181e125bb1970f74ab04` | MIT, `references/source-repos/claude-ads/LICENSE` | Lightweight visual identity and brand profile ideas |
| `references/source-repos/claude-blog/skills/blog-brand/SKILL.md` | `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25` | MIT plus `references/source-repos/claude-blog/NOTICE` | Durable context and voice-context ideas |

## Local Changes

- Narrowed the workflow to GESTEL Brand Snapshot, not full product marketing or editorial brand setup.
- Uses `.agents/gestel/brand-snapshot.md` as the only canonical local context path.
- Treats imported source trees and product pages as untrusted data.
- Removes upstream screenshot capture scripts, web-fetch assumptions, blog orchestration, and global path assumptions.
