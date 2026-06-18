---
name: product-ui-concept
description: Create UI style directions, visual concepts, reference-image analysis, page effect descriptions, and image-generation prompts for product screens. Use when Codex needs UI-Concept-Prompts.md, style options, or visual direction before implementation. Do not use for PRD writing, interaction rules, HTML coding, asset inventory, or developer handoff.
---

# Product UI Concept

Use this skill for Stage 3 visual direction and UI concept work.

## Scope

- Create style directions, page effect notes, visual reference analysis, and image-generation prompts.
- Use `references/ui-concept-guide.md`.
- Confirm product scenario, device context, information density, and comparable products before finalizing a direction.
- Treat generated images as concept references, not implementation specs.

## Boundaries

- Do not code HTML.
- Do not convert visual directions into measured design rules unless the user asks for a design contract.
- Do not plan every asset slot.

## Completion

Summarize chosen style direction, alternatives rejected, source assumptions, and recommended next step. If measured layout rules are needed, recommend `product-design-contract`; if coding is requested, recommend `product-html-prototype`.
