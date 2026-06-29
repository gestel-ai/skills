<!-- Updated: 2026-06-26 | v1.0 -->
<!-- Sources: OpenAI Codex Agent Skills docs, local skill pattern audit, platform-agnostic research intake design -->
<!-- Used by: skillify -->

# Deep Research Prompt Library

Use this library to ask the user for consistent Deep Research runs before creating or refreshing a research-backed skill.

## When To Use

Use these prompts only after the research gate passes:

- Current platform, API, policy, pricing, law, model behavior, ranking, or market-trend claims matter.
- The skill depends on benchmarks, vendor docs, imported prompt frameworks, or third-party research.
- The user explicitly asks for a research-backed skill.

Do not use these prompts for stable local workflows, simple scripts, straightforward repo conventions, or skills whose correctness can be validated locally.

## Variables

Set these once and keep them identical across platforms:

- `skill_name`: target skill name.
- `domain`: domain the skill should cover.
- `target_user`: who will invoke the skill.
- `core_jobs`: 3-5 jobs the skill must support.
- `near_misses`: 3-5 adjacent tasks the skill should not trigger on.
- `freshness_mode`: one of `evergreen`, `current`, `trend-sensitive`, or `regulated`.
- `date`: research run date.
- `known_sources`: official docs, repos, papers, or local files the user wants included.
- `non_goals`: things the research should not cover.

## Freshness Modes

Use the same prompt body and vary only this block:

```text
Freshness mode: <freshness_mode>

If evergreen:
- Prioritize stable principles, official specs, and durable design patterns.
- Mark time-sensitive details as optional follow-up research.

If current:
- Verify official documentation and current platform behavior as of <date>.
- Mark each current claim with date checked and refresh trigger.

If trend-sensitive:
- Focus on changes in the last 6-12 months, but preserve stable principles separately.
- Include trend confidence, counter-evidence, and expected expiry.

If regulated:
- Treat legal, policy, pricing, medical, financial, or compliance claims as needing primary sources.
- Do not infer rules from commentary alone.
- Include jurisdiction, policy version, or publication date where relevant.
```

## Core Prompt

Use this body for ChatGPT, Gemini, Claude, and Perplexity. Keep the topic and output schema identical so reports are comparable.

```text
Research topic: Build or refresh an agent skill named <skill_name> for <domain>.
Target user: <target_user>.
Core jobs the skill must support:
- <core_job_1>
- <core_job_2>
- <core_job_3>

Near-miss tasks the skill should not trigger on:
- <near_miss_1>
- <near_miss_2>
- <near_miss_3>

<freshness_mode block>

Known sources to include:
- <known_source_1>
- <known_source_2>

Non-goals:
- <non_goal_1>
- <non_goal_2>

Research goals:
1. Identify stable best practices for this skill domain.
2. Identify current or freshness-sensitive claims and their refresh triggers.
3. Find concrete examples, anti-patterns, edge cases, and failure modes.
4. Recommend trigger wording and near-miss boundaries.
5. Recommend references, scripts, assets, and eval cases.
6. Flag source conflicts, weak evidence, and open questions.

Output format:
1. Executive summary
2. Stable principles
3. Current or freshness-sensitive claims
4. Recommended SKILL.md workflow
5. Recommended reference files
6. Recommended scripts or lint/format gates
7. Recommended eval cases, including should-not-trigger cases
8. Risks, anti-patterns, and safety concerns
9. Source table with title, URL, publisher, date checked, and why it matters
10. Open questions

Return the report as Markdown that can be saved as:
research-sources/<platform>-deep-research-<date>.md
```

## Platform Wrappers

Add exactly one wrapper above the core prompt.

### ChatGPT

```text
Use ChatGPT Deep Research for a multi-step, source-backed investigation. Prefer official and primary sources, separate evidence from inference, and include a complete bibliography.
```

### Gemini

```text
Use Gemini Deep Research. Preserve the research plan if Gemini creates one, use current web sources, and return the final report with citations and bibliography in Markdown.
```

### Claude

```text
Use Claude Research. Investigate multiple angles systematically, include easy-to-check citations, call out uncertainty and source conflicts, and do not use tools that write to external systems.
```

### Perplexity

```text
Use Perplexity Deep Research or Advanced Deep Research. Prefer exhaustive source discovery, compare conflicting sources, cite every major claim, and include a low-confidence or not-used source section.
```

## User Request Template

When asking the user for sources, use this shape:

```text
이 skill은 최신성/근거가 중요한 자료 기반 skill이라 `research-sources/`가 필요합니다.
제가 실행 중 임의로 source 파일을 만들지는 않겠습니다.

아래 4개 플랫폼에서 같은 주제로 Deep Research를 각각 돌린 뒤 Markdown 파일이나 로컬 경로를 공유해주세요:

- ChatGPT: `research-sources/chatgpt-deep-research-YYYY-MM-DD.md`
- Gemini: `research-sources/gemini-deep-research-YYYY-MM-DD.md`
- Claude: `research-sources/claude-deep-research-YYYY-MM-DD.md`
- Perplexity: `research-sources/perplexity-deep-research-YYYY-MM-DD.md`

사용 불가능한 플랫폼은 건너뛰어도 됩니다. 대신 최종 provenance에 빠진 source로 표시하겠습니다.

각 플랫폼에는 아래 prompt를 사용해주세요:

<platform wrapper>
<core prompt with variables filled>
```
