---
name: dev-handoff
description: Prepare final developer handoff for a concrete project. Use when Codex needs Docs-Handoff.md, implementation notes, canonical file maps, Vibo coding prompts, production limitations, QA priorities, or final package audit before developers implement from PRD, interaction spec, Design.md, Asset-Spec.md, and HTML prototype files. Do not use when maintaining skills themselves or when the task is only product building, interaction design, UI design, HTML skeleton work, or visual asset rendering.
---

# Dev Handoff

## Introduction

This skill prepares a concrete product project for implementation. It gathers stable artifacts into one developer-facing entry point and checks that the package is ready to hand off.

## Scope

- Create or repair the canonical `Docs-Handoff.md` entry point.
- Classify project documents as Must read, Read when needed, or Archive / do not deliver.
- Link PRD, interaction spec, Design.md, Asset-Spec.md, prototype file map, known limitations, implementation priorities, QA focus, and production replacements.
- Use `references/vibo-coding-handoff.md`.
- Use `references/change-impact-guide.md` when handoff changes reveal contradictions in docs or prototype files.

## Required Audit

Run `scripts/audit_delivery.py <project-root>` before final handoff when filesystem access allows it. Resolve errors and explain remaining warnings.

## Boundaries

- Do not use this skill for skill maintenance or dashboard maintenance.
- Do not refactor a stable prototype merely to reduce line count. Provide a decomposition map instead.

## Completion

Summarize handoff readiness, canonical files, audit result, limitations, and implementation priorities. This is normally the final stage, so do not recommend another delivery skill unless a missing upstream artifact needs repair.
