---
name: ui-design-master
description: Master UI visual direction and design contracts. Use when Codex needs UI style directions, visual concepts, reference analysis, UI-Concept-Prompts.md, Design.md, visual tokens, component rules, typography, spacing, layout constraints, page exceptions, and screen-specific visual QA. Do not use for PRD writing, interaction-only work, raw HTML skeleton implementation, asset rendering inventory, or developer handoff.
---

# UI Design Master

## Introduction

This skill owns the visual design layer. It combines UI concept direction with measured design contracts so later HTML skeleton and asset work have a clear visual source of truth.

## Scope

- Create UI style directions, visual reference analysis, page effect notes, and image-generation prompts.
- Create or repair `Design.md`.
- Define global tokens, component standards, screen-specific rules, page exceptions, layout constraints, typography, spacing, states, and QA checks.
- Use `references/ui-concept-guide.md` for visual direction.
- Use `references/design-system-guide.md` for measured design contracts.
- Use `references/change-impact-guide.md` when visual decisions affect HTML, assets, interaction, requirements, or handoff.

## Required Checks

- Treat generated UI images as concept references, not implementation specs.
- Do not encode undocumented visual assumptions directly into HTML/CSS.
- If a page needs a one-off rule, record it as a page exception rather than a global component rule.
- When HTML reveals a better repeated rule, update `Design.md` and remove stale rules.

## Boundaries

- Do not write PRD or full interaction specs.
- Do not build HTML skeletons unless the user explicitly asks to implement the design.
- Do not inventory every asset slot unless visual decisions require asset planning.

## Completion

Summarize chosen UI direction, design rules changed, affected screens/components, and known exceptions. If HTML implementation is next, recommend:

`html-skeleton-worker`

https://github.com/YinHeBuilder/codex-product-delivery-skill/tree/main/skills/html-skeleton-worker
