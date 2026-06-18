# Asset Spec Guide

Use this guide when a high-fidelity HTML prototype contains image, icon, cover, avatar, or illustration placeholders that will be filled later.

Stage mapping: use this reference only for **Stage 6 - Asset Spec / 资产规格** in product-delivery tasks. After finishing Stage 6, return to the Stage Gate template in `SKILL.md` and pause unless the user explicitly authorized automatic progression. Do not apply this pause rule to skill-maintenance tasks.

## Role In The Product Workflow

`Asset-Spec.md` is a project deliverable produced after the high-fidelity HTML skeleton and before final asset generation/replacement. It connects the product/interaction intent, the approved visual direction, and the exact HTML asset slots.

Do not treat asset work as an unrelated art task. It is part of the full product handoff chain:

```text
Product idea
→ Stage 1 PRD
→ Stage 2 Interaction Spec
→ Stage 3 UI Concept
→ Stage 4 HTML Prototype
→ Stage 6 Asset-Spec.md
→ Asset generation/replacement
→ Stage 7 Developer Handoff
```

## When To Create It

Create or update `Asset-Spec.md` when:

- The HTML contains green dashed asset placeholders.
- The user wants to generate icons, covers, illustrations, avatars, hero images, or thumbnails later.
- A project has multiple screens and assets need stable IDs for review.
- The HTML skeleton has been accepted but visual assets are not final.

## Required Columns

For each asset slot, include:

- `ID`: stable ID shown in the HTML placeholder.
- `Screen`: page or state where the asset appears.
- `Location`: precise UI area, such as top bar, hero card, navigation grid, content card, detail panel, or media control area.
- `Purpose`: what the asset communicates.
- `Size / Ratio`: CSS slot size and crop behavior.
- `Target Format`: expected output format, such as PNG, transparent PNG, SVG, CSS only, video, or other agreed format.
- `Visual Direction`: style, mood, subject, and constraints.
- `Prompt Notes`: concise generation prompt ingredients.
- `Source / File`: generated or replacement file path when available.
- `Status`: one of `待绘制`, `已生成`, `已替换`, `需调整`, `已确认`.

These are the minimum columns. For high-fidelity product work, `Asset-Spec.md` should be treated as a slot contract, not only a production list.

Add these contract fields whenever the slot participates in layout-sensitive UI:

- `Component / Region`: which button, tab, card, row, toolbar, panel, or navigation item owns the slot.
- `Anchor / Crop`: center, top, top-left, face-safe, subject-safe, fill, contain, or other crop/anchor rule.
- `Overflow Policy`: whether the real asset must stay inside the box or may visually overflow it.
- `State Usage`: whether the slot changes by normal, selected, disabled, locked, current, hover/focus, or error state.
- `Replacement Constraint`: what must not change after replacement, such as button height, text baseline, card width, row padding, or module alignment.

Recommended high-fidelity column shape:

```text
ID | Screen | Location | Component/Region | Purpose | Size/Ratio | Target Format | Anchor/Crop | Overflow Policy | State Usage | Visual Direction | Prompt Notes | Source/File | Replacement Constraint | Status
```

## Asset Coverage Review

Before generating or replacing assets, restate the asset scope: one slot, one module, one screen, one format group, or the full visible page.

Default scope for long product conversations should be one screen/page at a time. Do not fill assets across every page in a prototype by default, even if multiple pages already exist. Multi-page asset replacement is allowed only when the user explicitly asks for it or when a resumable page ledger is already in place.

Before finishing, audit that:

- every in-scope HTML placeholder or planned slot has an `Asset-Spec.md` row
- every row includes ID, screen/location, container size, target format, visual direction, source/file, and status
- the generated/replaced file format matches `Target Format`
- no old temporary crop, placeholder class, green dashed slot, or stale source path remains in completed regions
- asset replacement did not alter layout dimensions, typography, spacing, baseline alignment, or card size
- any intentionally pending slot is clearly marked with status and reason

## ID Prefixes

Use stable prefixes so the HTML, asset spec, and final files stay aligned:

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

## Authoring Rules

- Every green dashed placeholder in HTML must have exactly one row in `Asset-Spec.md`.
- Every row in `Asset-Spec.md` must correspond to a visible placeholder or a planned asset slot.
- If a slot belongs to a button, tab, navigation row, or repeated card control, record the owning component so later asset replacement does not silently distort the component contract defined in `Design.md`.
- When temporary icons are removed from an HTML skeleton, immediately add replacement placeholder rows for the same functional positions. Do not leave future icon locations as text-only controls unless the final design is explicitly CSS/text-only.
- Do not change HTML layout dimensions during asset replacement.
- If an image does not crop well, adjust the image composition or crop, not the HTML slot.
- Keep prompts short enough to be actionable but specific enough to preserve product context and visual style.
- Group assets by screen first, then by visual hierarchy.
- If the requested scope is "fill assets for this screen", inventory every visible slot on that screen, including small button icons, row-end action icons, state badges, and empty-state illustrations. Do not stop at the largest hero or cover art.
- After one screen's asset fill is complete, summarize covered slots before moving to the next screen. Treat each page as a separately auditable unit.

## File Naming

When assets are generated, save files with the asset ID first:

```text
assets/
├── A01-primary-avatar.png
├── H01-hero-background.png
├── C01-feature-icon.png
└── M01-cover-artwork.png
```

## Verification

After replacing placeholders with assets:

- Check that no text or UI controls shift.
- Check that every image fills its slot without distortion.
- Check that important subjects are not cropped out.
- Check that small icons remain recognizable at actual rendered size.
- Update `Status` and `Source / File` in `Asset-Spec.md`.
- Check that replacement did not break button padding, icon/text gap, row height, card baseline alignment, or selected-state backgrounds defined in `Design.md`.

## Completion Threshold

Do not treat `Asset-Spec.md` as complete unless:

- every in-scope visible slot has a row
- each row has enough information to generate or replace the asset without guessing layout behavior
- small but layout-critical slots are covered, not only large imagery
- replacement constraints protect the surrounding HTML from accidental visual drift
