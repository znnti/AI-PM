# Codex Delivery Skills

A modular Codex skill set for staged product delivery. Each skill acts like a role in a product team, and `delivery-router` decides which role should step in.

这是一组按产品团队角色拆分的 Codex skills。每个 skill 只负责一个明确阶段，`delivery-router` 负责判断谁该介入，不承载完整大流程。

## Skill Set

| Skill | Role | When it steps in |
| --- | --- | --- |
| `delivery-router` | Router | Broad or ambiguous delivery requests |
| `product-builder` | Product Builder | Ideas, PRD, scope, requirements, acceptance criteria |
| `interaction-designer` | Interaction Designer | Flows, navigation, screen states, permissions, edge cases |
| `ui-design-master` | UI Design Master | UI direction, visual language, `Design.md`, component rules |
| `html-skeleton-worker` | HTML Skeleton Worker | HTML skeletons, product screens, routes, modules, layout repair |
| `visual-asset-rendering-master` | Visual Asset Rendering Master | `Asset-Spec.md`, asset slots, visual rendering prompts, replacement rules |
| `dev-handoff` | Dev Handoff | Concrete project handoff, `Docs-Handoff.md`, implementation notes, final audit |

## Workflow

Recommended order:

```text
product-builder
-> interaction-designer
-> ui-design-master
-> html-skeleton-worker
-> visual-asset-rendering-master
-> dev-handoff
```

Each role stops after its own stage and recommends the next skill with its GitHub folder URL. It should not automatically enter the next stage unless the user asks.

## Why It Is Split

The old single skill was too large. It could pull PRD, interaction, UI, HTML, design, asset, and handoff rules into context even when the user only needed one stage.

The new role-based design keeps triggering precise:

- Product shaping calls `product-builder`.
- Interaction behavior calls `interaction-designer`.
- UI direction and visual contract work call `ui-design-master`.
- HTML screen structure calls `html-skeleton-worker`.
- Asset slots and rendering prompts call `visual-asset-rendering-master`.
- Concrete project handoff calls `dev-handoff`.
- Skill maintenance should use `skill-creator`, not these delivery skills.

## Typical Use

Use the router when the request is broad:

```text
Use $delivery-router to route this product request and continue with the right role skill.
```

Use a role skill directly when the stage is clear:

```text
Use $product-builder to shape this idea into PRD.md.
```

```text
Use $interaction-designer to define the flows, screen states, and edge cases.
```

```text
Use $ui-design-master to define the visual direction and Design.md rules.
```

```text
Use $html-skeleton-worker to repair index.html#home and verify it against Design.md and Asset-Spec.md.
```

```text
Use $visual-asset-rendering-master to inventory asset slots and prepare rendering prompts.
```

```text
Use $dev-handoff to prepare this concrete project for developer implementation.
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
    ├── product-builder/
    ├── interaction-designer/
    ├── ui-design-master/
    ├── html-skeleton-worker/
    ├── visual-asset-rendering-master/
    └── dev-handoff/
```

## Notes

- Keep project-specific decisions in project folders, not inside skills.
- Keep each role skill small and stage-specific.
- Use `dev-handoff` only for real project handoff.
- Use `skill-creator` for maintaining or refactoring these skills.
- `delivery-router` is a router, not a full workflow engine.
