# Codex Skill for Product Managers

Turn rough product ideas into structured delivery artifacts with one reusable Codex skill.

面向产品经理的 Codex Skill，用来把模糊产品想法推进为可交付的产品文档、原型与开发交付材料。

This repository publishes a **Codex skill for product managers**. It is designed for **end-to-end product delivery work**: from product framing and PRD writing to interaction spec, UI direction, HTML prototype, `Design.md`, `Asset-Spec.md`, and developer handoff.

这是一个面向 **产品经理 / AI PM / 产品交付协作** 的 Codex skill，覆盖 **从产品想法到开发交付** 的整条工作链路：产品定义、PRD、交互说明、UI 方向、HTML 原型、`Design.md`、`Asset-Spec.md` 与开发交付。

> A Codex skill for product managers focused on end-to-end product delivery, from product ideas and PRDs to HTML prototypes, design contracts, asset specs, and developer handoff.

![Product delivery flow](./assets/readme/product-delivery-flow.svg)

## What This Repository Is

- A **Codex skill**, not just a prompt collection.
- Built for **product managers, AI PM workflows, and product delivery collaboration**.
- Designed to support both **full workflow execution** and **scoped repair work**.
- Structured so the reusable mechanism stays in the skill while project-specific files stay in project folders.

### Who This Is For | 适合谁用

- Product managers who want Codex to help move from idea to delivery.
- AI PM or prototyping workflows that need reusable product-delivery structure.
- Teams that want requirements, prototype, design contracts, and handoff materials to stay aligned.
- 希望用 Codex 把产品想法系统化推进到交付阶段的产品经理。
- 需要稳定产出 PRD、交互说明、HTML 原型与开发交付材料的 AI 协作流程。
- 希望把需求、原型、设计合同、资产合同和交付说明串成一条链路的团队。

## Why This Skill Exists

Product work often breaks between stages:

- requirements are written but are not implementation-ready
- UI ideas exist but are not translated into measurable prototype rules
- HTML is built without stable design or asset contracts
- project work gets repeated because standards live only inside one project

This skill exists to make the product-delivery chain reusable and operational inside Codex.

这个 skill 的目标不是提供一堆静态模板，而是把“产品需求到开发交付”的方法沉淀为一套可复用、可迭代、可被 Codex 实际执行的机制。

## What It Covers

![Operating modes](./assets/readme/operating-modes.svg)

### Full product delivery

Move from idea to handoff through a staged workflow:

`Idea -> PRD -> Interaction Spec -> UI Concept -> HTML Prototype -> Design.md -> Asset-Spec.md -> Developer Handoff`

### Stage-specific delivery

Use only one stage when needed, such as:

- PRD repair
- interaction repair
- UI concept work
- HTML prototype work
- design contract work
- asset contract work

### Screen-local refinement

Repair only one exact scope without reloading the whole workflow, for example:

- one screen
- one route
- one module
- one icon family
- one button family
- one asset batch

### Skill maintenance

Maintain the skill itself without triggering product-delivery stage gates.

## What This Skill Produces

![Deliverables overview](./assets/readme/deliverables-overview.svg)

Typical outputs include:

- `PRD.md`
- `Interaction-Spec.md`
- `UI concept directions`
- `Design.md`
- `Asset-Spec.md`
- `HTML prototypes`
- `Developer handoff notes`

## Why It Is Different From A Template Repo

- It routes requests by **work mode**, not by one static document template.
- It distinguishes **full delivery** from **one-screen repair**.
- It treats `Design.md` and `Asset-Spec.md` as **implementation contracts**, not optional notes.
- It keeps stage-gate confirmation for real product-delivery work while allowing continuous execution for skill maintenance.

## Best-Fit Use Cases

- turn a rough feature idea into a PRD and interaction spec
- create UI concept directions before prototyping
- build or repair high-fidelity HTML prototypes for phone, pad, TV, or web
- strengthen `Design.md` and `Asset-Spec.md` before asset replacement
- prepare developer handoff after product and prototype work are stable

## About This Repository | 仓库说明

**Description**

`A Codex skill for product managers focused on end-to-end product delivery, from product ideas and PRDs to HTML prototypes, design contracts, asset specs, and developer handoff.`

**Suggested Topics**

`codex`, `codex-skill`, `product-management`, `product-manager`, `product-delivery`, `prd`, `interaction-spec`, `html-prototype`, `design-system`, `developer-handoff`

## Install

### Install from GitHub into Codex

Current repository path:

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo YinHeBuilder/codex-product-delivery-skill \
  --path skills/product-requirements-prototyper
```

After installing, restart Codex.

### Manual install

Copy this folder:

```text
skills/product-requirements-prototyper
```

into:

```text
~/.codex/skills/product-requirements-prototyper
```

Then restart Codex.

## Example Prompts

```text
Use product-requirements-prototyper to turn this product idea into a PRD and interaction spec.
```

```text
Use product-requirements-prototyper to create a high-fidelity HTML prototype for this iPad story app.
```

```text
Use product-requirements-prototyper to repair only index.html#home and update the relevant Design.md and Asset-Spec.md rules.
```

```text
Use product-requirements-prototyper to prepare developer handoff materials from the current prototype folder.
```

## Repository Structure

```text
.
├── README.md
├── LICENSE
├── assets/
│   └── readme/
└── skills/
    └── product-requirements-prototyper/
        ├── SKILL.md
        ├── agents/
        │   └── openai.yaml
        ├── references/
        └── assets/
```

## Repository Naming

The repository is now named `codex-product-delivery-skill`, which is much clearer for new visitors because it exposes all three key concepts immediately:

- `Codex`
- `skill`
- `product delivery`

Also good:

- `codex-pm-delivery-skill`
- `codex-skill-product-manager`

Why this matters:

- `Codex` should appear in the repository name
- `product delivery` or `product manager` should appear in the repository name
- visitors should understand within seconds that this is a **Codex skill for product delivery work**

## Skill Location

The actual published skill lives here:

- [skills/product-requirements-prototyper](./skills/product-requirements-prototyper/)

## Notes

- Keep project-specific decisions in project files, not in the skill.
- Keep skill references reusable and project-neutral.
- Stage Gate is preserved for actual product-delivery work.
- Skill maintenance should run continuously unless the user explicitly asks for step-by-step confirmation.

## Bilingual README Note | 关于中英双语

This README intentionally mixes English and Chinese in key sections so both Chinese-speaking and international users can understand the role of the repository quickly.

这个 README 有意识地在关键位置采用中英双语，是为了让中文用户和海外用户都能快速看懂这个仓库的定位、作用和安装方式。
