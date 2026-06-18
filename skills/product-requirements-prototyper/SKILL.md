---
name: product-requirements-prototyper
description: Turn product ideas, feature requests, rough requirements, or existing product artifacts into scoped product deliverables. Use when Codex needs to create or repair PRDs, interaction specs, user flows, information architecture, UI concept directions, image-generation prompts, multi-device HTML prototypes for phone, pad, TV, or web, Design.md and Asset-Spec.md contracts, screen-local product UI, or developer handoff materials for Vibo coding and implementation teams.
metadata:
  version: 0.2.0
---

# Product Requirements Prototyper

## Overview

Use this skill to turn a rough product thought into a product package that a designer, engineer, or AI coding workflow can act on. Produce structured documents first, then representative UI concepts, then coded HTML prototypes for the target devices.

For full product-manager delivery tasks, follow `references/full-product-delivery-workflow.md` as the end-to-end operating method. Keep reusable workflow and quality standards in this skill; keep project-specific content such as PRDs, HTML files, asset inventories, image prompts, and generated images inside the project folder.

Skill reference files must stay project-neutral. Do not add product-specific examples, asset names, screen copy, visual themes, or generated project decisions into this skill. Store those details in the active project's `PRD.md`, `Interaction-Spec.md`, `Design.md`, `Asset-Spec.md`, prototype files, or handoff notes instead.

## Operating Modes

This skill should behave like a lightweight router first and a heavy workflow only when needed. Do not load the whole skill body for every request.

At the start of each request, classify the work into exactly one of these modes:

- **Full product delivery**: end-to-end product work from idea or rough requirements toward documents, UI direction, HTML, assets, and handoff.
- **Stage-specific delivery**: the user wants one stage only, such as PRD repair, interaction repair, UI concept, HTML prototype, `Design.md`, `Asset-Spec.md`, or handoff.
- **Screen-local refinement**: the user wants to repair one concrete screen, route, or module, such as `#home`, `#detail`, `#player`, one card family, one button group, one asset group, or one device page.
- **Skill maintenance**: the user wants to modify this skill, its references, routing rules, or guidance.

Mode selection controls how much context may be loaded:

- Full product delivery may load the relevant stage references one by one as the workflow advances.
- Stage-specific delivery must load only the active stage reference plus the directly required project files.
- Screen-local refinement must prefer page-level contract files and the exact HTML/CSS/asset scope. Do not re-read PRD, interaction, or unrelated stage references unless the current repair truly depends on them.
- Skill maintenance must read only the skill files being edited.

## Stage Gate Workflow

Use Stage Gate to control transitions between product-delivery stages. The user may begin from any stage. Do not generate the entire product package blindly unless the user explicitly authorizes automatic progression.

Stage Gate applies when a completed product-delivery stage would advance into a different stage: PRD, interaction spec, UI concept, HTML prototype, Design.md, Asset-Spec.md, asset generation/replacement, or developer handoff.

Do not emit a Stage Gate after every screen-local correction, feedback turn, or continuation inside the same requested stage. Continue within the named screen/module and summarize normally. Emit a gate only when the current stage is complete and another stage is proposed, when moving to another screen requires user scope approval, or when the user explicitly asks for phased confirmation.

For high-fidelity HTML and asset work, Stage Gate alone is not enough. Default execution unit must also shrink to one page, one screen, or one local route at a time unless the user explicitly asks for multi-screen batching or full auto mode. Do not silently code or fill every screen in a long prototype in one pass just because the project contains multiple pages.

Stage Gate does not apply when the user is maintaining this skill itself. If the request is to maintain, modify, refactor, repair, or tune `product-requirements-prototyper` rules, `SKILL.md`, references, skill metadata, or skill guidance, treat it as a skill-maintenance task:

- Do not route the work into Stage 1-7.
- Do not pause after each edited skill file or rule section.
- Do not create or continue project deliverable documents.
- Modify all necessary skill files and references in one pass when possible.
- Report once at the end with files changed and the new operating rule.
- Only pause for step-by-step confirmation during skill maintenance if the user explicitly asks for "分阶段确认", "每步确认", or equivalent.

### Stage Order

- **Stage 0: Workflow Routing / 阶段判断**
- **Stage 1: PRD / 产品需求文档**
- **Stage 2: Interaction Spec / 交互说明**
- **Stage 3: UI Concept / UI 风格方向**
- **Stage 4: HTML Prototype / HTML 原型**
- **Stage 5: Design System / 高保真设计规范**
- **Stage 6: Asset Spec / 资产规格**
- **Stage 7: Developer Handoff / 开发交付**

### Stage 0 Routing

At the start of each request, determine the current stage from the user's wording and available project files.

- If the user asks to maintain, modify, refactor, repair, or tune this skill, `SKILL.md`, references, Stage Gate rules, reference loading rules, or skill guidance, classify the request as **skill maintenance**, not product delivery. In skill maintenance mode, skip Stage 0-7 routing and complete the requested skill edits without Stage Gate pauses unless the user explicitly asks for staged confirmation.
- If the user asks to repair one named screen, route, anchor, device page, or module such as `#home`, `#detail`, `#player`, `phone.html`, one card family, one icon group, or one button group, classify the request as **screen-local refinement** first. In this mode, do not auto-load the whole product workflow. Read only the exact screen HTML, the relevant contract files, and the relevant asset rows.
- If the user asks for high-fidelity HTML skeleton build or asset fill without clearly limiting the scope, default to **page-by-page execution**: finish one named screen, route, or device page first, summarize it, then ask whether to continue with the next page unless the user already approved automatic multi-page progression.

- If the user asks for requirements, product scope, acceptance criteria, or PRD repair, route to Stage 1.
- If the user asks for flows, states, paths, edge cases, screen behavior, or interaction repair, route to Stage 2.
- If the user asks for visual directions, UI styles, effect prompts, reference-image analysis, or style selection, route to Stage 3.
- If the user asks to build, repair, or inspect an HTML prototype, route to Stage 4.
- If the user asks for measured visual rules, layout contract, design tokens, or `Design.md`, route to Stage 5.
- If the user asks for asset slots, placeholder inventories, image-generation prompts, or `Asset-Spec.md`, route to Stage 6.
- If the user asks for implementation notes, Vibo handoff, developer instructions, or final package handoff, route to Stage 7.

Use this skill, not `html-presentation-designer`, for product HTML coding: app/web/pad/TV prototypes, HTML skeletons, high-fidelity UI repair, `Design.md`-driven layout work, asset placeholders, and product handoff. `html-presentation-designer` is only for slide-like presentation HTML such as PPT-style reports, talks, and article-to-slides work.

Support starting from any stage. For example, if the user says "根据这个 PRD 做 HTML 原型", treat the current stage as Stage 4, read only HTML-prototype references plus the provided/project PRD as source material, list assumptions for missing interaction details, and do not force a return to Stage 1 unless the user asks.

### Stage Gate Rule

After completing a product-delivery stage, output a Stage Gate summary only when proposing a transition into another stage. Do not automatically enter the next product-delivery stage unless the user clearly says one of: "继续下一步", "直接推进完整流程", "不要每步确认", "不用每一步问我", "中间不用确认", or "全部自动完成".

For a stage-specific request, finish the requested stage and stop without asking to enter another stage unless a next-stage recommendation is materially useful. For screen-local refinement, continue same-screen feedback without gates; use one completion summary when the screen reaches a stable or verified state.

Do not use this Stage Gate template for skill-maintenance tasks. For skill maintenance, make the requested `SKILL.md` and reference edits continuously and provide one final summary.

The Stage Gate summary must include:

- current completed stage name
- files generated or modified in this stage
- key conclusions from this stage
- gaps or questions that still need confirmation
- recommended next stage
- a direct question asking whether to continue into the next stage

Use this fixed reply template:

```text
【阶段完成】
当前阶段：Stage X - 阶段名称
已完成内容：
- ...
生成/修改文件：
- ...
待确认问题：
- ...
建议下一步：
- 推荐进入 Stage Y - 阶段名称
是否继续进入下一阶段？也可以选择回到上一个阶段补充。
```

When the user authorizes automatic progression, stages may continue without waiting after each gate, but each stage must still record a concise completion summary before moving on.

### Backtracking Rule

If the user says "补一下 PRD", "前面的交互说明不完整", "回到 UI 风格方向重新选", "先别做原型，先完善需求", "补充上一个环节", or similar, pause the current stage and return to the requested earlier stage.

After backtracking work is complete, run the Stage Gate again and ask whether to:

- return to the interrupted stage
- continue to the next stage from the revised point
- save the revision only and stop

Do not keep advancing the interrupted stage while repairing the earlier stage.

### Allowed Stage Transitions

Default allowed forward transitions:

- Stage 1 -> Stage 2
- Stage 2 -> Stage 3
- Stage 3 -> Stage 4
- Stage 4 -> Stage 5
- Stage 4 -> Stage 6
- Stage 5 -> Stage 6
- Stage 6 -> Stage 7

The user may actively skip stages. When skipping, state the risk before proceeding. For example, if there is no interaction spec and the user wants HTML anyway, say: "可以继续，但部分页面状态、错误态、空状态可能需要基于合理假设生成。"

### Missing Information Rule

If a stage lacks upstream materials, do not stop the task and do not force the user to restart from Stage 1. Create a usable version from available information, explicitly list assumptions, mark what needs later supplementation, and remind the user at the Stage Gate that they can backtrack to fill gaps.

### Reference Loading Rules

Load only the references needed for the current stage. If the user backtracks, load only the reference for the requested earlier stage and any directly required source files; do not re-read every reference file.

- Stage 0: `references/full-product-delivery-workflow.md` only when routing is unclear or a full workflow is requested.
- Stage 1: `references/prd-outline.md`.
- Stage 2: `references/interaction-spec.md`.
- Stage 3: `references/ui-concept-guide.md`.
- Stage 4: `references/html-prototype-guide.md` and the HTML template assets only when coding HTML.
- Stage 5: `references/design-system-guide.md`.
- Stage 6: `references/asset-spec-guide.md`.
- Stage 7: `references/vibo-coding-handoff.md`.
- Cross-document repair or handoff audit: `references/change-impact-guide.md`.

For full auto mode, load each stage's reference just before executing that stage.

### Minimal Read Matrix

Use this matrix to reduce overhead. Do not exceed it unless the current task is blocked without more context.

- **Full product delivery**: current stage reference + direct upstream project files for that stage.
- **PRD repair**: `references/prd-outline.md` + current `PRD.md` + only the user-provided source notes.
- **Interaction repair**: `references/interaction-spec.md` + current `Interaction-Spec.md` + relevant `PRD.md` sections.
- **UI concept work**: `references/ui-concept-guide.md` + current visual checkpoint materials + only the screens in scope.
- **HTML screen repair**: `references/html-prototype-guide.md` + exact HTML file/anchor + relevant `Design.md`, `Asset-Spec.md`, and page-level contract files.
- **Design repair**: `references/design-system-guide.md` + current `Design.md` + exact screen HTML + page-level contracts.
- **Asset repair**: `references/asset-spec-guide.md` + current `Asset-Spec.md` + exact screen HTML + only the relevant asset group.
- **Developer handoff**: `references/vibo-coding-handoff.md` + the actual files being handed off.
- **Cross-document change**: `references/change-impact-guide.md` + only the files selected by its impact matrix.
- **Skill maintenance**: only the skill files being edited.

If the project already has page-level contract files such as `Button-Contract.md`, `Card-Contract.md`, `Icon-Control-Contract.md`, `Typography-Contract.md`, `Surface-Shadow-Contract.md`, or `Player-Contract.md`, prefer those over re-reading broad project documents during screen-local refinement.

For high-fidelity product UI work, do not treat Stage 4 HTML, Stage 5 `Design.md`, and Stage 6 `Asset-Spec.md` as isolated deliverables. They form one control loop:

- `Design.md` defines reusable visual and component rules.
- `Asset-Spec.md` defines slot-by-slot asset contracts.
- HTML implements both and must be checked against both.

Before creating a new page or editing high-fidelity HTML, run a **Design Contract Preflight**:

- Confirm `Design.md` has global tokens, component standards, screen-specific rules, a page exception mechanism, and a QA checklist for the in-scope screen or module.
- Confirm page rules inherit global tokens and component contracts first. A new page must start from `Design.md`, not from a screenshot or one-off CSS guesses.
- If the user gives an explicit special requirement for one page, module, or state, implement that requirement locally and record it as a screen rule or page exception. Do not promote it into a global token or component standard unless the user explicitly asks for a global rule such as "以后都这样" or "作为通用规范".
- If `Design.md` is missing the needed global/component rule, update `Design.md` or the relevant contract before editing HTML. Do not encode undocumented design assumptions directly in CSS.
- After editing HTML, audit the changed region back against `Design.md`, `Asset-Spec.md`, and any page-level contracts; remove or revise stale rules that would recreate the old state.

If this loop is weak, strengthen the skill-level rules and references instead of only patching one project's markdown files.


## Deliverable Modes

Choose the output mode from the user's request. If the user says “完整一点” or gives a new product idea without constraints, use Full Package.

- **Lean Product Brief**: concise PRD sections, core flow, screen list, and next questions.
- **Full Package**: PRD, interaction spec, UI concept prompts, multi-device HTML prototype, and Vibo coding handoff.
- **Prototype First**: fast IA, core flow, and HTML prototype before long-form documentation.
- **Handoff Repair**: improve existing docs or HTML so a technical teammate can implement from them.

Do not use presentation-deck structures for product prototypes. A product prototype should start on the actual product screen, preserve product navigation and states, and be organized around screens, regions, assets, and flows rather than slides, page numbers, or keyboard-based presentation navigation.

## Product Reasoning Rules

- Follow a standard PRD structure and write from user value, business goal, system behavior, data rule, permission rule, and acceptance criteria angles.
- Separate product truth from assumptions. Use an `Assumptions` section when details are inferred.
- Convert vague ideas into scenarios and jobs-to-be-done before writing screens.
- Keep requirements testable. Prefer observable behavior over abstract intent.
- Include edge states, empty states, loading states, permissions, errors, and recovery paths for important flows.
- Derive UI style from product scenario, user profile, device context, content density, and comparable products; do not force a fixed visual style.
- When competitor or comparable-product research materially affects UI decisions, browse current references or ask the user for examples before finalizing the direction.
- Confirm UI style before page-by-page UI effect generation; confirm page UI effects before HTML coding.
- Treat UI images as concept references, not implementation specs. The HTML prototype is the implementation-facing artifact.
- For high-fidelity HTML, translate confirmed UI effects into measured layout constraints: canvas size, grid columns, block heights, typography scale, baseline alignment, spacing, border radius, and placeholder dimensions. Do not rely on "looks similar" judgment alone.
- Create `Design.md` for each high-fidelity project after UI effects are approved and before coding or repairing HTML. Treat it as the project-level visual contract.
- Treat `Design.md` as a required implementation contract, not an optional style memo. For high-fidelity work it must define the component system, including button variants, usage rules, sizing, spacing, icon/text equations, text-wrap policy, and state rules strongly enough that HTML can be audited against it.
- Maintain `Design.md` with a clear hierarchy: global tokens and component contracts first, page/screen rules second, asset slot rules third. Page-specific user requests are local exceptions by default; they must not rewrite global standards unless explicitly promoted by the user.
- Keep `Design.md` and HTML in sync. If HTML changes reveal a better layout rule, update `Design.md`; if `Design.md` changes, update the HTML.
- Use green dashed placeholders for unfinished image/icon slots during layout validation. Keep icon, cover, illustration, avatar, and play-button slots empty until the layout skeleton is approved.
- Treat `Asset-Spec.md` as a slot contract, not only an asset list. It must bind each visible slot to component/region, size, format, crop/anchor, overflow, state usage, and replacement constraints so later asset work cannot silently change layout.
- Do not start or finish high-fidelity HTML on undocumented visual assumptions. Before coding, confirm that `Design.md` and `Asset-Spec.md` are sufficiently defined for the in-scope screens; before closing, audit the HTML against those files and record any missing rule that caused drift.
- When building prototypes, make the first screen the actual product experience, not a marketing landing page.
- For phone, pad, TV, and web, adapt information density, navigation, input method, and layout rather than simply resizing the same page.

## Scope And Coverage Discipline

Every stage must include a small review loop: define scope, execute against a checklist, then audit coverage before handing off.

Apply this discipline to PRDs, interaction specs, UI concepts, page effect prompts/images, full effect sets, Design.md, HTML skeletons, Asset-Spec.md, asset generation/replacement, and developer handoff.

Before executing a stage:

- Restate the requested scope: one feature, one flow, one screen, one device, one module, one asset type, or the full project package.
- Read the relevant current project files instead of relying on prior-turn memory.
- Build a coverage checklist for the stage. Examples: PRD sections, interaction states, pages/devices, UI effect screens, HTML regions, asset slots, handoff files.

During execution:

- Work from the checklist, not from the most visually prominent or most recently discussed item.
- If the user changes scope midstream, run a compensation pass over adjacent requirements, interactions, layout, assets, and docs.
- Use `references/change-impact-guide.md` to select which project contracts must change; do not update every document reflexively.

Before final response:

- Re-read or search the affected files to confirm every checklist item was handled.
- Update the project contract files that changed: `PRD.md`, `Interaction-Spec.md`, `Design.md`, `Asset-Spec.md`, prototype files, or handoff notes.
- State any intentionally out-of-scope or still-temporary items explicitly.

This rule exists because product work spans multiple turns. Do not assume earlier context is complete enough to decide current coverage.

For screen-local refinement, shrink the checklist to the local scope. Example: one page, one module, one icon family, one button family, or one asset batch. Do not expand a local repair into a full project audit unless the user asks or a discovered dependency makes it necessary.

For high-fidelity HTML skeleton work and placeholder-to-asset replacement, treat "one screen/page at a time" as the default safe operating mode:

- Start with a lightweight global scan before the first deep page pass. Identify the in-scope pages, routes, modules, key states, and known contract gaps without fully loading every page implementation.
- Build or repair one screen, route, or device page first.
- Update the local `Design.md` and `Asset-Spec.md` coverage for that page in the same pass.
- Summarize page completion before moving to the next page.
- Only batch multiple pages continuously when the user explicitly says to do so, or when a resumable page checklist has already been created and the user approved automatic progression.

If the project is large and the user wants less manual intervention, use a resumable automation pattern instead of one giant pass:

- create a screen inventory
- keep the inventory lightweight; do not fully re-read every page on every turn
- mark each screen with status such as `pending`, `in_progress`, `skeleton_done`, `asset_ready`, `asset_filled`, `verified`
- process pages sequentially against that ledger
- re-read the current page contract files before each page pass
- after finishing one page, return to the ledger and choose the next page intentionally instead of relying on conversational memory

This keeps long conversations from losing requirements when context compresses or folds.

Recommended ledger fields:

- `screen`
- `route_or_anchor`
- `device`
- `status`
- `depends_on`
- `design_contract_status`
- `asset_spec_status`
- `open_questions`
- `next_action`

The ledger is the project-memory layer. The single-page pass is only the execution layer.

### Standard Screen Ledger Template

When multi-screen HTML or asset work spans multiple turns, create or update a `Screen-Ledger.md` or an equivalent section in project notes before the first deep page pass.

Use this fixed header order:

```md
| Screen | Route / Anchor | Device | Scope | Status | Depends On | Design Contract | Asset Spec | Open Questions | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Home | `index.html#home` | iPad | skeleton + assets | scanned | PRD, Interaction, home modules | partial | pending | hero icon style not final | build skeleton first |
```

Use these status values only:

- `pending`: in scope but not scanned yet
- `scanned`: globally identified, waiting for deep work
- `in_progress`: current active page
- `blocked`: cannot continue until a dependency or decision is resolved
- `skeleton_done`: HTML skeleton and placeholder layout are stable
- `asset_ready`: page layout is stable and asset contracts are ready
- `asset_filled`: assets were replaced for the current scope
- `verified`: page passed the current audit and can move forward
- `out_of_scope`: intentionally excluded from the current request

Field meaning:

- `Screen`: stable page or module name
- `Route / Anchor`: exact file path, route, or HTML anchor
- `Device`: phone, pad, TV, web, or mixed
- `Scope`: what this pass covers for the page, such as skeleton, repair, assets, or verification
- `Status`: use the fixed status set above
- `Depends On`: upstream docs, states, or sibling pages that affect this page
- `Design Contract`: `missing`, `partial`, `ready`, or `verified`
- `Asset Spec`: `missing`, `partial`, `ready`, or `verified`
- `Open Questions`: unresolved requirements, visual decisions, or state gaps
- `Next Action`: the next concrete move, not a generic note

Usage rules:

- Keep one row per screen or local route in the current task scope.
- During the first scan, fill only enough detail to preserve continuity; do not deep-analyze every page yet.
- Before each page pass, set the current row to `in_progress`.
- After each page pass, update `Status`, `Design Contract`, `Asset Spec`, `Open Questions`, and `Next Action`.
- Never rely on conversation memory alone for deciding the next page.


## Invocation Observability

Treat invocation telemetry as a host/runtime responsibility. Do not manually append invocation logs from the product workflow unless the user explicitly asks for project-specific telemetry. Monitoring failure must never block or alter product delivery.

## Output Package Structure

For a Full Package, create a folder named after the product or feature and include:

```text
product-name/
├── PRD.md
├── Interaction-Spec.md
├── UI-Concept-Prompts.md
├── Design.md
├── Asset-Spec.md
├── Docs-Handoff.md
└── prototype/
    ├── index.html
    ├── phone.html
    ├── pad.html
    ├── tv.html
    └── web.html
```

If the user wants a single file, create `index.html` with device tabs or viewport frames instead of separate HTML files.

Use one canonical handoff entry file. Prefer `Docs-Handoff.md`; link any Vibo-specific implementation prompt from it instead of creating competing handoff entry points.

## Device Prototype Guidance

- **Phone**: prioritize one-handed flow, bottom navigation or primary CTA placement, concise content, and clear touch targets.
- **Pad**: use split views, side panels, comparison, editing surfaces, or master-detail layouts.
- **TV**: use focus states, remote-control navigation, large type, sparse choices, and 10-foot viewing distance.
- **Web**: use dense but organized information, tables where useful, side navigation, filters, and persistent actions.

## References

- Read `references/full-product-delivery-workflow.md` when executing a full product-manager workflow from idea to docs, UI effects, high-fidelity HTML, asset planning, and developer handoff.
- Read `references/prd-outline.md` when writing product requirement documents.
- Read `references/interaction-spec.md` when defining flows, states, and screen behavior.
- Read `references/ui-concept-guide.md` when generating UI effect directions or image prompts.
- Read `references/design-system-guide.md` when converting approved UI effects into project-level visual rules before HTML implementation.
- Read `references/html-prototype-guide.md` before coding multi-device HTML prototypes.
- Read `references/asset-spec-guide.md` when creating asset placeholder inventories, image-generation prompts, or fill-image production plans.
- Read `references/vibo-coding-handoff.md` before preparing implementation handoff notes.
- Read `references/change-impact-guide.md` when an HTML or product change may require synchronized updates across requirements, interaction, design, assets, contracts, or handoff files.
