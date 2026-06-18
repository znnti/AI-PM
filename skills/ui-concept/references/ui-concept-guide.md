# UI Concept Guide

Use UI concepts to explore visual direction before coding prototypes. Do not apply a fixed style by default. Derive visual style from product scenario, target user, device context, content density, and comparable products.

Stage mapping: use this reference only for **Stage 3 - UI Concept / UI 风格方向** in product-delivery tasks. After finishing Stage 3, return to the Stage Gate template in `SKILL.md` and pause unless the user explicitly authorized automatic progression. Do not apply this pause rule to skill-maintenance tasks.

## UI Coverage Review

Before generating UI directions or effects, restate the visual scope: target device(s), screens, states, style references, and whether the user expects one representative image or a full screen set.

Before finishing a UI concept or effect set, audit coverage:

- every requested screen/device has a concept or effect prompt
- each direction covers layout, typography, palette, component feel, icon/imagery style, density, depth/shadow, and state treatment
- reference images have been analyzed into reusable rules, not copied blindly
- page effects include realistic content, primary/secondary actions, and important states
- any skipped screen, state, or device is explicitly marked as out of scope

## Style Derivation Workflow

1. Identify the product category and primary user scenario.
2. Identify the user's emotional and functional needs: speed, trust, focus, delight, authority, control, immersion, or clarity.
3. Identify device context: phone, pad, TV, web, kiosk, dashboard, or cross-device journey.
4. Analyze comparable products or competitors when the user names them. If current competitor details matter, browse or ask for references before finalizing the visual direction.
5. Extract reusable visual principles from competitors: navigation model, layout density, card/table usage, typography scale, color role, motion, affordances, and state treatment.
6. Choose 2-4 UI directions and explain why each fits or does not fit the product.
7. For each direction, provide a style sample description and a style-sample image prompt before any final page rendering.
8. Ask the user to confirm one style direction. If none fit, accept reference images and regenerate style options.
9. After style confirmation, generate page-by-page UI effect prompts or images.
10. Ask the user to confirm the page UI effects before generating HTML prototypes through the Stage Gate. Do not proceed to Stage 4 unless the user confirms or has authorized automatic progression.

## Competitor And Reference Analysis

When references are available, summarize them with this structure:

```text
Reference:
Audience:
Core scenario:
Layout pattern:
Navigation pattern:
Information density:
Visual tone:
Useful patterns to borrow:
Patterns to avoid:
Implication for our product:
```

Do not copy a competitor's brand or distinctive visual identity. Borrow product logic and interaction patterns, then create an original design direction.

## UI Checkpoint Flow

Use this sequence:

```text
Style exploration -> Style sample confirmation -> Page-by-page UI effects -> Page UI confirmation -> HTML prototype coding
```

Do not skip directly from style exploration to HTML unless the user explicitly asks for full auto mode.

## Concept Directions

Generate 2-4 directions when the product style is undecided. Each direction should include:

- Direction name
- Suitable users and scenarios
- Mood keywords
- Layout principles
- Color direction and color roles
- Typography direction
- Component feel
- Interaction and motion style
- Example screens to visualize
- Style sample prompt
- Risks or mismatch
- Recommendation

## Reference Image Handling

If the user provides reference images after rejecting proposed styles, analyze them before generating new directions:

- Color palette and contrast
- Typography mood and scale
- Layout rhythm and whitespace
- Information density
- Navigation and component patterns
- Corners, borders, shadows, and depth
- Icon and imagery style
- Motion or interaction cues if visible
- What to borrow and what to avoid

Do not copy the reference image exactly. Convert the visual language into product-appropriate rules.

## Page-By-Page UI Effects

After style confirmation, create UI effect prompts or images for each key screen. For every page include:

- Device target
- Screen goal
- User state
- Content and realistic sample data
- Key components
- Interaction states to show
- Style rules inherited from the confirmed direction

Pause for confirmation after page UI effects. Only then write HTML prototypes.

## Image Prompt Pattern

Use this prompt pattern for representative UI effect images:

```text
High-fidelity [device] UI design for [product/feature], showing [screen and scenario]. Audience: [target user]. Product category: [category]. Visual direction: [direction]. Layout: [navigation, hierarchy, modules]. Comparable product references: [patterns only, no brand copying]. Include: [key components and realistic data]. Avoid: marketing hero pages, fake unreadable text, decorative clutter, copied brand identity. Aspect ratio: [ratio].
```

## Prompt Rules

- Ask for real product screens, not abstract app mockups.
- Include specific data examples when useful.
- Generate separate prompts for phone, pad, TV, and web if the layouts differ.
- Treat generated images as visual reference only; do not rely on them for exact text or spacing.
- After style confirmation, generate page UI effects first.
- After page UI effects are confirmed, translate the confirmed direction and page effects into coded HTML prototype rules.
