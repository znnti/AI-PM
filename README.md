# Product Requirements Prototyper

Turn product ideas, feature requests, or rough requirements into structured product deliverables for downstream design and development work.

This Codex skill is built for product managers, product designers, AI prototyping workflows, and implementation handoff scenarios. It supports both full product-delivery chains and scoped work such as PRD repair, interaction repair, UI concept work, HTML prototyping, `Design.md`, `Asset-Spec.md`, and developer handoff.

## What This Skill Does

- Routes requests into product-delivery stages instead of treating every request as one generic writing task.
- Supports full delivery from idea to handoff.
- Supports stage-specific work such as only PRD, only HTML, or only asset planning.
- Supports screen-local refinement such as fixing one page, one button family, one icon group, or one asset batch.
- Separates reusable skill rules from project-specific files.
- Uses `Design.md` and `Asset-Spec.md` as implementation contracts for high-fidelity prototype work.

## Best-Fit Use Cases

- Turn a rough feature idea into a PRD and interaction spec.
- Generate UI concept directions before prototyping.
- Build or repair high-fidelity product HTML prototypes for phone, pad, TV, or web.
- Create or strengthen `Design.md` and `Asset-Spec.md` before asset replacement.
- Prepare developer handoff materials after product and prototype work is stable.

## Operating Modes

- `Full product delivery`
- `Stage-specific delivery`
- `Screen-local refinement`
- `Skill maintenance`

The skill now distinguishes local page repair from full workflow execution, so a request like `fix #home` or `repair one button group` does not automatically reload the entire product-delivery chain.

## Install

### Option 1: Install from GitHub into Codex

If your repo is public and the skill lives at `skills/product-requirements-prototyper`, install it with the Codex GitHub installer:

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo YOUR_GITHUB_NAME/YOUR_REPO_NAME \
  --path skills/product-requirements-prototyper
```

After installing, restart Codex so the new skill is picked up.

### Option 2: Manual install

Copy the skill folder into:

```text
~/.codex/skills/product-requirements-prototyper
```

Then restart Codex.

## Suggested Repository Structure

```text
your-repo/
├── README.md
├── LICENSE
└── skills/
    └── product-requirements-prototyper/
        ├── SKILL.md
        ├── agents/
        │   └── openai.yaml
        ├── references/
        └── assets/
```

## Example Prompts

```text
Use product-requirements-prototyper to turn this product idea into a PRD and interaction spec.
```

```text
Use product-requirements-prototyper to create a high-fidelity HTML prototype for this iPad story app.
```

```text
Use product-requirements-prototyper to repair only index.html#home and update the relevant Design.md and Asset-Spec.md rules.
```

```text
Use product-requirements-prototyper to create developer handoff materials from the existing PRD, Design.md, Asset-Spec.md, and prototype files.
```

## Outputs You Can Expect

- `PRD.md`
- `Interaction-Spec.md`
- `UI concept directions`
- `Design.md`
- `Asset-Spec.md`
- `HTML prototypes`
- `Developer handoff notes`

## Notes

- Keep project-specific decisions in project files, not in the skill.
- Keep the skill references generic and reusable.
- If the user asks for staged confirmation during product delivery, the skill pauses at stage gates.
- If the task is skill maintenance, the skill should complete the maintenance pass continuously unless the user explicitly asks for step-by-step confirmation.
