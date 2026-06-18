---
name: html-prototype
description: Build, inspect, or repair HTML prototypes for app, web, pad, TV, or phone screens. Use for index.html, phone.html, pad.html, tv.html, web.html, route anchors, screen-local refinement, CSS/layout repair, prototype behavior, and HTML audit against Design.md or Asset-Spec.md. Do not use for slide presentations, PRD-only work, asset-generation planning, or final developer handoff.
---

# HTML Prototype

## Introduction

This skill implements and repairs product screens in HTML. It is the right skill for concrete pages, routes, modules, CSS layout, prototype behavior, and screen-local refinement.

## Scope

- Build or repair HTML prototypes and exact screen/route/module scopes.
- Default to one screen, one route, or one device page at a time.
- Use `references/html-prototype-guide.md`.
- Use `references/change-impact-guide.md` when HTML changes affect requirements, interaction, design, assets, or handoff files.
- Use `assets/html-prototype-template/` only when starting a new prototype.

## Required Checks

- Before high-fidelity HTML, confirm `Design.md` and `Asset-Spec.md` are sufficient for the in-scope screen.
- Prefer page-level contracts over broad project docs during local repair.
- After editing, verify the changed region against `Design.md`, `Asset-Spec.md`, and relevant page contracts.
- Do not use slide-deck navigation or presentation structure for product prototypes.

## Boundaries

- Do not create PRD, interaction spec, visual concept prompts, asset inventory, or handoff files unless the user explicitly asks for that adjacent work.
- For presentation-like HTML, use `html-presentation-designer` instead.

## Completion

Summarize the screen or route changed, verification performed, remaining temporary placeholders, and any contract files that should be updated next. If measured design rules are next, recommend `design-contract`; if asset slots are next, recommend `asset-spec`:

`https://github.com/YinHeBuilder/codex-product-delivery-skill/tree/main/skills/design-contract`

`https://github.com/YinHeBuilder/codex-product-delivery-skill/tree/main/skills/asset-spec`
