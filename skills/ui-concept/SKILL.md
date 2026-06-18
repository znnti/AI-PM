---
name: ui-concept
description: Create UI style directions, visual concepts, reference-image analysis, page effect descriptions, and image-generation prompts for screens. Use when Codex needs UI-Concept-Prompts.md, style options, or visual direction before implementation. Do not use for PRD writing, interaction rules, HTML coding, asset inventory, or developer handoff.
---

# UI Concept

## Introduction

This skill explores the look and feel before implementation. It helps choose visual directions, describe page effects, analyze references, and prepare image-generation prompts.

## Scope

- Create style directions, page effect notes, visual reference analysis, and image-generation prompts.
- Use `references/ui-concept-guide.md`.
- Confirm scenario, device context, information density, and comparable products before finalizing a direction.
- Treat generated images as concept references, not implementation specs.

## Boundaries

- Do not code HTML.
- Do not convert visual directions into measured design rules unless the user asks for a design contract.
- Do not plan every asset slot.

## Completion

Summarize chosen style direction, alternatives rejected, source assumptions, and recommended next step. If coding is next, recommend `html-prototype`; if measured design rules are next, recommend `design-contract`:

`https://github.com/YinHeBuilder/codex-product-delivery-skill/tree/main/skills/html-prototype`

`https://github.com/YinHeBuilder/codex-product-delivery-skill/tree/main/skills/design-contract`
