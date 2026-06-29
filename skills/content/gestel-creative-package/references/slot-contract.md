<!-- Updated: 2026-06-26 | v1.0 -->
<!-- Sources: GESTEL_AGENT_SPEC.md section 13.0, local app/lib/creative-flow.ts, distilled ad creative source skills -->
<!-- Used by: gestel-creative-package -->

# Slot Contract

Slots are structured creative inputs. They keep the MVP out of freeform canvas editing while still allowing useful iteration.

## Required Slot Groups

| Slot | Required | Notes |
| --- | --- | --- |
| `product_visual` | Yes | Points to the preserved product photo or selected crop. Product form, color, package, and label must remain faithful. |
| `headline` | Yes | Short Korean commerce headline. Must not introduce unsupported claims. |
| `subcopy` | No | Clarifies product benefit, use case, or proof. |
| `cta` | Yes | Simple platform-safe action such as "구매하기", "자세히 보기", or "혜택 확인". |
| `badge` | No | Review, coupon, limited offer, ingredient, or shipping badge. Needs evidence when factual. |
| `price_or_offer` | No | Requires user-confirmed price, discount, shipping, bundle, or deadline evidence. |
| `disclosure` | Conditional | Required when advertising, sponsorship, AI virtual person, limited quantity, or price-evidence disclosure applies. |

## Allowed Edits

The MVP allows slot-level edits only:

- Headline.
- Subcopy.
- CTA.
- Badge.
- Price or offer text.
- Template family.
- Layout ID.
- Ratio expansion.
- Regeneration request.

Do not model arbitrary layers, masks, freehand positioning, or direct canvas manipulation in this skill.

## Evidence Rules

- Every price, discount, ranking, certification, ingredient, effect, shipping promise, review quote, or deadline needs an evidence ID or URL.
- If evidence is missing, lower the claim, remove it, or route to `gestel-creative-review` with `claim_price_evidence` risk.
- Preserve exact Korean claim text when checking evidence.

## Korean Copy Defaults

Use `ko-KR`, natural commerce Korean, and concise mobile-first text. Avoid machine-translated stiffness, exaggerated medical or financial certainty, and unverifiable superlatives.
