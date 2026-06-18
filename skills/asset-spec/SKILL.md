---
name: asset-spec
description: Create, repair, or audit asset specifications such as Asset-Spec.md, image/icon/avatar/cover/illustration slots, placeholder inventories, asset dimensions, crop rules, replacement constraints, and image-generation prompts. Use when Codex needs asset planning or asset-slot coverage for HTML. Do not use for PRD writing, flow design, HTML coding, design-token work, or developer handoff.
---

# Asset Spec

## Introduction

This skill defines the asset contract. It inventories image, icon, avatar, cover, illustration, and decorative slots so assets can be generated or replaced without breaking layout.

## Scope

- Create or repair `Asset-Spec.md`.
- Inventory visible icon, cover, illustration, avatar, play-button, empty-state, and decorative slots.
- Bind each slot to component/region, size, format, crop/anchor, overflow, state usage, and replacement constraints.
- Default to one screen or one asset group at a time.
- Use `references/asset-spec-guide.md`.
- Use `references/change-impact-guide.md` when asset changes affect HTML, design, interaction, or handoff files.

## Boundaries

- Do not build HTML unless the user asks to fill or repair the exact asset slot in code.
- Do not create Design.md except when asset dimensions reveal a missing design rule.
- Do not prepare developer handoff.

## Completion

Summarize covered slots, missing assets, prompt groups, and any HTML/design follow-up. If the product package is ready for developers, recommend installing or using `dev-handoff`:

`https://github.com/YinHeBuilder/codex-product-delivery-skill/tree/main/skills/dev-handoff`
