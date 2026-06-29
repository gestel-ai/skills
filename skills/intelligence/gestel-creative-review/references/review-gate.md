<!-- Updated: 2026-06-26 | v1.0 -->
<!-- Sources: CONTEXT.md, GESTEL_AGENT_SPEC.md section 13.1, distilled ads-creative and ad-creative source skills -->
<!-- Used by: gestel-creative-review -->

# Creative Review Gate

Every generated creative must pass these gates before it is marked launch-ready.

## Product Fidelity

Fail when the generated creative:

- Changes product shape, color, package, logo, label, quantity, ingredient, variant, or included accessories materially.
- Invents a product option, bundle, ingredient, certification, or use case.
- Replaces the product with a generic stock-like object.
- Crops the product so severely that the advertised item is ambiguous.

Warnings are acceptable only when the difference is cosmetic and does not alter what the customer believes they are buying.

## Claim And Price Evidence

Fail or require revision when the creative includes an unsupported:

- Price, discount, coupon, deadline, shipping promise, or limited quantity claim.
- Ranking, bestseller, "No. 1", guarantee, certification, medical, financial, safety, or efficacy claim.
- Review quote, star rating, before/after implication, or comparison.

Each factual claim needs a source from the product URL, user-confirmed input, uploaded evidence, or Brand Snapshot evidence table. If evidence is missing, lower the wording, remove the claim, or request evidence.

## Platform Fit

Fail or require revision when:

- Ratio does not match the intended static placement.
- Main text, CTA, logo, or product is at high crop risk.
- Korean copy is unnatural, misleading, or too dense for mobile.
- Required advertising, sponsorship, AI virtual person, price, or limited-quantity disclosure is missing.
- The creative needs a policy check for category-sensitive claims before launch.

## Status Rules

| Situation | `review_status` | `failure_type` | `credit_policy` | `regeneration_available` |
| --- | --- | --- | --- | --- |
| All gates pass | `launch-ready` | `none` | `charge` | `false` |
| Product materially changed | `needs_revision` or `blocked` | `product_fidelity` | `regeneration_credit` | `true` |
| Unsupported claim or price | `needs_revision` | `claim_price_evidence` | `charge` | `false` |
| Platform ratio, safe zone, readability, or disclosure issue | `needs_revision` | `platform_fit` | `charge` | `true` when regeneration is needed |
| Provider or system failure | `blocked` | `system` | `refund` or `no_charge` | `true` |
| User requested an unsafe or unsupported claim | `blocked` | `user_input` | `charge` | `false` |

## Required Fixes

Every non-launch-ready result needs at least one specific fix:

- Slot edit.
- Evidence request.
- Softer replacement copy.
- Template or ratio change.
- Regeneration instruction focused on product preservation.
