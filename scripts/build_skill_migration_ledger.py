#!/usr/bin/env python3
"""Build the skill migration ledger from source skill paths."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]

COMMITS = {
    "claude-ads": "283d9d4917cb7c4f2ce9181e125bb1970f74ab04",
    "claude-blog": "49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25",
    "claude-seo": "d830cdb2ad339bb7f062339fe82228b072e98061",
    "marketingskills": "8bfcdffb655f16e713940cd04fb08891899c47db",
}

LICENSES = {
    "claude-ads": "MIT",
    "claude-blog": "MIT",
    "claude-seo": "MIT",
    "marketingskills": "MIT",
}

NOTICES = {
    "claude-blog": "references/source-repos/claude-blog/NOTICE",
}

MERGED_LOCAL_SKILLS = {
    "references/skills/marketingskills/skills/product-marketing/SKILL.md": (
        "gestel-brand-snapshot",
        "Distilled into the local Brand Snapshot context workflow.",
    ),
    "references/skills/marketingskills/skills/customer-research/SKILL.md": (
        "gestel-brand-snapshot",
        "Distilled into the local Brand Snapshot evidence and voice-of-customer workflow.",
    ),
    "references/skills/claude-ads/skills/ads-dna/SKILL.md": (
        "gestel-brand-snapshot",
        "Distilled into the local Brand Snapshot visual identity workflow without upstream screenshot helpers.",
    ),
    "references/skills/claude-blog/skills/blog-brand/SKILL.md": (
        "gestel-brand-snapshot",
        "Distilled into the local Brand Snapshot durable context workflow without blog orchestration.",
    ),
    "references/skills/marketingskills/skills/ad-creative/SKILL.md": (
        "gestel-creative-package",
        "Distilled into the local Creative Package workflow and review-adjacent contracts.",
    ),
    "references/skills/marketingskills/skills/ads/SKILL.md": (
        "gestel-creative-package",
        "Merged into the local Creative Package workflow as the lightweight paid-ads trigger shape.",
    ),
    "references/skills/claude-ads/skills/ads-create/SKILL.md": (
        "gestel-creative-package",
        "Distilled into local Creative Package manifest and brief structure.",
    ),
    "references/skills/claude-ads/skills/ads-creative/SKILL.md": (
        "gestel-creative-package",
        "Distilled into local static creative quality and package planning references.",
    ),
    "references/skills/claude-ads/skills/ads-plan/SKILL.md": (
        "gestel-creative-package",
        "Distilled into local template-family and first-pack planning references.",
    ),
    "references/skills/claude-ads/skills/ads-meta/SKILL.md": (
        "gestel-creative-review",
        "Narrowed into local static placement review and freshness-gated platform-fit checks.",
    ),
    "references/skills/marketingskills/skills/analytics/SKILL.md": (
        "gestel-ads-intelligence",
        "Distilled into local manual performance import and decision-quality workflow.",
    ),
    "references/skills/marketingskills/skills/ab-testing/SKILL.md": (
        "gestel-ads-intelligence",
        "Distilled into local next-test hypothesis and guardrail workflow.",
    ),
    "references/skills/claude-ads/skills/ads-attribution/SKILL.md": (
        "gestel-ads-intelligence",
        "Distilled into local attribution caveats without live account or server-side audit adapters.",
    ),
    "references/skills/claude-ads/skills/ads-test/SKILL.md": (
        "gestel-ads-intelligence",
        "Distilled into local experiment planning for static creative variants.",
    ),
}

DUPLICATE_SUPERSEDED = {
    "references/skills/claude-seo/skills/seo-dataforseo/SKILL.md": (
        "Duplicate source name and adapter surface; superseded by the extension path if a DataForSEO adapter is ever migrated."
    ),
    "references/skills/claude-seo/skills/seo-image-gen/SKILL.md": (
        "Duplicate source name and image-generation surface; superseded by the extensions/banana path if image-generation SEO support is ever migrated."
    ),
}

PROVIDER_OR_AUTH = {
    "blog-audio",
    "blog-google",
    "blog-notebooklm",
    "ads-generate",
    "ads-photoshoot",
    "seo-ahrefs",
    "seo-bing",
    "seo-dataforseo",
    "seo-firecrawl",
    "seo-google",
    "seo-profound",
    "seo-seranking",
}

PROVIDER_ADAPTER_DETAILS = {
    "ads-generate": {
        "required_credentials": [
            "banana-claude or approved image provider credential",
            "nanobanana-mcp configuration",
        ],
        "cost_or_quota_risk": [
            "per-image generation cost",
            "provider rate limits",
            "batch generation spend",
        ],
        "next_input_needed": "Choose the approved image-generation provider, credential location, cost gate, output manifest, and fallback behavior before migrating.",
    },
    "ads-photoshoot": {
        "required_credentials": [
            "banana-claude or approved image provider credential",
            "nanobanana-mcp configuration",
        ],
        "cost_or_quota_risk": [
            "per-image generation cost",
            "style x size batch spend",
        ],
        "next_input_needed": "Choose the approved product-photography provider, credential location, cost gate, output manifest, and retry policy before migrating.",
    },
    "blog-audio": {
        "required_credentials": ["GOOGLE_AI_API_KEY", "FFmpeg availability"],
        "cost_or_quota_risk": ["Gemini TTS usage cost", "voice/model quota limits"],
        "next_input_needed": "Define a Gemini TTS adapter contract with API-key detection, model/voice allowlist, cost gate, and MP3/WAV fallback before migrating.",
    },
    "blog-google": {
        "required_credentials": [
            "Google API key",
            "Google OAuth or service-account credentials",
            "optional GA4 property ID",
            "optional Google Ads developer token and customer ID",
        ],
        "cost_or_quota_risk": [
            "Google API quotas",
            "Indexing API daily publish limit",
            "NLP API billing requirement",
            "report-rendering system dependencies",
        ],
        "next_input_needed": "Define a Google SEO/blog data adapter contract with credential tiers, quota gates, read-only defaults, and report fallback before migrating.",
    },
    "blog-notebooklm": {
        "required_credentials": [
            "Google account with NotebookLM access",
            "interactive browser authentication",
        ],
        "cost_or_quota_risk": [
            "NotebookLM account query limits",
            "headless browser runtime cost",
        ],
        "next_input_needed": "Define a NotebookLM browser adapter contract with auth-state storage rules, no-commit secrets policy, rate limits, and graceful fallback before migrating.",
    },
    "seo-ahrefs": {
        "required_credentials": ["Ahrefs API token", "official @ahrefs/mcp server"],
        "cost_or_quota_risk": ["Ahrefs metered API units", "batch URL cost"],
        "next_input_needed": "Define an Ahrefs MCP adapter contract with availability detection, cost gate, unit logging, and fallback to non-Ahrefs backlink sources before migrating.",
    },
    "seo-bing": {
        "required_credentials": [
            "BING_WEBMASTER_API_KEY",
            "optional INDEXNOW_KEY",
        ],
        "cost_or_quota_risk": [
            "Bing Webmaster API limits",
            "IndexNow submission limits",
        ],
        "next_input_needed": "Define a Bing Webmaster/IndexNow adapter contract with credential checks, host-key verification, read/write authorization, and fallback behavior before migrating.",
    },
    "seo-dataforseo": {
        "required_credentials": [
            "DataForSEO MCP server",
            "DataForSEO API login/password",
        ],
        "cost_or_quota_risk": [
            "DataForSEO per-call charges",
            "filtered query cost multipliers",
            "daily budget limits",
        ],
        "next_input_needed": "Define a DataForSEO MCP adapter contract with endpoint allowlist, pre-call cost gate, post-call logging, daily budget, and no-data fallback before migrating.",
    },
    "seo-firecrawl": {
        "required_credentials": ["Firecrawl MCP server", "FIRECRAWL_API_KEY"],
        "cost_or_quota_risk": [
            "Firecrawl monthly credits",
            "large crawl credit burn",
            "rate limits",
        ],
        "next_input_needed": "Define a Firecrawl adapter contract with page caps, credit estimates, robots/permission handling, and no-cost fallback to local fetch for narrow tasks before migrating.",
    },
    "seo-profound": {
        "required_credentials": ["PROFOUND_API_KEY"],
        "cost_or_quota_risk": [
            "Profound API usage limits",
            "brand tracking query volume",
        ],
        "next_input_needed": "Define a Profound adapter contract with API-key detection, platform coverage statement, quota/cost gate, and confidence labeling before migrating.",
    },
    "seo-seranking": {
        "required_credentials": ["SERANKING_API_KEY"],
        "cost_or_quota_risk": [
            "SE Ranking API unit usage",
            "multi-platform AI visibility query cost",
        ],
        "next_input_needed": "Define an SE Ranking adapter contract with API-key detection, unit cost gate, platform sample-size reporting, and fallback behavior before migrating.",
    },
    "seo-google": {
        "required_credentials": [
            "Google API key",
            "Google OAuth or service-account credentials",
            "optional GA4 property ID",
            "optional Google Ads developer token and customer ID",
        ],
        "cost_or_quota_risk": [
            "Google API quotas",
            "Indexing API daily publish limit",
            "NLP API billing requirement",
            "report-rendering system dependencies",
        ],
        "next_input_needed": "Define a Google SEO adapter contract with credential tiers, quota gates, explicit write authorization for indexing, and report fallback before migrating.",
    },
}

MISSING_RUNTIME_DETAILS = {
    "references/skills/claude-ads/ads/SKILL.md": [
        "scripts/generate_report.py",
        "specialist sub-skills: 22 ads sub-skills",
        "specialist agents: audit and creative agents",
    ],
    "references/skills/claude-ads/skills/ads-audit/SKILL.md": [
        "specialist agents: audit-google",
        "specialist agents: audit-meta",
        "specialist agents: audit-creative",
        "specialist agents: audit-tracking",
        "specialist agents: audit-budget",
        "specialist agents: audit-compliance",
    ],
    "references/skills/claude-blog/skills/blog-analyze/SKILL.md": [
        "scripts/cognitive_load.py",
        "root references: quality-scoring, eeat-signals, ai-slop-detection, editorial-heuristics",
    ],
    "references/skills/claude-blog/skills/blog-discourse/SKILL.md": [
        "scripts/discourse_research.py",
        "root references: research-quality and synthesis-contract",
        "WebSearch result collection pipeline",
    ],
    "references/skills/claude-blog/skills/blog-flow/SKILL.md": [
        "scripts/sync_flow.py",
        "external FLOW prompt sync from GitHub",
        "CC BY prompt attribution workflow",
    ],
    "references/skills/claude-blog/skills/blog-rewrite/SKILL.md": [
        "scripts/blog_preflight.py",
        "scripts/blog_render.py",
        "scripts/generate_hero.py",
        "specialist agent: blog-reviewer",
    ],
    "references/skills/claude-blog/skills/blog-write/SKILL.md": [
        "scripts/blog_preflight.py",
        "scripts/blog_render.py",
        "scripts/generate_hero.py",
        "specialist agent: blog-reviewer",
    ],
    "references/skills/claude-blog/skills/blog/SKILL.md": [
        "scripts/blog_preflight.py",
        "scripts/blog_render.py",
        "scripts/generate_hero.py",
        "scripts/load_untrusted_root.py",
        "specialist agents: blog-researcher, blog-writer, blog-seo, blog-reviewer, blog-translator",
    ],
    "references/skills/claude-seo/extensions/unlighthouse/skills/seo-unlighthouse/SKILL.md": [
        "scripts/unlighthouse_run.py",
        "scripts/lcp_subparts.py",
        "Node 18+ and unlighthouse npm package",
    ],
    "references/skills/claude-seo/skills/seo-audit/SKILL.md": [
        "scripts/render_page.py",
        "scripts/google_auth.py",
        "scripts/backlinks_auth.py",
        "scripts/drift_history.py",
        "scripts/google_report.py",
        "specialist SEO subagents",
    ],
    "references/skills/claude-seo/skills/seo-backlinks/SKILL.md": [
        "scripts/backlinks_auth.py",
        "scripts/moz_api.py",
        "scripts/bing_webmaster.py",
        "scripts/commoncrawl_graph.py",
        "scripts/verify_backlinks.py",
    ],
    "references/skills/claude-seo/skills/seo-cluster/SKILL.md": [
        "scripts/dataforseo_costs.py",
        "scripts/render_page.py",
        "templates/cluster-map.html",
    ],
    "references/skills/claude-seo/skills/seo-drift/SKILL.md": [
        "scripts/drift_baseline.py",
        "scripts/drift_compare.py",
        "scripts/drift_history.py",
        "scripts/drift_report.py",
        "scripts/fetch_page.py",
        "scripts/pagespeed_check.py",
        "scripts/parse_html.py",
    ],
    "references/skills/claude-seo/skills/seo-ecommerce/SKILL.md": [
        "scripts/render_page.py",
        "scripts/parse_html.py",
        "scripts/dataforseo_costs.py",
        "scripts/dataforseo_merchant.py",
        "scripts/dataforseo_normalize.py",
        "scripts/ucp_check.py",
    ],
    "references/skills/claude-seo/skills/seo-flow/SKILL.md": [
        "scripts/sync_flow.py",
        "external FLOW prompt sync from GitHub",
        "CC BY prompt attribution workflow",
    ],
    "references/skills/claude-seo/skills/seo-images/SKILL.md": [
        "scripts/iptc_ai_label.py",
        "scripts/parse_html.py",
    ],
    "references/skills/claude-seo/skills/seo-sxo/SKILL.md": [
        "scripts/parse_html.py",
        "scripts/render_page.py",
    ],
    "references/skills/claude-seo/skills/seo-technical/SKILL.md": [
        "scripts/agent_ux_check.py",
        "scripts/crux_history.py",
        "scripts/gsc_inspect.py",
        "scripts/pagespeed_check.py",
        "scripts/render_page.py",
    ],
    "references/skills/claude-seo/skills/seo/SKILL.md": [
        "scripts/backlinks_auth.py",
        "scripts/drift_history.py",
        "scripts/google_auth.py",
        "scripts/google_report.py",
        "specialist SEO sub-skills",
    ],
}

FRESHNESS_SENSITIVE = {
    "ads-amazon",
    "ads-apple",
    "ads-competitor",
    "ads-google",
    "ads-linkedin",
    "ads-microsoft",
    "ads-server-side-tracking",
    "ads-tiktok",
    "ads-youtube",
    "ai-seo",
    "aso",
    "blog-factcheck",
    "blog-geo",
    "blog-schema",
    "blog-seo-check",
    "programmatic-seo",
    "schema",
    "seo-competitor-pages",
    "seo-content",
    "seo-content-brief",
    "seo-geo",
    "seo-hreflang",
    "seo-image-gen",
    "seo-local",
    "seo-maps",
    "seo-page",
    "seo-plan",
    "seo-programmatic",
    "seo-schema",
    "seo-sitemap",
}

FRESHNESS_SENSITIVE_SOURCE_PATHS = {
    "references/skills/marketingskills/skills/seo-audit/SKILL.md",
}

ACTIVE_MIGRATION_NAMES = {
    "ads-budget",
    "ads-landing",
    "ads-math",
    "blog-audit",
    "blog-brief",
    "blog-calendar",
    "blog-cannibalization",
    "blog-chart",
    "blog-cluster",
    "blog-image",
    "blog-locale-audit",
    "blog-localize",
    "blog-multilingual",
    "blog-outline",
    "blog-persona",
    "blog-repurpose",
    "blog-strategy",
    "blog-taxonomy",
    "blog-translate",
    "churn-prevention",
    "co-marketing",
    "cold-email",
    "community-marketing",
    "competitor-profiling",
    "competitors",
    "content-strategy",
    "copy-editing",
    "copywriting",
    "cro",
    "directory-submissions",
    "emails",
    "free-tools",
    "image",
    "launch",
    "lead-magnets",
    "marketing-ideas",
    "marketing-plan",
    "marketing-psychology",
    "offers",
    "onboarding",
    "paywalls",
    "popups",
    "pricing",
    "prospecting",
    "public-relations",
    "referrals",
    "revops",
    "sales-enablement",
    "signup",
    "site-architecture",
    "sms",
    "social",
    "video",
}


def repo_slug(source_path: str) -> str:
    parts = Path(source_path).parts
    try:
        return parts[2]
    except IndexError as exc:
        raise ValueError(f"Invalid source path: {source_path}") from exc


def skill_name(source_path: str) -> str:
    return Path(source_path).parent.name


def upstream_path(source_path: str) -> str:
    return source_path.replace("references/skills/", "references/source-repos/", 1)


def base_entry(source_path: str) -> dict[str, Any]:
    repo = repo_slug(source_path)
    entry = {
        "source_path": source_path,
        "upstream_path": upstream_path(source_path),
        "name": skill_name(source_path),
        "repo": repo,
        "commit": COMMITS[repo],
        "license": LICENSES[repo],
    }
    if repo in NOTICES:
        entry["notice"] = NOTICES[repo]
    return entry


def build_entry(source_path: str) -> dict[str, Any]:
    entry = base_entry(source_path)
    name = entry["name"]

    if source_path in MERGED_LOCAL_SKILLS:
        local_skill, reason = MERGED_LOCAL_SKILLS[source_path]
        entry.update(
            {
                "status": "merged into named local skill",
                "local_skill": local_skill,
                "reason": reason,
            }
        )
        return entry

    if source_path in DUPLICATE_SUPERSEDED:
        entry.update(
            {
                "status": "duplicate superseded",
                "reason": DUPLICATE_SUPERSEDED[source_path],
            }
        )
        return entry

    if name in PROVIDER_OR_AUTH:
        details = PROVIDER_ADAPTER_DETAILS[name]
        entry.update(
            {
                "status": "blocked by provider/auth/cost adapter",
                "reason": "The source skill assumes an external provider, authenticated account, paid API, or provider-specific adapter that is not standardized in this repo.",
                "adapter_contract": f"docs/skill-migration-adapter-contracts.md#{name}",
                "required_credentials": details["required_credentials"],
                "cost_or_quota_risk": details["cost_or_quota_risk"],
                "next_input_needed": details["next_input_needed"],
            }
        )
        return entry

    if source_path in MISSING_RUNTIME_DETAILS:
        entry.update(
            {
                "status": "blocked by missing runtime dependency",
                "reason": "The source skill references root helper scripts, specialist agents, CLI tools, or package dependencies that have not been migrated into local project skill runtime.",
                "missing_runtime_refs": MISSING_RUNTIME_DETAILS[source_path],
                "next_input_needed": "Inspect the listed upstream runtime, then either migrate the minimal local runtime with TDD and validation or keep the source inactive with this exact blocker.",
            }
        )
        return entry

    if name in FRESHNESS_SENSITIVE or source_path in FRESHNESS_SENSITIVE_SOURCE_PATHS:
        entry.update(
            {
                "status": "waiting on user-provided Deep Research",
                "reason": "The source skill depends on platform rules, SEO behavior, marketplace behavior, policy, or other freshness-sensitive facts that need user-provided Deep Research before active local migration.",
            }
        )
        return entry

    if name in ACTIVE_MIGRATION_NAMES:
        entry.update(
            {
                "status": "migrated active local skill",
                "local_skill": f"gestel-{name}",
                "reason": "License-compatible source skill with no hidden credential, paid provider adapter, or missing upstream runtime dependency detected for this local standardization checkpoint.",
            }
        )
        return entry

    entry.update(
        {
            "status": "archived/reference-only with reason",
            "reason": "License-compatible source material, but not yet standardized into an active local project skill in this migration checkpoint.",
        }
    )
    return entry


def source_paths(root: Path) -> list[str]:
    base = root / "references" / "skills"
    return sorted(path.relative_to(root).as_posix() for path in base.rglob("SKILL.md"))


def build_ledger(root: Path) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "generated_by": ".agents/skills/scripts/build_skill_migration_ledger.py",
        "entries": [build_entry(path) for path in source_paths(root)],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Build docs/skill-migration-ledger.json"
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=ROOT,
        help="Repository root, defaulting to this script's project root",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("docs/skill-migration-ledger.json"),
        help="Output path relative to root unless absolute",
    )
    parser.add_argument("--write", action="store_true", help="Write the ledger")
    args = parser.parse_args(argv)

    root = args.root.resolve()
    output = args.output if args.output.is_absolute() else root / args.output
    rendered = json.dumps(build_ledger(root), indent=2, ensure_ascii=True) + "\n"
    if args.write:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered)
        print(f"Wrote {output.relative_to(root)}")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
