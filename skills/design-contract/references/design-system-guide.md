# Design.md Guide

Create `Design.md` for every product project that has confirmed UI effect images or a high-fidelity HTML prototype target.

Stage mapping: use this reference only for **Stage 5 - Design System / 高保真设计规范** in product-delivery tasks. After finishing Stage 5, return to the Stage Gate template in `SKILL.md` and pause unless the user explicitly authorized automatic progression. Do not apply this pause rule to skill-maintenance tasks.

## Purpose

`Design.md` is the bridge between visual effects and implementation. It captures the reusable visual rules for one project so the HTML prototype can be checked against explicit design standards instead of vague similarity.

Use it together with:

- `PRD.md` for product truth.
- `Interaction-Spec.md` for behavior and states.
- `Asset-Spec.md` for image, icon, avatar, cover, illustration, and media placeholders.
- `prototype/index.html` or device-specific HTML files for implementation.

`Design.md` should be specific enough to implement from, but not so overloaded that every pixel observation becomes permanent law. Use it as the project-level visual contract, and keep raw observations, rejected options, and temporary comparisons in project notes when needed.

Important: a valid `Design.md` is not just a descriptive summary. It is the rulebook that later HTML and asset replacement work must obey. If a future implementer cannot tell whether a button, card, toolbar, tab, or list row is correct, then `Design.md` is still incomplete.

## Skill Boundary

Use this guide for product UI design systems and high-fidelity prototype rules. Do not use `html-presentation-designer` as the owner for product `Design.md` work, even if the immediate task looks like visual polish. Presentation-deck typography and layout instincts may inform the craft, but product `Design.md` must describe reusable product screens, states, regions, asset slots, and acceptance checks.

## Core Principle

Reference images must be treated as design evidence, not inspiration.

Design review is also a coverage discipline. Before creating or revising `Design.md`, restate which screens, devices, modules, states, and reference images are in scope. Before finishing, audit that every in-scope item has corresponding rules or is explicitly marked out of scope.

Do not jump directly from "the reference looks soft" to CSS guesses. Convert the image into measured and named design facts:

1. Canvas and coordinate system.
2. Major regions and module boxes.
3. Alignment and baseline relationships.
4. Typography hierarchy.
5. Component sizing.
6. Spacing rhythm.
7. Surface, shadow, radius, and opacity rules.
8. Asset slots and real-image visual overflow.
9. Interaction states.
10. Acceptance checks.

The goal is not to record every visible pixel. The goal is to capture the few stable rules that explain the page and prevent future drift.

## Multi-Pass Reference Analysis

Use multiple passes for high-fidelity screens. A single visual pass almost always loses important details.

### Pass 0: Source Control

Before analyzing, define the source of truth:

- Which image is the target effect.
- Which HTML screen is the current implementation.
- Which device, viewport, orientation, and scale are assumed.
- Whether the image is a full screen, cropped screen, browser screenshot, or generated effect.
- Whether real assets are final or still placeholders.

Record this at the top of `Design.md` so future comparisons do not mix different references.

### Pass 1: Canvas and Grid

Measure the large geometry first:

- Canvas width and height.
- Page padding.
- Column widths.
- Row heights.
- Major gaps.
- Shared top edges.
- Shared bottom edges.
- Cross-module alignments.

Write equations when possible. Example shape:

```text
left padding + col A + gap + col B + gap + col C + right padding = canvas width
```

If this equation cannot be written, the layout is probably not ready for high-fidelity HTML.

### Pass 2: Module Boxes

Draw or infer a bounding box for each major region:

- Top/status/navigation area.
- Primary content block.
- Side panel.
- Repeated list/card region.
- Bottom control or summary region.
- Modal or overlay if present.

For each module, record:

- `x / y`
- `width / height`
- top-edge relationship
- bottom-edge relationship
- internal padding
- outer gap to neighbors

Do not skip bottom edges. Many high-fidelity layout problems happen because top alignment is correct but bottom anchoring is missing.

### Pass 3: Internal Rhythm

Analyze each module from top to bottom:

- Title to metadata.
- Metadata to body.
- Body to controls.
- Controls to module bottom.
- List title to first row.
- Row to row.

Classify each vertical gap as one of:

- fixed gap
- content-driven gap
- elastic gap
- bottom-anchored gap

This prevents natural-flow HTML from drifting away from the reference. If a control should align to a module bottom, state that explicitly.

### Pass 4: Typography

Record text roles, not just font sizes:

- system/status text
- page title
- section title
- card title
- body
- label/pill
- metadata
- button text
- state text
- annotation/helper text

For each role, record:

- font size
- line height
- weight
- color
- max line count where relevant
- wrapping rule

Text wrapping is a first-class design constraint. Buttons, compact labels, tab labels, and right-side row values usually need explicit no-wrap rules.

### Pass 5: Component System

Record reusable component rules:

- cards
- buttons
- tags/pills
- rows
- toggles
- progress bars
- icon slots
- avatars
- image covers
- tabs
- modals
- navigation controls

For each component, capture:

- width / height or sizing mode
- padding
- gap
- border
- radius
- surface color
- shadow token
- icon size
- internal grid, including icon column width, text column minimum width, gap, and left/right safe padding
- text role
- state variants

For high-fidelity product work, buttons are mandatory component-contract items. Do not leave button rules implied by screenshots or scattered CSS.

Every `Design.md` that includes interactive controls must define a button system with at least:

- variant name, such as `primary`, `secondary`, `ghost`, `destructive`, `icon-only`, `chip/tab`, or project-specific equivalents
- intended usage and priority rule
- height and minimum width
- horizontal padding
- icon slot size
- icon-text gap
- border radius
- background, border, and shadow token
- text role, font size, weight, and no-wrap rule
- state variants: default, hover/focus if relevant, pressed, disabled, selected/current if relevant
- whether the button is width-fixed, content-fit, full-width, or grid-aligned

If a project contains multiple button families, explain why. Do not let every module invent a different CTA shape without a documented role difference.

Use a button contract table when possible:

```text
Variant | Usage | Height | Min Width | Padding | Icon | Gap | Radius | Text Role | Surface | Border | Shadow | No-wrap | States
```

For buttons with icons, also record the internal equation:

```text
left padding + icon slot + icon/text gap + label width + right padding = button content width
```

Treat wrapped button labels as a design-system failure unless the project explicitly uses multi-line buttons.

Do not let each screen invent a new component version unless the difference has a purpose.

For compact navigation rows, sidebars, menus, and list items, do not record only the outer size and icon size. Also record the internal horizontal equation:

```text
left padding + icon slot + icon/text gap + text minimum width + right safe padding = row content width
```

Active or selected backgrounds make spacing errors more visible. Text must not touch the selected background edge, and icons must not appear stranded far from the left edge unless the reference intentionally uses a centered icon column.

### Pass 6: Surface and Shadow

Analyze shadows separately from layout.

Shadow is not a default decoration. Add a shadow only when the reference or accepted design direction shows a reason for elevation, separation, action emphasis, or material depth.

For each surface type, decide whether it is:

- attached/near-background
- light floating
- elevated
- modal-level
- glow/action emphasis

Then define separate tokens. Do not reuse one generic shadow for every surface.

Capture:

- x offset
- y offset
- blur radius
- spread if used
- color and opacity
- whether it is functional elevation or visual glow
- whether the element should have no shadow because it must visually merge with its parent surface

Important rule: if the reference surface appears close to the background, keep blur radius and y offset small. Large blur values can make cards look high and detached even when the coordinates are right.

If a real image already has a white or flat background and sits on a matching card surface, do not add image-level `drop-shadow` unless the reference clearly shows that image floating. Extra image shadows can create an unintended pasted-on layer.

### Pass 7: Asset Slots

Separate asset layout from asset appearance.

For each image/icon/avatar/cover/illustration slot, record:

- asset ID
- layout box size
- target asset format, for example `transparent PNG`, `raster PNG`, `SVG`, `video`, or `CSS only`
- intended real asset type
- whether the real asset may visually overflow the box
- anchor point
- crop behavior
- shadow behavior
- production status

The target format is part of the slot contract, not a later implementation detail. Use it to decide how to move from placeholder stage to real asset stage:

- Use `transparent PNG` or `raster PNG` when the reference shows rendered, skeuomorphic, photographic, clay, 3D, or soft bitmap texture.
- Use `SVG` only when the reference is vector-flat, line-icon based, or must remain deterministic and style-system-native.
- Use `CSS only` only for simple geometric UI primitives such as plain progress bars, pill backgrounds, and untextured surfaces.
- Do not replace a rendered bitmap-style reference icon with SVG merely to avoid cropping problems; fix the asset workflow by generating or cropping the bitmap per slot.
- Do not crop all icons from one full-screen reference unless the slot contract allows it. Small icon slots usually need per-slot generation or source assets to avoid visual drift and offset errors.

Recommended slot table columns:

```text
ID | Name | Layout Box | Target Format | Visual Style | Anchor/Crop | Overflow | Shadow | Source/Status
```

Placeholder validation and real-asset validation are separate:

- Placeholder validation: layout, alignment, dimensions, no text overlap.
- Real-asset validation: visual weight, crop, shadow, color harmony, occlusion.

Asset-slot rules must point back to the component system. If an icon belongs inside a button, tab, list row, or navigation rail item, record enough information that later asset replacement cannot change the button padding, row height, or text alignment.

### Pass 7B: Asset Fill Scope Audit

Every asset-fill or asset-replacement request needs an explicit scope audit. Do not rely on memory of earlier requirements or on the most recent cropped screenshot alone.

Before editing:

1. **Restate the requested scope**
   Identify whether the user asked for one slot, one module, one screen, one asset type, or the full visible page.

2. **Inventory all slots in scope**
   Read the current HTML and `Asset-Spec.md`, then list every slot covered by the scope. Include slots that are easy to miss: navigation buttons, inline button icons, state icons, empty/locked/current-state icons, decorative illustrations, and repeated list row icons.

3. **Check slot contracts**
   For each slot, confirm name, layout box, target format, visual style, source/status, and whether the current file matches the intended format.

4. **Process by checklist, not by attention**
   Update assets one by one against the slot inventory. Do not stop after the visually largest or most recently discussed items unless the user explicitly narrowed the request.

After editing:

1. **Reference audit**
   Search the HTML for old file extensions, old placeholder classes, temporary crop names, green dashed slots, or stale source paths inside the affected screen.

2. **Inventory audit**
   Update `Asset-Spec.md` so every slot in the requested scope has a current file, target format, container size, and status.

3. **Design contract audit**
   Update `Design.md` only with reusable rules: scope coverage, target format policy, container dimensions, crop/anchor rules, and validation criteria. Do not replace slot data with a vague "filled" status.

4. **Completeness statement**
   Before finishing, state which slots were covered and which slots are intentionally out of scope or still pending. If any slot remains temporary, mark it explicitly.

This pass exists because asset work often happens across multiple turns. The assistant must re-read the scope and current files each time instead of assuming earlier context is still complete.

### Pass 8: States

Record UI states as visual rules:

- active
- selected
- current/playing
- disabled
- locked
- loading
- empty
- error
- success
- expanded/collapsed

For each state, define which visual properties change:

- icon
- text
- background
- border
- shadow
- opacity
- position
- state label

Do not represent state only as text if the reference uses iconography, color, or shape.

### Pass 9: Difference Log

When comparing HTML to a reference, maintain a difference log before editing:

| Module | Reference | Current HTML | Difference | Fix rule | Status |
| --- | --- | --- | --- | --- | --- |

Use this log to decide which differences become `Design.md` rules and which are one-off implementation fixes.

Only promote a difference into `Design.md` when it is:

- repeated across the screen,
- structurally important,
- likely to regress,
- or needed to explain future implementation choices.

### Pass 9B: Change Request Compensation

Treat every user-requested design change as a small system migration, not an isolated edit.

When a change removes, moves, resizes, or restates a UI element, do a compensation pass before closing the task:

1. **Identify the changed module**  
   Name the exact module, component, state, or asset slot affected by the request.

2. **Trace layout dependencies**  
   Check nearby baselines, grid offsets, fixed heights, elastic gaps, bottom anchors, and sibling alignment rules. If an element is removed, remove the spacing that only existed to make room for it.

3. **Trace component dependencies**  
   Check whether CSS classes, DOM nodes, state variants, asset records, or design tokens are now unused, duplicated, or misleading.

4. **Update the project contract**  
   Update `Design.md` with the new accepted rule and remove or revise old rules that would cause future regressions. When assets are affected, update `Asset-Spec.md` as well.

5. **Run a regression checklist**  
   Recheck counts, overflow, no-wrap rules, alignment, visual hierarchy, hidden/empty states, and any content variants that were intentionally introduced.

6. **Record the delta**  
   Add a short Difference Log or change-log row explaining the old behavior, the new rule, and the compensation performed.

Do not leave old design assumptions in `Design.md` after HTML changes. A stale rule is more dangerous than a missing rule because future implementation will faithfully recreate the wrong state.

### Pass 10: Acceptance Checklist

Every high-fidelity `Design.md` needs a checklist. It should include both hard geometry checks and visual checks.

Hard checks:

- canvas size
- grid math
- module dimensions
- shared top/bottom baselines
- button no-wrap
- text overflow
- asset slot dimensions

Visual checks:

- shadow radius and elevation
- component state clarity
- typography hierarchy
- surface contrast
- repeated-row consistency
- real asset visual weight

## One Screen or Many Screens?

Analyze one screen at a time for high-fidelity detail. Do not try to extract a complete design system from many screens in a single pass.

Recommended order:

1. Pick the most representative screen.
2. Build a precise `Design.md` section for that screen.
3. Extract reusable tokens from that screen.
4. Move to the next screen.
5. Reconcile tokens only after 2-3 screens reveal repeated patterns.

This avoids two common failures:

- Overfitting the whole design system to one image.
- Losing micro-details by scanning too many screens at once.

For a multi-screen product, structure `Design.md` like this:

```text
Design.md
├── Purpose and Contract Hierarchy
├── Global Visual Direction
├── Global Tokens
├── Component System
├── Page Exception Table
├── Screen Rules
│   ├── Screen A
│   ├── Screen B
│   └── Screen C
└── QA Checklist
```

## Contract Hierarchy and Page Exceptions

A high-fidelity `Design.md` must make rule priority explicit. Use this hierarchy:

1. **Global tokens**: canvas, safe margins, navigation geometry, spacing scale, typography scale, color, radius, shadows.
2. **Component standards**: button families, cards, rows, tabs, modals, navigation controls, icon slots, avatars, states.
3. **Screen rules**: one screen's information structure, grid, module sizes, and screen-specific constraints.
4. **Asset slot rules**: image/icon file, crop, format, visual weight, and replacement constraints.

New pages must inherit global tokens and component standards before adding screen rules. Do not start a new high-fidelity page from ad hoc CSS, a screenshot impression, or a local module preference.

If the user gives an explicit special requirement for a page, module, or state, treat it as a local exception by default:

- Apply it only to the named page/module/state.
- Record it in a Page Exception Table or the relevant Screen Rules section.
- Include scope, reason/source, affected components, and acceptance checks.
- Do not promote it into a global token or component standard unless the user explicitly asks for global promotion.

Page exceptions are allowed; silent global drift is not.

## Should Design.md Be Rewritten Multiple Times?

Yes, but not casually.

Use staged rewrites:

1. **Draft 1: observation capture**  
   Record canvas, modules, and obvious visual tokens.

2. **Draft 2: measured rules**  
   Convert observations into explicit dimensions, spacing, text roles, component standards, and state rules.

3. **Draft 3: implementation reconciliation**  
   After HTML is built or repaired, compare actual output to the reference and update only accepted rules.

4. **Draft 4: stabilization**  
   Remove temporary notes, mark open risks, and keep the durable design contract.

Avoid endless rewriting by separating:

- `Design.md`: stable rules.
- difference log: current mismatches.
- implementation notes: what changed in HTML.
- `Asset-Spec.md`: image and icon production.

## Parameter Ledger

For high-fidelity work, include a parameter ledger in `Design.md`.

Minimum ledger:

| Category | Parameter | Value | Applies To | Source | Status |
| --- | --- | --- | --- | --- | --- |
| Canvas | width | `...px` | all screens | reference | locked |
| Grid | primary columns | `...` | screen name | reference | locked |
| Typography | title | `...` | title role | reference/html | candidate |
| Shadow | panel | `...` | cards | reference/html | locked |
| Component | primary button | `...` | CTA | reference/html | locked |

At minimum, include rows for every major button family, repeated card family, navigation item family, and any control whose visual drift would be obvious to users.

Use `Status` values:

- `observed`: seen in reference but not yet implemented.
- `candidate`: plausible value awaiting visual check.
- `locked`: accepted rule.
- `rejected`: tried and rejected.
- `asset-dependent`: must be rechecked after real assets arrive.

This is the main trick for not losing parameters.

## Required Sections

Include these sections unless the project clearly does not need one:

1. **Purpose**: How `Design.md`, `Asset-Spec.md`, and HTML relate.
2. **Reference Sources**: target images, HTML pages, device assumptions, and comparison status.
3. **Device and Canvas**: viewport size, orientation, density assumptions, fixed-layout or responsive mode.
4. **Visual Keywords**: concise language for the product's emotional and visual direction.
5. **Parameter Ledger**: key values and lock status.
6. **Color System**: background, text, muted text, card, line, primary action, warning/success if relevant.
7. **Typography Scale**: status, page title, section title, card title, body, label, metadata.
8. **Layout Grid**: page padding, column widths, row heights, major gaps, repeated grid rules.
9. **Spacing and Baselines**: shared top/bottom edges, elastic gaps, bottom anchoring rules.
10. **Surface and Shadow System**: separate tokens for panel, list, button, progress, modal, glow.
11. **Component Standards**: cards, buttons, tags, lists, tabs, modals, navigation, controls.
12. **Button System**: button families, usage rules, dimensions, equations, text-wrap policy, icon rules, and state behavior.
13. **Asset Placeholder Rules**: green dashed placeholder usage, asset ID display, dimension stability.
14. **State Rules**: active, selected, locked, disabled, playing/current, success/error.
15. **Screen-Specific Rules**: important screen layouts and per-screen visual constraints.
16. **Page Exception Table**: local exceptions, scope, reason/source, affected components, acceptance checks, and whether the user explicitly promoted them to global.
17. **Difference Log**: reference vs current HTML mismatch table.
18. **Change Request Log**: accepted user changes, layout compensation, stale-rule cleanup, and verification.
19. **Alignment QA Checklist**: edge alignment, baseline alignment, overflow, repeated component consistency.
20. **Two-Way Update Rule**: update `Design.md` when HTML changes reveal a better rule, and update HTML when `Design.md` changes.

## Completion Threshold

Do not claim that `Design.md` is complete for a high-fidelity screen unless all of the following are true:

- core layout math is present
- typography roles are named
- repeated components are standardized
- button families are explicitly defined
- asset placeholders and slot rules are referenced
- relevant states are defined
- global tokens and screen-specific rules are separated
- local page exceptions are recorded and have not silently changed global rules
- the HTML can be checked against a concrete checklist instead of visual intuition alone

## High-Fidelity Rules

- Before coding HTML, translate approved effect images into measured tokens: canvas, page padding, section positions, card sizes, column widths, font sizes, line-heights, radii, shadows, and repeated item dimensions.
- Do not use temporary emoji, icon fonts, or random placeholder imagery during high-fidelity layout validation.
- Use green dashed placeholders for all future assets and label each placeholder with ID, purpose, and size.
- Use `Asset-Spec.md` for the detailed production plan of each asset. Do not put long image prompts inside HTML.
- Validate one region at a time: status/top bar, main content grid, side panel, repeated cards, bottom list, modal.
- For each region, compare top edge, visual centerline, text baseline, bottom edge, and overflow.
- Inspect micro-components, not only large layout blocks: button background layers, icon slots inside buttons, status toggles, pill tags, progress bars, row action columns, and small control states.
- For compact side navigation or menu rows, inspect left icon distance, icon/text gap, text column width, and right safe padding in both normal and selected states.
- When a reference screen has an icon inside a button or row, create a placeholder for that icon even if the final image is not ready. Do not replace it with plain text.
- For list rows with multiple right-side meanings, preserve separate columns for function icon, duration/value, and state/action instead of collapsing them into one text column.
- Capture vertical rhythm between blocks: if the reference has compact stacked cards, specify card heights and inter-block gaps so HTML does not create large dead bands.
- If a visual effect image and the HTML disagree, either fix the HTML or update `Design.md` with the new accepted rule. Do not leave the difference implicit.
- If a user-requested change removes or relocates a module, inspect and clean up the spacing, baselines, asset notes, state rules, and old `Design.md` entries that depended on that module.
- If button text wraps unexpectedly, treat it as a layout bug, not a content problem. Fix width, columns, font size, or no-wrap rules.
- If a card looks too detached from the background, inspect shadow blur/y-offset before changing coordinates.
- If an image looks pasted onto a card, inspect image-level shadows and background mismatch before changing the image crop.
- If a content module should align with neighboring module bottoms, use a fixed module height plus elastic internal spacing instead of natural document flow.

## Recommended Workflow

For high-fidelity HTML prototype work:

1. Analyze one approved reference screen using Pass 0-10.
2. Create `Design.md` Draft 1 with reference sources, canvas, grid, and module boxes.
3. Create or update `Asset-Spec.md` with placeholder inventory.
4. Build an HTML layout skeleton with stable placeholders.
5. Compare HTML against the reference region by region.
6. Update the difference log.
7. Promote repeated or structural fixes into `Design.md`.
8. Apply HTML fixes.
9. For user-requested changes, run the Change Request Compensation pass and clean up stale rules.
10. Repeat comparison until hard geometry checks pass.
11. Add visual texture checks: shadow, radius, color, type hierarchy, state clarity.
12. After real assets are added, run the asset-dependent checks again.

## Recommended File Placement

For a full product package:

```text
product-name/
├── PRD.md
├── Interaction-Spec.md
├── UI-Style-Checkpoint.md
├── Design.md
├── Asset-Spec.md
├── Docs-Handoff.md
└── prototype/
    └── index.html
```
