# PRD Outline

Use this outline for standard product requirement documents. The PRD must be structured, testable, and implementation-facing. Do not write a loose proposal or marketing narrative.

Stage mapping: use this reference only for **Stage 1 - PRD / 产品需求文档** in product-delivery tasks. After finishing Stage 1, return to the Stage Gate template in `SKILL.md` and pause unless the user explicitly authorized automatic progression. Do not apply this pause rule to skill-maintenance tasks.

## PRD Writing Principles

- Start from user scenario and product problem, then derive features.
- Separate facts, assumptions, decisions, and open questions.
- Describe requirements from user value, business objective, system behavior, data rule, permission rule, and acceptance criteria angles.
- Make every core requirement verifiable by design, QA, engineering, or product review.
- Avoid vague verbs such as optimize, enhance, support, empower, or improve unless followed by concrete behavior and measurable criteria.

## PRD Coverage Review

Before writing, restate the PRD scope: product, feature, release, user group, platform, and known exclusions.

Before finishing, audit that the PRD covers:

- problem and evidence
- target users and scenarios
- goals, non-goals, and success metrics
- in-scope and out-of-scope items
- core flows and alternate/failure paths
- functional requirements with acceptance criteria
- screen/content requirements
- data, permissions, integrations, analytics, and compliance when relevant
- risks, tradeoffs, assumptions, and open questions
- release and validation plan

If a section is intentionally not applicable, mark it as `N/A` with a short reason instead of silently omitting it.

## 1. Document Metadata

- Product or feature name
- Version and date
- Author / owner
- Stakeholders
- Target release or milestone
- Related documents or prototypes

## 2. Background And Problem

- Business background
- User pain point
- Current workflow or current solution
- Why this problem matters now
- Evidence, examples, research notes, or assumptions

## 3. Product Goals And Success Metrics

- User goal
- Business goal
- Experience goal
- Operational or technical goal when relevant
- Success metrics: activation, task completion, conversion, retention, satisfaction, efficiency, quality, or cost reduction
- Guardrail metrics and anti-goals

## 4. Target Users And Scenarios

For each user type include:

- User role and characteristics
- Primary scenario
- Job-to-be-done
- Frequency and urgency
- Device or environment
- Key decision points

## 5. Scope

- In scope
- Out of scope
- Non-goals
- Dependencies
- Constraints
- Assumptions

## 6. User Journey And Core Flows

Describe the flow before listing screens:

```text
Entry point -> User intent -> Key action -> System response -> Result -> Next action
```

Include main path, alternate paths, and failure/recovery paths.

## 7. Functional Requirements

Write each requirement with this structure:

```text
ID:
Name:
User value:
Trigger:
Preconditions:
System behavior:
Data involved:
Permission rule:
Priority:
Acceptance criteria:
Edge cases:
```

Acceptance criteria should use observable statements, for example:

```text
Given [context], when [action], then [expected result].
```

## 8. Screen And Content Requirements

For each screen include:

- Screen purpose
- Information hierarchy
- Required modules or components
- Primary action
- Secondary actions
- Required copy or content fields
- State coverage: default, empty, loading, error, success, disabled, permission denied

## 9. Data, Permissions, And Integrations

- Data entities and key fields
- Data source or input method
- Create/read/update/delete rules
- Role permissions
- Privacy or compliance requirements
- API or integration assumptions
- Analytics events

## 10. Risks, Tradeoffs, And Open Questions

- Product risks
- Design risks
- Technical risks
- Operational risks
- Tradeoffs and rejected alternatives
- Decisions needed before development

## 11. Release And Validation Plan

- MVP scope
- Later iterations
- QA focus
- Experiment or rollout plan
- Review checklist before development handoff
