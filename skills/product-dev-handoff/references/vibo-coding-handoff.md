# Vibo Coding Handoff

Use this handoff format when the prototype and documents will be used by technical teammates or AI coding workflows.

Stage mapping: use this reference only for **Stage 7 - Developer Handoff / 开发交付** in product-delivery tasks. After finishing Stage 7, return to the Stage Gate template in `SKILL.md` and pause unless the user explicitly authorized automatic progression. Do not apply this pause rule to skill-maintenance tasks.

## Handoff Coverage Review

Before writing handoff, restate the implementation scope: feature, screens, devices, stack assumptions, and known exclusions.

Before finishing, audit that the handoff package references:

- PRD and interaction spec
- Design.md and visual rules
- Asset-Spec.md and asset status
- prototype file map and entry URLs/files
- required screens, flows, states, permissions, and data rules
- layout-locked areas and flexible/prototype-only areas
- known limitations, open decisions, and production replacement needs
- implementation priorities and QA focus

Create one canonical `Docs-Handoff.md` entry point. Classify every project document as:

- **Must read**: required before implementation
- **Read when needed**: component or screen-specific contracts
- **Archive / do not deliver**: obsolete, duplicated, or process-only material

Do not keep competing active copies of `Design.md`, `Asset-Spec.md`, or the handoff entry. If device-specific variants are necessary, name and link them explicitly from `Docs-Handoff.md`.

Do not hand off only the HTML if behavior, assets, or requirements are still documented elsewhere.

## Handoff Checklist

- Product goal and user scenario
- Final scope and non-goals
- Required screens
- Required states
- Interaction rules
- Data model sketch
- API assumptions or integration points
- Analytics events
- Permission rules
- Prototype file map
- Known limitations of the prototype
- Implementation priorities
- Canonical file paths and archived duplicates
- Prototype-only mock data, emoji, simulated APIs, and unfinished production integrations

Run `scripts/audit_delivery.py <project-root>` before final handoff. Resolve errors and explain any remaining warnings.

## Engineering Notes

Separate what is fixed from what is illustrative:

- Fixed: requirements, flows, states, validation, data dependencies, permissions.
- Flexible: visual polish, exact copy, animation timing, local mock data.

Treat prototype size as two separate concerns:

- **Browser runtime**: HTML line count alone is rarely the main performance cost; assets, rendering, and event behavior matter more.
- **AI/engineering context**: a monolithic prototype increases token use, edit conflicts, and regression risk.

Do not refactor a stable handoff prototype only to reduce line count. Instead, provide a production decomposition map by screen, component, state, and service when the implementation team will rebuild it in a framework.

## AI Coding Prompt Pattern

```text
Use the attached PRD, interaction spec, and HTML prototype as the source of truth. Implement the product in [target stack]. Preserve the flows, states, information hierarchy, and device-specific behavior. Treat the HTML as a functional reference, not production code. Ask before changing scope.
```
