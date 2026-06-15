# HTML Prototype Guide

Use HTML prototypes to make requirements concrete for engineering and AI coding workflows.

Stage mapping: use this reference only for **Stage 4 - HTML Prototype / HTML 原型** in product-delivery tasks. After finishing Stage 4, return to the Stage Gate template in `SKILL.md` and pause unless the user explicitly authorized automatic progression. Do not apply this pause rule to skill-maintenance tasks.

## HTML Coverage Review

Before coding, restate the prototype scope: device(s), screen(s), flows, states, and whether the task is skeleton-only, asset-fill, repair, or full prototype.

If the task is a one-screen repair, name the exact scope up front, for example:

- `index.html#home`
- `index.html#detail`
- `index.html#player`
- one device page such as `phone.html`
- one repeated module such as story cards, chapter rows, or player controls

In one-screen repair mode, do not treat the whole prototype as in scope unless the user explicitly broadens it.

Before finishing, audit that the prototype covers:

- all in-scope screens and navigation paths
- required states: normal, empty, loading, error, permission, disabled, success, and current/selected when relevant
- all major regions on each screen: top bar, navigation, main content, panels, repeated lists/cards, bottom controls, overlays
- text fit, wrapping, and overflow on the target viewport
- asset placeholders or final assets for every visible image/icon/avatar/cover/illustration slot
- back/return logic and cross-page navigation behavior
- no stale temporary references, unused duplicated UI, or misleading placeholder labels in completed regions

If verification cannot use a browser screenshot, state the verification limit and perform file-level checks for references, dimensions, and state coverage.

## Prototype Standards

- Create usable screens, not static posters.
- Include realistic sample data.
- Include key states: normal, empty, loading, error, permission denied, and success where relevant.
- Keep navigation clickable enough to demonstrate the core flow.
- Use responsive constraints and stable layout dimensions.
- Avoid decorative-only sections unless they are part of the product experience.
- Verify the prototype in a browser before delivery.
- Do not structure product prototypes as slide decks. Avoid `.slide`-based navigation, page counters, and keyboard-only presentation patterns unless the product itself is a presentation tool.

## Product HTML Coding Ownership

Use this reference for product HTML skeletons, high-fidelity product screens, app/web/pad/TV UI repairs, Design.md-driven layout fixes, and asset-placeholder coding.

Do not hand product prototype coding to `html-presentation-designer`. That skill is for 16:9 presentation decks and report-style HTML. Product HTML coding must keep product flows, screen states, asset slots, navigation, back behavior, and handoff documents aligned.

Useful visual QA habits that were previously practiced in presentation-style work may be reused here only as product-screen checks:

- establish explicit typography roles instead of letting all text share the same weight
- compare blocks by top edge, centerline, baseline, and bottom edge
- keep repeated cards, controls, and slots at stable dimensions
- verify text fit, line height, and visual hierarchy in the real target viewport
- update `Design.md` when a repeated layout rule becomes accepted product truth

## High-Fidelity HTML Skeleton Workflow

Use this workflow when the user expects the HTML prototype to closely match approved UI effect images.

Default delivery unit: one screen/page per pass. Unless the user explicitly requests multi-screen batching or full auto mode, do not build every page in a prototype at once. Finish one screen, verify one screen, and summarize one screen before advancing.

This does not mean "ignore the remaining pages." Before the first deep implementation pass, do a lightweight global scan and create a screen ledger or page queue so the remaining pages stay visible throughout the task.

1. **Run a preflight check before coding.** Confirm the scope, target viewport, approved reference images, and whether the task is skeleton build, high-fidelity repair, or asset-fill. For high-fidelity work, verify that `Design.md` already contains or will immediately contain layout rules, component rules, and button standards, and that `Asset-Spec.md` can cover every visible slot. If those contracts are missing, create or strengthen them before calling the HTML "done."
2. **Lock the canvas first.** Set the target device viewport explicitly, such as a fixed phone portrait, tablet landscape, TV, or web dashboard mock. Do not let ordinary responsive web behavior change the design during the first fidelity pass.
3. **Measure the approved effect image into layout tokens.** Record page padding, top status height, section widths, grid columns, card heights, row gaps, border radius, major font sizes, repeated component sizes, and button equations before coding.
4. **Build an asset-free skeleton.** Replace all future images, covers, avatars, icons, illustrations, and play icons with green dashed placeholders. Use the same placeholder dimensions as the final asset slots, and show each placeholder's asset ID, purpose, and intended size directly in the page. When removing temporary emoji, icon-font glyphs, SVG symbols, or text-only stand-ins, preserve the original functional position as a placeholder slot instead of deleting the slot.
5. **Validate regions one at a time.** For each screen, check top navigation/header, hero/banner, side panels, repeated cards, bottom rows, and interactive controls separately. Do not fix every region in one pass.
6. **Check alignment explicitly.** For every horizontal band, inspect top edge, visual centerline, text baseline, and bottom edge. Fix title/subtitle groups that float too high or low relative to neighboring controls.
7. **Check typography and button rules as measurements.** Compare title, subtitle, label, card title, body copy, metadata, and button labels against the reference and `Design.md`. Adjust line-height, font-weight, padding, no-wrap, and icon/text spacing with the same care as font-size.
8. **Check overflow and containment.** Repeated items must fit inside their parent card without clipping, spilling, or changing the container height. Use fixed row heights for icon grids and stable card dimensions.
9. **Only add real assets after the skeleton is approved.** Replacing placeholders with icons or images must not change layout dimensions. If an asset needs a different crop, change the asset, not the container.
10. **Run a browser verification pass.** Open the exact local URL, compare against the approved effect image, and iterate. If screenshot automation is unavailable, use the browser view and local structure checks, and state the verification limits.

## HTML Preflight Gate

Before starting or declaring completion for a high-fidelity screen, check these items:

- `Design.md` contains the in-scope canvas, grid, typography, component rules, and button system, or is updated in the same pass.
- `Asset-Spec.md` exists or is prepared for every visible image/icon/avatar/cover/illustration slot.
- Repeated controls do not rely on unstated assumptions such as "use a similar button."
- The current task scope is explicit: which screens, states, devices, and modules are in scope.

If any item is missing, fix the contract files first or in parallel. Do not leave HTML as the only place where the visual rules exist.

## Screen-Local Refinement Mode

Use this mode when the user is repairing one exact screen or module instead of building the whole prototype.

Read in this order:

1. the exact HTML file and local anchor/module
2. page-level contract files, if the project has them
3. the relevant `Design.md` section
4. the relevant `Asset-Spec.md` rows

Do not read unrelated screens, unrelated contract files, or the full project PRD/interaction docs unless the current repair cannot be completed safely without them.

Keep the local repair checklist narrow:

- target screen/module geometry
- target controls and text fit
- target asset slots
- target navigation or return behavior
- directly adjacent dependent rules only

For new high-fidelity skeleton builds where the user did not name one page but the product contains multiple screens, create a page queue first and still execute page by page:

- identify the in-scope pages
- record them in a screen ledger with status and dependencies
- choose the first page explicitly
- complete skeleton, placeholder, and local contract sync for that page
- update the ledger after the page pass
- summarize what is now stable before opening the next page

Do not keep two or three partially stabilized pages open in one pass unless the user explicitly accepts that risk.

Keep the first scan lightweight for token efficiency:

- read routing structure, page names, anchors, and obvious module boundaries first
- avoid deep visual comparison for every page during the scan
- deep-read only the current page being implemented plus directly adjacent dependencies

The scan creates continuity; the page pass creates fidelity.

Use this fixed ledger template for multi-screen work:

```md
| Screen | Route / Anchor | Device | Scope | Status | Depends On | Design Contract | Asset Spec | Open Questions | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Home | `index.html#home` | iPad | skeleton + assets | scanned | PRD, Interaction, home modules | partial | pending | hero icon style not final | build skeleton first |
```

Use these status values only:

- `pending`
- `scanned`
- `in_progress`
- `blocked`
- `skeleton_done`
- `asset_ready`
- `asset_filled`
- `verified`
- `out_of_scope`

Keep the ledger lightweight during the first scan. Deep details belong to the current page pass, not to every row up front.

## Button And Control Discipline

Buttons are not "small details." They are one of the fastest ways for a prototype to drift.

When coding or repairing HTML:

- Map every visible button and interactive control to a documented button or control family in `Design.md`.
- Do not invent a new button style in CSS unless `Design.md` is updated with a reason and a contract.
- Check height, min-width, horizontal padding, icon slot size, icon/text gap, radius, surface, border, shadow, and no-wrap behavior.
- For icon-only buttons, verify the hit area and the visual icon box separately.
- For mixed button groups, verify that visual priority comes from the documented variant system rather than accidental size or shadow differences.
- If a button label wraps, overflows, or collapses icon spacing, treat it as a design-contract failure and fix the rule rather than hiding the symptom.

## Placeholder Convention

- Use a green dashed border for all unfilled asset slots.
- Keep placeholder interiors neutral and low opacity so layout can be judged without visual noise.
- Apply placeholders to avatar slots, header icons, navigation icons, cover images, hero/background images, action buttons, section-title icons, and content thumbnails.
- Do not use emoji or temporary icon fonts in high-fidelity skeleton mode; they distort perceived size, weight, and spacing.
- Removing a temporary icon is not the same as removing the asset slot. If a control will later receive a rendered icon, keep a same-size green dashed placeholder in the button, row, tab, toolbar, or navigation area so the next asset-generation pass knows exactly where to fill it.
- Give every placeholder a visible asset label, for example `A01 avatar 68x68`, `H01 hero bg 626x286`, or `I03 nav icon 38x38`. Use dimensions from the active project's approved design, not from a hardcoded example.
- Use stable asset ID prefixes: `A` for avatar/header artwork, `I` for navigation or utility icons, `H` for hero/banner artwork, `T` for section-title icons, `C` for content or feature icons, `M` for media/cover artwork, `P` for play/action buttons, and `N` for thumbnails or supporting imagery.
- Keep the asset label in the HTML until final asset replacement. The label is the handoff key for generating or swapping each image one by one.
- Create an `Asset-Spec.md` file for high-fidelity projects. It should list every asset ID, screen location, purpose, required size or ratio, visual direction, prompt notes, and production status. Keep image-generation prompts and replacement status in this document rather than burying them in the HTML.

Placeholder IDs in HTML must match `Asset-Spec.md` exactly. If the asset slot belongs to a button, tab, row action, toolbar, or navigation control, keep the slot aligned with the owning component contract in `Design.md`.

## Multi-Device Adaptation

Phone, pad, TV, and web should have distinct layouts when the use case demands it.

- Phone: compact flows, thumb-friendly controls, progressive disclosure.
- Pad: side-by-side panels, canvas space, mixed touch and keyboard assumptions.
- TV: focus ring, directional navigation, large type, reduced density.
- Web: efficient scanning, filters, tables, persistent navigation, keyboard/mouse assumptions.

## Handoff Comments

In the HTML, use short comments for important product decisions only. Do not over-comment obvious markup.

## Completion Audit

Before closing a high-fidelity HTML task, explicitly verify:

- every repeated button/control matches a documented variant
- no unexplained button size, radius, padding, or shadow variants remain
- every visible asset slot is represented in `Asset-Spec.md`
- asset placeholders or final assets preserve the surrounding layout
- the final HTML can be explained by `Design.md` and `Asset-Spec.md`, not by one-off CSS accidents
