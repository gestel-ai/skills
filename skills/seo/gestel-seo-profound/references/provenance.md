<!-- Sources: references/source-repos/MANIFEST.md, source path listed below -->
<!-- Used by: gestel-seo-profound -->

# Provenance

This skill is a local standardization of license-compatible source material. It does not copy upstream runtime scripts, the extension installer (`install.sh`/`install.ps1`/`uninstall.sh`), the Profound API client, provider adapters, API keys, or any hidden credential assumptions.

## Source Map

- Source path: `references/skills/claude-seo/extensions/profound/skills/seo-profound/SKILL.md`
- Supporting source consulted: `references/skills/claude-seo/extensions/profound/docs/PROFOUND-SETUP.md`
- Upstream path: `references/source-repos/claude-seo/extensions/profound/skills/seo-profound/SKILL.md`
- Source `references/` and `evals/`: none present in the source skill folder, so none were copied.
- Commit: `d830cdb2ad339bb7f062339fe82228b072e98061`
- License: MIT (Copyright (c) 2026 agricidaniel)

## Local Changes

- Converted a thin provider-routing skill (which assumed a live Profound API key and continuous polling) into a self-contained analysis skill with trigger-focused frontmatter (triggers, near-miss exclusions, and the no-credentials/no-paid-provider/no-live-mutation/no-upstream-scripts boundary inline).
- Distilled the implicit methodology into real, embedded content: precise metric definitions (citation rate, share of voice, co-citation, win/loss, trend delta), a funnel-spanning prompt-set design framework, sampling-noise floors, baseline-band alert math, a diagnosis-to-fix-lever map, and a provider-free one-shot sampling procedure. Authored `references/llm-citation-tracking.md` (local) and linked it from SKILL.md.
- Converted the deferred runtime dependencies (Profound API key, `install.sh`/`install.ps1`, continuous LLM polling, dated time-series, real-time alerts, full platform coverage, SE Ranking / DataForSEO adapters) into explicit Boundaries that route to a user-supplied export, a separately configured provider adapter, or the local manual one-shot sample.
- Preserved the original provider command list as attribution only, marked non-invocable without the paid key.
- No dependency on the top-level `references/` tree; that tree is attribution only.

## Related Source Repo Commits (attribution only)

- claude-ads: `283d9d4917cb7c4f2ce9181e125bb1970f74ab04`
- claude-blog: `49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25`
- claude-seo: `d830cdb2ad339bb7f062339fe82228b072e98061`
- marketingskills: `8bfcdffb655f16e713940cd04fb08891899c47db`
