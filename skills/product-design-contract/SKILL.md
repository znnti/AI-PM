---
name: product-design-contract
description: Create, repair, or audit product design contracts such as Design.md, visual tokens, component rules, layout constraints, typography, spacing, button standards, page exceptions, and screen-specific visual QA rules. Use when Codex needs measured design rules before or after HTML work. Do not use for PRD writing, interaction-only work, raw HTML implementation, asset inventory, or developer handoff.
---

# Product Design Contract

Use this skill for Stage 5 design-system and measured visual contract work.

## Scope

- Create or repair `Design.md`.
- Define global tokens, component standards, screen-specific rules, page exceptions, layout constraints, typography, spacing, states, and QA checks.
- Use `references/design-system-guide.md`.
- Use `references/change-impact-guide.md` when design rule changes affect HTML, assets, interaction, requirements, or handoff files.

## Required Checks

- Do not encode undocumented layout assumptions directly in CSS.
- If a page needs a one-off rule, record it as a page exception rather than a global component rule.
- When HTML changes reveal a better rule, update `Design.md` and remove stale rules.

## Boundaries

- Do not generate PRD or interaction specs.
- Do not inventory assets unless design changes affect asset slots.
- Do not prepare developer handoff.

## Completion

Summarize the rules changed, affected screens/components, required HTML or asset follow-up, and known exceptions.
