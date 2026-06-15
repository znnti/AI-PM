# Interaction Spec

Use this reference to turn requirements into clear product behavior.

Stage mapping: use this reference only for **Stage 2 - Interaction Spec / 交互说明** in product-delivery tasks. After finishing Stage 2, return to the Stage Gate template in `SKILL.md` and pause unless the user explicitly authorized automatic progression. Do not apply this pause rule to skill-maintenance tasks.

## Interaction Coverage Review

Before writing, restate the interaction scope: flows, screens, devices, roles, and states covered.

Before finishing, audit that every in-scope flow has:

- entry point and exit states
- main path
- alternate paths
- failure and recovery paths
- loading, empty, error, success, disabled, and permission states when relevant
- navigation behavior, including back behavior and cross-screen return logic
- input validation and feedback
- state changes caused by taps, clicks, gestures, keyboard, remote, or system events

Cross-check with the PRD: every important requirement should have interaction behavior, and every important interaction should map back to a requirement or scenario.

## Flow Definition

For every core flow include:

- Entry point
- Preconditions
- Main path
- Alternate paths
- Exit states
- Failure states

## Screen Spec

For each screen include:

- Screen purpose
- Primary user action
- Secondary actions
- Content hierarchy
- Components
- Input rules
- Validation rules
- Loading, empty, error, and success states
- Navigation behavior

## Interaction Detail

Specify gestures, clicks, focus behavior, keyboard behavior, remote-control behavior for TV, transitions, disabled states, confirmations, and undo behavior where useful.

## State Matrix

Use a compact matrix for important screens:

```text
State | Trigger | UI response | Data response | Recovery
```
