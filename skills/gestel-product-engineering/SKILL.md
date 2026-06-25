---
name: gestel-product-engineering
description: Pragmatic product engineering guidance for designing, implementing, reviewing, and refactoring application code with small reversible changes, boring technology, simple architecture, semantic HTML, and practical tests. Use when maintainability, delivery speed, and operational risk matter.
---

# Gestel Product Engineering

Use this skill to keep product engineering work simple, shippable, and easy to
debug.

## Operating Bias

- Treat complexity as a cost.
- Prefer the smallest system that solves the real problem well.
- Spend engineering effort on domain behavior, product value, and user
  workflows before framework ceremony.
- Reuse existing infrastructure before adding a new moving part.
- Add dependencies, services, abstractions, and process only when they directly
  unlock current user or business value.

## Workflow

1. Read the existing code, docs, tests, and operational setup before proposing a
   shape.
2. Identify the 80/20 version that delivers the core value.
3. Keep changes small, reversible, and aligned with local patterns.
4. Explain maintainability, delivery-speed, or operational-risk tradeoffs when
   they materially affect the decision.
5. Verify the work with the narrowest reliable checks that cover the changed
   behavior.

## Architecture

- Prefer monoliths before microservices.
- Prefer server-rendered HTML before client-heavy SPAs for content, forms, and
  simple CRUD.
- Prefer SQL and a managed relational database before specialized datastores.
- Do not optimize for hypothetical scale before concrete pressure appears.
- Do not split systems before boundaries are stable and obvious.
- Introduce abstractions after repeated evidence, not anticipation.
- Keep boundaries narrow: a good interface hides internal complexity and is easy
  to explain.

## Frontend

- Use semantic HTML first.
- Use native browser features for forms, disclosure, dialogs, validation,
  navigation, and basic interactivity where practical.
- Add JavaScript only when HTML and CSS cannot express the behavior cleanly.
- Avoid client-side application architecture for pages that mainly display
  content, collect forms, or perform simple CRUD.
- If a framework is already in use, follow existing conventions and keep the
  interaction complexity justified by the product.

## Implementation

- Prefer clear, boring code over clever code.
- Avoid premature DRY; duplication is often cheaper than the wrong abstraction.
- Name intermediate concepts when they make code easier to read.
- Do not hide simple logic behind unnecessary layers.
- Delete code, configuration, dependencies, and services that no longer carry
  their weight.

## Testing

- Treat tests as feedback tools, not rituals.
- Prefer integration tests around stable boundaries.
- Keep a small, reliable end-to-end suite for critical user flows.
- Use unit tests where they clarify logic or help drive a small design.
- For bug fixes, reproduce the bug with a regression test first when practical.
- Avoid excessive mocking; mock only at coarse system boundaries when there is
  no better option.

## Refactoring

- Refactor when the system has enough shape to reveal good boundaries.
- Keep refactors incremental; the system should stay working between steps.
- Avoid large rewrites unless the current design blocks necessary work and
  smaller steps are not viable.

## Decision Check

Before adding a feature, dependency, service, abstraction, framework, or
process, answer:

- Does this solve a current real problem?
- Can existing technology solve it well enough?
- Will this make onboarding, debugging, deployment, or testing harder?
- Does this move effort toward domain value or away from it?
- What is the simplest version that delivers most of the value?
- What would make us remove this later?
