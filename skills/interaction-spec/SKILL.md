---
name: interaction-spec
description: Create, repair, or audit interaction specifications for flows, screen states, navigation, validation, permissions, empty/loading/error states, and edge cases. Use when Codex needs Interaction-Spec.md or behavior-level updates. Do not use for visual style exploration, HTML implementation, asset planning, or developer handoff.
---

# Interaction Spec

## Introduction

This skill defines how the product behaves. It turns requirements into flows, screen states, navigation rules, edge cases, and interaction details that later design and HTML work can implement.

## Scope

- Create or repair `Interaction-Spec.md`.
- Define flows, screens, states, navigation, permissions, validation, errors, empty states, loading states, and recovery paths.
- Read current `PRD.md` sections only when behavior depends on requirements.
- Use `references/interaction-spec.md` as the structure guide.
- Use `references/change-impact-guide.md` when behavior changes require updates to PRD, HTML, design, assets, or handoff files.

## Boundaries

- Do not choose visual style unless the user asks for UI direction.
- Do not code HTML.
- Do not generate assets or final handoff.

## Completion

Summarize the flows or states changed, files touched, assumptions, and open behavior questions. If visual direction is next, recommend installing or using `ui-concept`:

`https://github.com/YinHeBuilder/codex-product-delivery-skill/tree/main/skills/ui-concept`
