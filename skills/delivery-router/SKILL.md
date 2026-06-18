---
name: delivery-router
description: Route staged product delivery requests to the correct role-based skill. Use when a user asks for broad product work, an ambiguous deliverable, full workflow planning, or when it is unclear whether the task belongs to product building, interaction design, UI design, HTML skeleton work, visual asset rendering, or developer handoff. Do not use this router for skill maintenance; use skill-creator for modifying skills.
---

# Delivery Router

## Introduction

This lightweight entry point decides which role-based delivery skill should handle the request. It should not execute every stage itself.

## Route First

Classify the user's request and use the focused role skill that matches the actual task:

- Product idea, PRD, requirement scope, goals, assumptions, acceptance criteria, or `PRD.md`: use `product-builder`.
- Flows, navigation, screen states, permissions, validation, and interaction behavior: use `interaction-designer`.
- UI direction, visual language, `Design.md`, visual tokens, component rules, page exceptions, and design contracts: use `ui-design-master`.
- HTML prototype skeletons, screen structure, route/page/module layout, and product HTML repair: use `html-skeleton-worker`.
- `Asset-Spec.md`, image/icon slots, asset rendering prompts, visual replacement rules, and asset coverage: use `visual-asset-rendering-master`.
- Concrete project handoff to developers, `Docs-Handoff.md`, canonical file maps, final audit, or Vibo coding notes: use `dev-handoff`.

## Full Workflow

For a complete product delivery path, move through:

1. `product-builder`
2. `interaction-designer`
3. `ui-design-master`
4. `html-skeleton-worker`
5. `visual-asset-rendering-master`
6. `dev-handoff`

Ask before advancing between major stages unless the user explicitly says to proceed automatically.

## Skill Maintenance Boundary

If the request is to modify skills, references, routing rules, metadata, or this router, do not run product stages. Treat it as skill maintenance and use `skill-creator` guidance.
