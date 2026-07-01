# /// script
# requires-python = ">=3.10"
# dependencies = ["fal-client>=0.5.0", "requests>=2.31", "python-dotenv>=1.0"]
# ///
"""Render images with GPT Image 2 (gpt-image-2) via the fal API.

Text-to-image and reference-image editing. Reads FAL_KEY from the environment or
a --env-file. Spends money per image, so it prints the request first and supports
--dry-run for a no-cost preflight.

Examples:
  # Preflight (no API call, no cost)
  uv run generate.py --prompt-file prompt.txt --image-size 1024x1024 --dry-run

  # Text-to-image
  uv run generate.py --prompt-file prompt.txt --image-size 1024x1024 \
      --quality high --output-dir renders --env-file ~/dev/gestel-app/.env

  # Reference-image edit (faithful reproduction / variant)
  uv run generate.py --prompt-file prompt.txt --mode edit \
      --ref-image original.jpg --input-fidelity high --output-dir renders
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

GENERATE_ENDPOINT = "openai/gpt-image-2"
EDIT_ENDPOINT = "openai/gpt-image-2/edit"

# fal accepts these named presets or an explicit {width, height}.
SIZE_PRESETS = {
    "square",
    "square_hd",
    "portrait_4_3",
    "portrait_16_9",
    "landscape_4_3",
    "landscape_16_9",
    "auto",
}


def eprint(*args: object) -> None:
    print(*args, file=sys.stderr, flush=True)


def parse_size(value: str) -> object:
    """Return a fal image_size: a preset string or a {width, height} dict."""
    if value in SIZE_PRESETS:
        return value
    match = re.fullmatch(r"(\d+)\s*[xX]\s*(\d+)", value.strip())
    if not match:
        raise SystemExit(
            f"--image-size must be a preset {sorted(SIZE_PRESETS)} or WxH like 1024x1024, got {value!r}"
        )
    width, height = int(match.group(1)), int(match.group(2))
    for edge in (width, height):
        if edge % 16 != 0:
            eprint(
                f"warning: edge {edge} is not a multiple of 16; gpt-image-2 may reject it"
            )
    return {"width": width, "height": height}


def load_env_file(path: Path) -> None:
    from dotenv import load_dotenv

    if not path.exists():
        raise SystemExit(f"--env-file not found: {path}")
    load_dotenv(dotenv_path=path, override=False)


def read_prompt(args: argparse.Namespace) -> str:
    if args.prompt_file:
        text = Path(args.prompt_file).read_text(encoding="utf-8").strip()
    elif args.prompt:
        text = args.prompt.strip()
    else:
        raise SystemExit("provide --prompt or --prompt-file")
    if not text:
        raise SystemExit("prompt is empty")
    return text


def build_arguments(
    args: argparse.Namespace, prompt: str, image_urls: list[str]
) -> dict:
    arguments: dict[str, object] = {
        "prompt": prompt,
        "num_images": args.num_images,
        "output_format": args.output_format,
        "quality": args.quality,
    }
    if args.image_size:
        arguments["image_size"] = parse_size(args.image_size)
    if args.mode == "edit":
        arguments["image_urls"] = image_urls
        if args.input_fidelity:
            arguments["input_fidelity"] = args.input_fidelity
        if args.mask_image:
            arguments["mask_url"] = args.mask_image
    return arguments


def resolve_ref_images(ref_images: list[str]) -> list[str]:
    """Upload local files to fal; pass through anything that is already a URL."""
    import fal_client

    urls: list[str] = []
    for ref in ref_images:
        if ref.startswith(("http://", "https://")):
            urls.append(ref)
            continue
        path = Path(ref)
        if not path.exists():
            raise SystemExit(f"--ref-image not found: {ref}")
        eprint(f"uploading reference image: {path}")
        urls.append(fal_client.upload_file(str(path)))
    return urls


def download(url: str, dest: Path) -> None:
    import requests

    resp = requests.get(url, timeout=120)
    resp.raise_for_status()
    dest.write_bytes(resp.content)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Render images with gpt-image-2 via fal."
    )
    src = parser.add_mutually_exclusive_group()
    src.add_argument("--prompt", help="prompt text (or use --prompt-file)")
    src.add_argument("--prompt-file", help="path to a file containing the prompt")
    parser.add_argument("--mode", choices=["generate", "edit"], default="generate")
    parser.add_argument(
        "--image-size",
        help="preset (e.g. landscape_4_3) or WxH (e.g. 1024x1024). Omit for the endpoint default.",
    )
    parser.add_argument("--quality", choices=["low", "medium", "high"], default="high")
    parser.add_argument("--num-images", type=int, default=1)
    parser.add_argument(
        "--output-format", choices=["png", "jpeg", "webp"], default="png"
    )
    parser.add_argument(
        "--input-fidelity", choices=["low", "high"], help="edit mode: preserve likeness"
    )
    parser.add_argument(
        "--ref-image",
        action="append",
        default=[],
        help="edit mode: local path or URL, repeatable",
    )
    parser.add_argument("--mask-image", help="edit mode: optional mask image URL")
    parser.add_argument("--output-dir", default="renders", help="where to save images")
    parser.add_argument("--name", default="render", help="output filename stem")
    parser.add_argument("--env-file", help="path to a .env file providing FAL_KEY")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print the request and exit without calling fal (no cost)",
    )
    args = parser.parse_args()

    if args.env_file:
        load_env_file(Path(args.env_file).expanduser())

    prompt = read_prompt(args)

    if args.mode == "edit" and not args.ref_image:
        raise SystemExit("edit mode requires at least one --ref-image")

    import os

    have_key = bool(os.environ.get("FAL_KEY"))

    endpoint = EDIT_ENDPOINT if args.mode == "edit" else GENERATE_ENDPOINT

    if args.dry_run:
        # Build arguments without uploading (show local ref paths as-is).
        preview = build_arguments(args, prompt, image_urls=list(args.ref_image))
        eprint(f"[dry-run] endpoint: {endpoint}")
        eprint(f"[dry-run] FAL_KEY present: {have_key}")
        eprint(
            f"[dry-run] would generate {args.num_images} image(s) — this WOULD cost money on a real run"
        )
        print(
            json.dumps(
                {"endpoint": endpoint, "arguments": preview},
                indent=2,
                ensure_ascii=False,
            )
        )
        return 0

    if not have_key:
        raise SystemExit(
            "FAL_KEY not set. Export it or pass --env-file pointing at a .env that defines FAL_KEY."
        )

    import fal_client

    image_urls = resolve_ref_images(args.ref_image) if args.mode == "edit" else []
    arguments = build_arguments(args, prompt, image_urls)

    eprint(f"calling {endpoint} for {args.num_images} image(s) (paid) ...")
    result = fal_client.subscribe(endpoint, arguments=arguments, with_logs=False)

    images = result.get("images") or []
    if not images:
        eprint("no images returned; full result follows:")
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 1

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    ext = {"jpeg": "jpg", "webp": "webp"}.get(args.output_format, "png")

    saved: list[str] = []
    for i, image in enumerate(images):
        url = image.get("url")
        if not url:
            continue
        suffix = "" if len(images) == 1 else f"-{i + 1}"
        dest = out_dir / f"{args.name}{suffix}.{ext}"
        download(url, dest)
        saved.append(str(dest))
        eprint(f"saved {dest}")

    print(
        json.dumps(
            {"endpoint": endpoint, "saved": saved, "count": len(saved)},
            indent=2,
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
