# GPT Image 2 on fal — API Reference

How `scripts/generate.py` calls GPT Image 2 through the fal API. This is a dated
snapshot (2026); re-verify against fal's live docs if a parameter is rejected.

## Endpoints

| Mode | Endpoint | Purpose |
| --- | --- | --- |
| Text-to-image | `openai/gpt-image-2` | Generate from a prompt only. |
| Edit / reference | `openai/gpt-image-2/edit` | Generate from a prompt plus one or more reference images. |

Up to 16 reference images are accepted in edit mode. Label each image's role in
the prompt when combining more than one (`Image 1: base scene to preserve.
Image 2: style reference.`).

## Arguments

| Argument | Values | Notes |
| --- | --- | --- |
| `prompt` | string | The structured prompt. Put literal text in quotes/ALL CAPS. |
| `image_size` | preset or `{width, height}` | Presets: `square`, `square_hd`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`, `auto`. Explicit dims must be multiples of 16, ratio ≤ 3:1, total pixels 655,360–8,294,400, recommended ceiling 2,560×1,440. |
| `quality` | `low` / `medium` / `high` | `high` for dense text, faces, fine detail; `medium` for general; `low` for fast/high-volume. |
| `num_images` | integer | Keep at `1` for a targeted render; each image is billed. |
| `output_format` | `png` / `jpeg` / `webp` | `png` for crisp graphics and text. |
| `input_fidelity` | `low` / `high` (edit) | `high` preserves likeness and geometry through larger edits. |
| `image_urls` | list of URLs (edit) | The script uploads local paths automatically. |
| `mask_url` | URL (edit, optional) | Restrict the edit to a masked region. |

## Script flags → arguments

| Flag | Maps to |
| --- | --- |
| `--prompt` / `--prompt-file` | `prompt` |
| `--image-size` | `image_size` (preset passthrough or parsed `WxH`) |
| `--quality` | `quality` |
| `--num-images` | `num_images` |
| `--output-format` | `output_format` |
| `--mode edit` + `--ref-image` | endpoint `.../edit` + `image_urls` |
| `--input-fidelity` | `input_fidelity` |
| `--mask-image` | `mask_url` |
| `--dry-run` | print request, no call, no cost |
| `--env-file` | load `FAL_KEY` from a `.env` |

## Result shape

`fal_client.subscribe(...)` returns a dict with an `images` list; each entry has a
`url`. The script downloads every returned URL into `--output-dir`, naming them
from `--name` (a numeric suffix is added when more than one image is returned),
and prints the saved paths as JSON.

## Aspect-ratio mapping

Match the source or intended shape to a valid size:

| Shape | image_size |
| --- | --- |
| Square (1:1) | `1024x1024` or `square_hd` |
| Portrait (2:3) | `1024x1536` or `portrait_4_3` |
| Portrait (4:5) | `1024x1280` |
| Landscape (3:2) | `1536x1024` or `landscape_4_3` |

For a non-standard ratio, pick the closest valid size and accept a small crop or
pad rather than forcing an out-of-range dimension.

## Cost note

Each returned image is billed, and `quality="high"` costs more than lower tiers.
The skill's confirmation gate exists because these calls are not free — never
loop or batch to fish for a better result without an explicit request.
