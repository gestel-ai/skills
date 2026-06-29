<!-- Updated: 2026-06-26 | v1.0 -->
<!-- Sources: OpenAI Codex Agent Skills docs, local skill pattern audit, platform-agnostic research intake design -->
<!-- Used by: skillify -->

# Deep Research Intake

Use this when the research gate passes and the user has not provided source research files.

## Intake Rule

Do not populate `research-sources/` yourself during normal execution. Ask the user to run Deep Research in external platforms and provide Markdown exports or local file paths.

Do not ask for Deep Research for every skill. Ask only when the skill depends on freshness-sensitive or evidence-critical material.

Request separate files when possible:

- `research-sources/chatgpt-deep-research-YYYY-MM-DD.md`
- `research-sources/gemini-deep-research-YYYY-MM-DD.md`
- `research-sources/claude-deep-research-YYYY-MM-DD.md`
- `research-sources/perplexity-deep-research-YYYY-MM-DD.md`

If a platform is unavailable, ask the user to skip it and note the missing source in the final provenance.

## What To Ask For

Ask the user for:

- The final report in Markdown.
- All cited links or source bibliography.
- Any research plan, scope, or assumptions shown by the platform.
- Date of the research run.
- The exact prompt used, if it differs from the template below.

## Shared Prompt Skeleton

Use `deep-research-prompt-library.md` to generate prompts with consistent topic, structure, and output format. The only routine variation should be the freshness mode and platform wrapper.

Use this structure in every platform prompt when a short inline prompt is enough:

```text
Research topic: <topic>
Target artifact: recommendations for updating an agent skill named <skill-name>.
Audience: an AI coding agent that writes SKILL.md, references, evals, scripts, and validation gates.

Research goals:
1. Identify current best practices, patterns, and edge cases for <domain>.
2. Separate stable principles from claims that may expire.
3. Collect concrete examples, anti-patterns, and decision criteria.
4. Flag disagreements, uncertainty, and missing evidence.
5. Produce a source-backed Markdown report suitable for saving as <platform>-deep-research-YYYY-MM-DD.md.

Scope:
- Include official/vendor documentation first.
- Include credible implementation examples and practitioner reports when useful.
- Exclude shallow listicles, uncited claims, and outdated material unless explaining historical context.

Output format:
- Executive summary
- Stable principles
- Current or time-sensitive claims with dates
- Recommended skill rules
- Suggested eval cases
- Suggested validation scripts or lint gates
- Risks and anti-patterns
- Source table with title, URL, publisher, date checked, and why it matters
- Open questions

Please cite sources inline and include a complete bibliography.
```

## ChatGPT Deep Research Prompt

```text
Use ChatGPT Deep Research for a multi-step, source-backed investigation.

<shared prompt skeleton>

Additional instructions:
- Ask at most 1-2 clarifying questions only if the scope is blocking.
- Prefer official documentation and primary sources before secondary commentary.
- Explicitly separate findings based on official sources from inferences.
- Include the final answer as Markdown that can be saved directly.
- Include the full list of sources consulted and mark any source that was read but not used.
```

## Gemini Deep Research Prompt

```text
Use Gemini Deep Research to produce an in-depth report. Use Google Search by default and include uploaded files, Drive files, or NotebookLM notebooks only if I explicitly provide them.

<shared prompt skeleton>

Additional instructions:
- Show or preserve the research plan if Gemini provides one.
- Use current web sources and cite them.
- Include charts or tables only when they improve the report; always include a text equivalent in Markdown.
- Distinguish evidence from synthesis.
- Export or present the final report as Markdown with bibliography.
```

## Claude Research Prompt

```text
Use Claude Research for a thorough, citation-backed investigation. You may use web search and available read-only connectors, but do not use tools that can write to external systems.

<shared prompt skeleton>

Additional instructions:
- Ask 1-2 key questions up front only if the missing context would materially change the research.
- Investigate multiple angles and follow-up questions systematically.
- Include easy-to-check citations and a source table.
- Call out uncertainty, source conflicts, and where original sources should be manually verified.
- Return the final report as Markdown.
```

## Perplexity Deep Research Prompt

```text
Use Perplexity Deep Research or Advanced Deep Research to create a comprehensive, citation-backed report.

<shared prompt skeleton>

Additional instructions:
- Prefer exhaustive source discovery over quick answer mode.
- Compare conflicting sources and explain which evidence is stronger.
- Include citations for every major claim.
- Include a source table and a short "not used / low confidence" section.
- Return the final report as Markdown.
```
