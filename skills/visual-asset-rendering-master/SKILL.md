---
name: visual-asset-rendering-master
description: Master visual asset planning and rendering. Use when Codex needs Asset-Spec.md, image/icon/avatar/cover/illustration slots, placeholder inventories, asset dimensions, crop rules, replacement constraints, visual rendering prompts, or asset coverage for HTML. Do not use for PRD writing, interaction design, raw HTML skeleton work, design-token work, or developer handoff.
---

# Visual Asset Rendering Master

## Introduction

This skill owns the visual asset layer. It defines asset slots and rendering prompts so images, icons, covers, illustrations, and decorative assets can be produced or replaced without breaking the product layout.

## Scope

- Create or repair `Asset-Spec.md`.
- Inventory visible icon, cover, illustration, avatar, play-button, empty-state, and decorative slots.
- Bind each slot to component/region, size, format, crop/anchor, overflow, state usage, and replacement constraints.
- Create concise visual rendering prompts for asset generation when requested.
- Default to one screen or one asset group at a time.
- Use `references/asset-spec-guide.md`.
- Use `references/change-impact-guide.md` when asset changes affect HTML, UI design, interaction, or handoff files.

## Boundaries

- Do not build HTML unless the user asks to fill or repair the exact asset slot in code.
- Do not create `Design.md` except when asset dimensions reveal a missing visual rule.
- Do not prepare developer handoff.

## Completion

Summarize covered slots, missing assets, rendering prompt groups, and HTML/design follow-up. If the product package is ready for developers, recommend:

`dev-handoff`

https://github.com/YinHeBuilder/codex-product-delivery-skill/tree/main/skills/dev-handoff
