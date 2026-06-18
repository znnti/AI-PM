---
name: html-skeleton-worker
description: Build, inspect, or repair HTML skeletons and prototypes for app, web, pad, TV, or phone screens. Use for index.html, phone.html, pad.html, tv.html, web.html, route anchors, screen-local refinement, CSS/layout repair, prototype structure, and audit against Design.md or Asset-Spec.md. Do not use for slide presentations, PRD-only work, visual direction, asset rendering inventory, or final developer handoff.
---

# HTML Skeleton Worker

## Introduction

This skill is the hands-on HTML worker. It turns product, interaction, and UI contracts into concrete screen skeletons, routes, modules, and repairable prototype structure.

## Scope

- Build or repair HTML skeletons, prototypes, and exact screen/route/module scopes.
- Default to one screen, one route, or one device page at a time.
- Use `references/html-prototype-guide.md`.
- Use `references/change-impact-guide.md` when HTML changes affect requirements, interaction, UI rules, assets, or handoff files.
- Use `assets/html-prototype-template/` only when starting a new prototype.

## Required Checks

- Before high-fidelity HTML, confirm `Design.md` and `Asset-Spec.md` are sufficient for the in-scope screen.
- Prefer page-level contracts over broad project docs during local repair.
- After editing, verify the changed region against `Design.md`, `Asset-Spec.md`, and relevant page contracts.
- Do not use slide-deck navigation or presentation structure for product prototypes.

## Boundaries

- Do not create PRD, full interaction specs, UI concept prompts, asset inventory, or handoff files unless the user explicitly asks for adjacent work.
- For presentation-like HTML, use `html-presentation-designer` instead.

## Completion

Summarize the screen or route changed, verification performed, remaining placeholders, and contract files that should be updated next. If visual assets are next, recommend:

`visual-asset-rendering-master`

https://github.com/YinHeBuilder/codex-product-delivery-skill/tree/main/skills/visual-asset-rendering-master
