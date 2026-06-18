---
name: delivery-router
description: Route product delivery requests to the correct focused skill. Use when a user asks for broad product work, an ambiguous product deliverable, full workflow planning, or when it is unclear whether the task belongs to PRD, interaction, UI concept, HTML prototype, design contract, asset spec, or developer handoff. Do not use this router for skill maintenance; use skill-creator for modifying skills.
---

# Delivery Router

## Introduction

This is the lightweight entry point for broad product-delivery requests. It does not execute every stage; it classifies the request and points Codex to the focused skill that should do the actual work.

## Route First

Classify the user's request and use the focused skill that matches the actual task:

- Requirements, scope, product goals, acceptance criteria, assumptions, or `PRD.md`: use `prd-writer`.
- Flows, navigation, screen states, validation, permissions, errors, empty/loading states, or `Interaction-Spec.md`: use `interaction-spec`.
- UI style direction, visual references, page effect descriptions, or image-generation prompts: use `ui-concept`.
- HTML prototype creation or repair, route/page/module refinement, CSS/layout fixes, or product screen implementation: use `html-prototype`.
- `Design.md`, measured visual rules, tokens, component standards, page exceptions, or layout contracts: use `design-contract`.
- `Asset-Spec.md`, asset slots, placeholders, image/icon replacement rules, or asset-generation prompts: use `asset-spec`.
- Concrete project delivery to engineers, `Docs-Handoff.md`, Vibo coding prompts, canonical file maps, final audit, or implementation notes: use `dev-handoff`.

## Full Workflow

For a full product package, move through the focused skills in this order:

1. `prd-writer`
2. `interaction-spec`
3. `ui-concept`
4. `html-prototype`
5. `design-contract`
6. `asset-spec`
7. `dev-handoff`

Ask before advancing between major stages unless the user explicitly says to proceed automatically. Within a focused stage, continue normal same-stage feedback without extra gates.

## Skill Maintenance Boundary

If the request is to modify skills, references, routing rules, metadata, or this router, do not run product stages. Treat the task as skill maintenance and use `skill-creator` guidance.

## Output

When routing only, state the chosen focused skill and why. When the user asked for actual work and the correct focused skill is available, proceed with that skill rather than staying in this router.
