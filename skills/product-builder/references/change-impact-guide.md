# Change Impact Guide

Use this guide when a product change can make HTML, requirements, interaction, visual contracts, assets, or handoff documentation disagree.

## Core Rule

Update only the contracts affected by the change, but never leave a known contradiction. Before editing, classify the change. After editing, search the affected files for the old rule, label, dimension, asset ID, or state.

## Impact Matrix

| Change type | Required checks and updates |
| --- | --- |
| Requirement, scope, or business rule | `PRD.md`; interaction and handoff when behavior or implementation changes |
| Flow, state, navigation, validation, or permission | `Interaction-Spec.md`; HTML; PRD when product scope changes; handoff when implementation behavior changes |
| Repeated layout, typography, button, control, surface, or spacing rule | `Design.md`; affected page/component contract; HTML |
| One-off screen geometry with no reusable rule | Exact HTML and page-level contract; update `Design.md` only when the rule becomes reusable |
| Asset added, removed, resized, renamed, cropped, or changes state | `Asset-Spec.md`; HTML references; owning component contract; handoff when production replacement status changes |
| UI element removed | HTML, interaction rules, asset rows, component contracts, and handoff references that mention it |
| Copy or sample data only | Exact HTML/data source; PRD only when copy is a requirement; mark production data dependencies in handoff |
| Viewport, canvas, device, or global navigation change | `Design.md`, affected HTML screens, relevant contracts, `Asset-Spec.md` dimensions, and handoff |
| Developer handoff or implementation-readiness change | `Docs-Handoff.md`, canonical file map, limitations, production replacements, and decomposition guidance |

## Canonical File Policy

- Keep one active `Design.md`, one active `Asset-Spec.md`, and one active `Docs-Handoff.md` for a prototype scope.
- Use explicit device or package suffixes when multiple active variants are necessary.
- Move obsolete duplicates to an archive folder or rename them with `.archive.md`.
- Link canonical paths from `Docs-Handoff.md`; do not make developers infer precedence from folder position.

## Compensation Pass

When feedback changes an already implemented decision:

1. Search the project for the old text, number, asset ID, state, and CSS/HTML selector.
2. Update the minimum affected contracts from the matrix.
3. Check adjacent states and repeated components for the same assumption.
4. Verify the exact screen and run `scripts/audit_delivery.py` when preparing handoff.
5. State any intentionally stale, illustrative, or archived material.
