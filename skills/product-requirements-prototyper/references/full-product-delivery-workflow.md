# Full Product Delivery Workflow

Use this guide for product-manager workflows that need to move from a rough product idea to documents, UI effects, high-fidelity HTML, asset planning, and developer handoff.

This guide is only for product-delivery work. Do not apply its Stage Gate pauses to maintenance of the skill itself, including edits to `SKILL.md`, references, routing rules, Stage Gate rules, or skill guidance.

## Core Principle

Keep reusable method inside the skill. Keep project-specific content inside the project folder.

- Skill-level content: workflow, standards, checkpoints, naming rules, validation rules, prompt strategy, and handoff structure.
- Project-level content: PRD, interaction spec, UI concepts, HTML files, asset inventory, generated images, final prompts, and implementation notes.

## Mode Boundary

This file is for full product-delivery work. Do not use it as the default reading path for one-screen repairs.

If the user asks to fix one concrete page, route, anchor, device view, component family, icon group, or asset group, switch to screen-local refinement:

- read the exact HTML file and local anchor/module first
- read only the relevant project contract files
- read only the relevant `Design.md` / `Asset-Spec.md` sections
- do not re-run the whole Stage 1-7 chain unless the user asks or the repair is blocked without upstream clarification

## Standard Delivery Chain

```text
Stage 0: Workflow Routing / 阶段判断
Stage 1: PRD / 产品需求文档
Stage 2: Interaction Spec / 交互说明
Stage 3: UI Concept / UI 风格方向
Stage 4: HTML Prototype / HTML 原型
Stage 5: Design System / 高保真设计规范
Stage 6: Asset Spec / 资产规格
Stage 7: Developer Handoff / 开发交付
```

## Stage Gate Rules

Each product-delivery stage has a mandatory review gate:

1. **Scope check**: What feature, flow, screen, device, module, or asset group is in scope?
2. **Coverage checklist**: Which sections, states, pages, regions, assets, or handoff items must be handled?
3. **Completion audit**: Did the produced files cover every checklist item, and did related files need updates?
4. **Stage Gate summary**: State the completed stage, files changed, key conclusions, gaps, recommended next stage, and ask whether to continue.

Do not move to the next stage only because the current output "looks done." Move only after the stage's coverage checklist has been reviewed and the user confirms, unless the user explicitly authorized automatic progression.

For skill-maintenance tasks, do not use this gate. Complete all necessary skill file edits and report once at the end unless the user explicitly asks for staged confirmation.

Use this Stage Gate template:

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

### Stage 0. Workflow Routing / 阶段判断

- Determine the user's intended entry stage from the request.
- Start from the requested stage rather than forcing the full workflow from Stage 1.
- If upstream documents are missing, proceed with explicit assumptions and list the gap at the Stage Gate.
- If the user asks to backtrack, pause the current stage and return to the requested earlier stage.

### Stage 1. PRD / 产品需求文档

- Convert the user's rough idea into scenario, target users, value proposition, core goals, scope, non-goals, assumptions, and success metrics.
- Review that target users, scenarios, goals, scope, non-goals, assumptions, risks, and success metrics are all covered before confirmation.
- End with a Stage Gate before moving to interaction work.

### Stage 2. Interaction Spec / 交互说明

- Keep interaction details concrete: entry points, user flows, screen states, error states, empty states, loading states, and recovery behavior.
- Before finishing, audit PRD requirements against interaction flows and states so no requirement lacks behavior and no state lacks product rationale.
- End with a Stage Gate before moving to UI concept work.

### Stage 3. UI Concept / UI 风格方向

- Derive style from product scenario, target user, device, content density, and comparable products.
- Provide multiple directions before committing.
- Accept user reference images and analyze visual language: palette, layout density, typography, component shape, icon style, imagery style, and interaction tone.
- Review that each proposed direction covers layout, typography, color, components, imagery/icon style, density, motion/state feel, risks, and fit/mismatch.
- End with a Stage Gate before moving to HTML prototype work.

### Stage 4. HTML Prototype / HTML 原型

- Before coding high-fidelity HTML, verify that `Design.md` and `Asset-Spec.md` are ready to act as control files for the in-scope screens, or update them in the same pass.
- Lock the target canvas first, such as a fixed tablet landscape, phone portrait, TV, or web dashboard viewport.
- Translate UI effects into layout tokens: page padding, column widths, card heights, row gaps, typography scale, border radius, shadow, component dimensions, button equations, and repeated grid rules.
- Build the HTML skeleton before filling assets.
- Use green dashed placeholders for every future image, cover, avatar, icon, illustration, and play button.
- Show asset ID, purpose, and dimensions inside every placeholder.
- Do not use emoji, temporary icon fonts, or decorative mock art during skeleton validation.
- Validate one region at a time: top bar, hero/banner, side panel, repeated cards, bottom lists.
- Check top edge, vertical centerline, bottom edge, text baseline, font size, line-height, overflow, and button/control consistency.
- Fix layout and alignment before asset generation.
- Before asset work begins, audit the skeleton against all screens/regions/states in scope and confirm every future visual asset has a visible placeholder.
- End with a Stage Gate. Recommended next stage may be Stage 5 for design-system documentation or Stage 6 for asset inventory, depending on the user's scope.

For one-screen HTML repair, scope the audit to that screen only. Do not automatically re-open every page in the prototype.

### Stage 5. Design System / 高保真设计规范

- Create or update `Design.md` when the project needs a reusable visual contract.
- Translate the visual effect set or accepted HTML into project-level rules: device canvas, color palette, typography scale, card style, spacing, grid, component sizing, button family contracts, shadow, border radius, and alignment checks.
- Include screen-specific layout rules for each confirmed page.
- Keep `Design.md` separate from `Asset-Spec.md`: `Design.md` defines layout and visual language; `Asset-Spec.md` defines the image/icon/cover assets that fill specific slots.
- Update `Design.md` when HTML implementation reveals a better accepted rule, and update HTML when `Design.md` changes.
- Before finishing, audit that every approved effect screen has canvas, grid, typography, component, button-system, surface/shadow, asset-slot, and acceptance rules.
- End with a Stage Gate before moving to asset specification.

### Stage 6. Asset Spec / 资产规格

- Create `Asset-Spec.md` after the high-fidelity skeleton exists.
- Every placeholder in HTML must have a matching row.
- Every row should include ID, screen, location, purpose, size/ratio, visual direction, prompt notes, source/file, and status.
- Every row should also include target format, such as PNG, transparent PNG, SVG, CSS only, video, or other agreed format.
- For layout-sensitive slots, rows should also record the owning component/region, crop or anchor rule, overflow policy, state usage, and replacement constraint so later asset replacement does not break buttons, rows, cards, or navigation items.
- Use stable prefixes:
  - `A`: avatar/header artwork
  - `I`: navigation or utility icons
  - `H`: hero/banner artwork
  - `T`: section-title icons
  - `C`: content or feature icons
  - `M`: media or cover artwork
  - `P`: play/action buttons
  - `N`: thumbnails or supporting imagery
  - `D`: detail-page or modal artwork
  - `V`: visual character or persona artwork when the product needs it
- End with a Stage Gate before moving to developer handoff or asset generation/replacement work.

### Asset Generation and Replacement

- Generate assets one group at a time, not all at once.
- Before generating, inventory all slots in the requested group or screen. After replacing, audit that every slot in that inventory has the correct file, target format, container fit, and status.
- Replace assets without changing HTML container dimensions.
- If an asset crops poorly, revise the asset composition, not the layout slot.
- After replacement, verify that typography, spacing, baseline alignment, and card dimensions did not shift.
- Update `Asset-Spec.md` status and source file path.

Asset generation/replacement is usually part of Stage 6 unless the user treats it as a separate implementation task. It still requires a Stage Gate summary when complete.

For multi-screen prototypes, Stage 4 HTML work and Stage 6 asset work should normally advance page by page. Use one completed screen as the working unit unless the user explicitly approves multi-screen batching or full auto progression with a resumable checklist.

Before the first page pass, create a lightweight screen ledger for the in-scope prototype so later pages do not disappear from working memory after one page triggers new requirements or issues.

Recommended fixed screen-ledger template:

```md
| Screen | Route / Anchor | Device | Scope | Status | Depends On | Design Contract | Asset Spec | Open Questions | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
```

Recommended status set:

- `pending`
- `scanned`
- `in_progress`
- `blocked`
- `skeleton_done`
- `asset_ready`
- `asset_filled`
- `verified`
- `out_of_scope`

### Stage 7. Developer Handoff / 开发交付

- Include PRD, interaction spec, HTML prototype, asset spec, known assumptions, and implementation notes.
- Call out which parts are layout-locked, which assets are placeholders, and which details still need production replacement.
- Audit handoff coverage against all project deliverables so engineering receives every file, known limitation, unresolved decision, and implementation priority.
- End with a Stage Gate that recommends stopping, reviewing, or returning to an earlier stage for fixes.

## Stage Transitions

Default allowed forward transitions:

- Stage 1 -> Stage 2
- Stage 2 -> Stage 3
- Stage 3 -> Stage 4
- Stage 4 -> Stage 5
- Stage 4 -> Stage 6
- Stage 5 -> Stage 6
- Stage 6 -> Stage 7

The user may skip stages. If they do, state the risk and proceed with assumptions instead of forcing a restart.

## Quality Checklist

Before delivery, verify:

- The first screen is the product experience, not a landing page.
- The requested scope has a matching coverage checklist, and the final files cover every checklist item or explicitly mark exclusions.
- High-fidelity HTML and asset-fill work did not skip past the page boundary silently; if multiple screens were involved, each page has its own completion state or summary.
- A screen ledger or equivalent page queue exists when multi-screen work spans multiple turns.
- Layout matches the approved effect image by measured grid, not by vague similarity.
- No placeholder spills outside its parent.
- All text fits and aligns with neighboring elements.
- Repeated components share consistent dimensions.
- Repeated buttons and controls share documented variant rules instead of ad hoc CSS differences.
- Green dashed placeholders are labeled.
- `Asset-Spec.md` covers every visible placeholder.
- `Design.md` contains button standards and the HTML actually follows them.
- Browser preview URL is provided.
- Skill invocation logs are written with `running` and `success` or an explicit terminal state.

## Logging

Write logs for meaningful stages:

- `product_framing_checkpoint`
- `generate_prd_interaction_spec`
- `ui_style_checkpoint`
- `page_ui_effect_checkpoint`
- `design_system_create`
- `html_prototype_build`
- `html_skeleton_placeholder`
- `html_asset_slot_annotation`
- `asset_spec_create`
- `asset_generation`
- `developer_handoff`

Use `running` when the stage starts and a terminal state when it ends. Do not leave stale running records without a later completion or failure entry.
