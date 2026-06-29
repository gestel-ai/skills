# Research Sources: skillify

This folder is reserved for user-provided Deep Research Markdown files.

Agents must not create, synthesize, or backfill research source files during normal skill execution. If source research is missing, ask the user to run Deep Research externally and provide the resulting `.md` files.

Use `../references/deep-research-intake.md` when requesting platform-specific Deep Research files.

## Expected Files

| Platform | Preferred File Name | Notes |
| --- | --- | --- |
| ChatGPT | `chatgpt-deep-research-YYYY-MM-DD.md` | Include final report, citations, and source list |
| Gemini | `gemini-deep-research-YYYY-MM-DD.md` | Include final report, citations, and source list |
| Claude | `claude-deep-research-YYYY-MM-DD.md` | Include final report, citations, and source list |
| Perplexity | `perplexity-deep-research-YYYY-MM-DD.md` | Include final report, citations, and source list |

## Runtime Rule

Use `references/` for normal skill execution. Use `research-sources/` only when auditing or refreshing a research-backed skill after the user has supplied source files.
