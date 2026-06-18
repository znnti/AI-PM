# Codex Delivery Skills

A modular Codex skill set for staged product delivery. Each stage is a small focused skill, and `delivery-router` only decides which skill should do the work.

这是一组按阶段拆分的 Codex skills。每个 skill 只负责一个明确阶段，`delivery-router` 只做判断和路由，不再承载完整大流程。

## Skill Set

| Skill | Introduction | Next step |
| --- | --- | --- |
| `delivery-router` | Routes broad or ambiguous delivery requests to the right focused skill. | Use the selected stage skill |
| `prd-writer` | Turns ideas, notes, and messy requirements into `PRD.md`. | `interaction-spec` |
| `interaction-spec` | Defines flows, screen states, navigation, validation, permissions, and edge cases. | `ui-concept` |
| `ui-concept` | Explores UI direction, visual references, page effect notes, and image prompts. | `html-prototype` or `design-contract` |
| `html-prototype` | Builds or repairs concrete HTML screens, routes, modules, and prototype behavior. | `design-contract` or `asset-spec` |
| `design-contract` | Owns `Design.md`, tokens, component rules, layout constraints, and page exceptions. | `asset-spec` |
| `asset-spec` | Defines `Asset-Spec.md`, asset slots, dimensions, crop rules, and replacement prompts. | `dev-handoff` |
| `dev-handoff` | Prepares a concrete project for developer or Vibo coding handoff. | Final stage |

## Why It Is Split

The old single skill was too large. It could pull PRD, interaction, UI, HTML, design, asset, and handoff rules into context even when the user only needed one stage.

The new design keeps triggering precise:

- PRD work calls `prd-writer`.
- Interaction work calls `interaction-spec`.
- UI direction calls `ui-concept`.
- HTML screen work calls `html-prototype`.
- Design rules call `design-contract`.
- Asset slots call `asset-spec`.
- Concrete project handoff calls `dev-handoff`.
- Skill maintenance should use `skill-creator`, not these delivery skills.

## Typical Use

Use the router when the request is broad:

```text
Use $delivery-router to route this product request and continue with the right focused skill.
```

Use a focused skill directly when the stage is clear:

```text
Use $prd-writer to turn this feature idea into PRD.md.
```

```text
Use $html-prototype to repair index.html#home and verify it against Design.md and Asset-Spec.md.
```

```text
Use $dev-handoff to prepare this concrete project for developer implementation.
```

## Stage Recommendation Pattern

Each stage skill should stop after its own stage and recommend the next skill only when useful. It should provide the GitHub folder URL, but it should not automatically enter the next stage unless the user asks.

Example:

```text
Next recommended skill: interaction-spec
https://github.com/YinHeBuilder/codex-product-delivery-skill/tree/main/skills/interaction-spec
```

## Install

Install or copy every folder under `skills/` into `~/.codex/skills/`, then restart Codex.

Manual install:

```bash
cp -R skills/* ~/.codex/skills/
```

## Repository Structure

```text
.
├── README.md
├── LICENSE
├── assets/
│   └── readme/
└── skills/
    ├── delivery-router/
    ├── prd-writer/
    ├── interaction-spec/
    ├── ui-concept/
    ├── html-prototype/
    ├── design-contract/
    ├── asset-spec/
    └── dev-handoff/
```

## Notes

- Keep project-specific decisions in project folders, not inside skills.
- Keep each skill small and stage-specific.
- Use `dev-handoff` only for real project handoff.
- Use `skill-creator` for maintaining or refactoring these skills.
- `delivery-router` is a router, not a full workflow engine.
