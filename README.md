# Codex Product Delivery Skills

A modular Codex skill set for product delivery. Instead of one large product-management skill handling every stage, this repository now publishes a lightweight router plus focused stage skills.

这是一组面向产品交付的 Codex skills。新版不再把 PRD、交互、UI、HTML、设计规范、资产规范和开发交付全部塞进一个大 skill，而是按阶段拆成多个小 skill，由路由 skill 判断该调用哪一个。

## Skill Set

| Skill | Purpose |
| --- | --- |
| `product-requirements-prototyper` | Lightweight router for broad or ambiguous product requests |
| `product-prd-writer` | PRD, product scope, requirements, assumptions, acceptance criteria |
| `product-interaction-spec` | Flows, screen states, navigation, validation, permissions, edge cases |
| `product-ui-concept` | UI directions, visual references, page effect notes, image prompts |
| `product-html-prototype` | Product HTML prototype creation, inspection, and screen-local repair |
| `product-design-contract` | `Design.md`, tokens, component rules, layout contracts, page exceptions |
| `product-asset-spec` | `Asset-Spec.md`, asset slots, placeholder rules, replacement prompts |
| `product-dev-handoff` | Concrete product-project handoff to developers or Vibo coding workflows |

## Why It Is Split

The previous `product-requirements-prototyper` workflow became too large. It could load broad product-delivery rules even when the user only wanted one small stage.

The new design keeps triggering more precise:

- PRD work calls the PRD skill only.
- HTML repair calls the HTML skill only.
- Developer handoff is only used for concrete product projects, not skill updates.
- Skill maintenance should use `skill-creator`, not product-delivery stages.
- The router exists only to classify broad requests and point Codex to the right focused skill.

## Typical Routing

Use `product-requirements-prototyper` when the request is broad or unclear:

```text
Use product-requirements-prototyper to route this product request and continue with the right focused skill.
```

Use a focused skill directly when the stage is clear:

```text
Use product-prd-writer to turn this feature idea into PRD.md.
```

```text
Use product-html-prototype to repair index.html#home and verify it against Design.md and Asset-Spec.md.
```

```text
Use product-dev-handoff to prepare this concrete product project for developer implementation.
```

## Install

Install or copy every folder under `skills/` into `~/.codex/skills/`, then restart Codex.

Manual install:

```bash
cp -R skills/product-* ~/.codex/skills/
```

## Repository Structure

```text
.
├── README.md
├── LICENSE
├── assets/
│   └── readme/
└── skills/
    ├── product-requirements-prototyper/
    ├── product-prd-writer/
    ├── product-interaction-spec/
    ├── product-ui-concept/
    ├── product-html-prototype/
    ├── product-design-contract/
    ├── product-asset-spec/
    └── product-dev-handoff/
```

## Notes

- Keep project-specific decisions in project folders, not inside skills.
- Keep each skill small and stage-specific.
- Use `product-dev-handoff` only for real product-project handoff.
- Use `skill-creator` for maintaining or refactoring these skills.
- `product-requirements-prototyper` is now a router, not the full workflow engine.
