<!-- Updated: 2026-06-26 | v1.0 -->
<!-- Sources: GESTEL_AGENT_SPEC.md sections 13.0 and 13.4.1 -->
<!-- Used by: gestel-creative-package, gestel-ads-intelligence -->

# Export Contract

A Creative Package is ready for a human or downstream tool to launch, but it is not a live campaign and must not mutate an ad account.

## Manifest Shape

Use JSON for machine checks:

```json
{
  "package_id": "pkg_20260626_example",
  "brand_snapshot_ref": ".agents/gestel/brand-snapshot.md",
  "channel": "meta",
  "commerce_surface": "smartstore",
  "items": [
    {
      "variant_id": "v_pkg_001_a",
      "template_family": "review_proof",
      "layout_id": "review_proof.proof.v1",
      "ratio": "4:5",
      "asset_path": "exports/v_pkg_001_a_4x5.png",
      "angle": "review proof",
      "experiment_hypothesis": "Review proof will improve CTR for cold Meta feed traffic.",
      "slots": {
        "product_visual": "product-photo-1",
        "headline": "구매 전 고민 줄이기",
        "cta": "자세히 보기"
      },
      "product_claim_evidence_ids": ["ev_review_001"],
      "review_status": "needs_review",
      "utm": {
        "utm_campaign": "gestel_pkg_20260626",
        "utm_content": "v_pkg_001_a"
      }
    }
  ],
  "export": {
    "package_name": "gestel_pkg_20260626",
    "naming_pattern": "{package_id}_{variant_id}_{ratio}"
  }
}
```

## Required Mapping Fields

Every item needs:

- `variant_id`.
- `template_family`.
- `layout_id`.
- `ratio`.
- `asset_path`.
- `angle`.
- `experiment_hypothesis`.
- `slots`.
- `review_status`.
- `utm.utm_campaign`.
- `utm.utm_content`.

The `variant_id`, exported creative name, and `utm_content` should map back to the same variant for manual performance import.

## Review Status Values

- `draft`: generated but not checked.
- `needs_review`: ready for Creative Review Gate.
- `launch-ready`: passed Creative Review Gate and owner approval requirements.
- `blocked`: cannot be made launch-ready without new evidence, product input, or regeneration.

## Validation

Run:

```bash
uv run .agents/skills/gestel-creative-package/scripts/validate_pack_schema.py <manifest.json>
```

For the initial MVP first pack, run:

```bash
uv run .agents/skills/gestel-creative-package/scripts/validate_pack_schema.py --mode first-pack <manifest.json>
```
