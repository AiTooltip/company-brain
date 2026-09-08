---
name: ui-ux
description: Design, implement, or critique usable, accessible, responsive digital interfaces and product flows with proportionate UX methods and intentional visual design. Use for websites, web apps, mobile apps, dashboards, onboarding, forms, navigation, and other interactive experiences. Do not use for non-interactive graphics, logos, or presentation layouts.
---

# UI/UX

Create interfaces that are clear, useful, accessible, and visually distinctive without turning every project into the same polished template.

This is a universal execution and quality skill. It does not define a brand's visual identity. For branded work, combine it with the Core Brand Skill, approved Brand Kit and assets, any brand-specific Website/UI Skill, and the No Slop Skill.

## Core Principle

Make expected behavior familiar and make the expression distinctive.

Use conventions where predictability helps people understand, navigate, enter information, recover from errors, or complete a task. Create character through typography, composition, rhythm, imagery, motion, interaction, and content-specific details that do not reduce comprehension.

Treat named UX laws as heuristics rather than universal formulas. Apply them to the user, task, context, and evidence. Do not use a law to justify a decision automatically.

## Start With the Experience

Before choosing a layout, establish:

- who the primary user is
- the user's most important task or desired outcome
- the business or product outcome
- the context of use, including device, environment, frequency, and urgency
- known content, technical constraints, accessibility needs, and risk
- what is known from evidence, what is assumed, and what still needs validation

Ask only the questions whose answers could materially change the flow or design. If reasonable assumptions are necessary, state them. Never invent research findings, analytics, user quotes, or validation.

## Scale the Method to the Risk

Use the smallest UX process that can responsibly answer the design problem.

- For a simple marketing page, define the audience, message hierarchy, primary action, responsive behavior, and accessibility requirements, then perform a focused critique.
- For a new feature or multi-step task, map the main flow, alternatives, errors, states, information architecture, and validation plan before polishing the interface.
- For unfamiliar, consequential, or high-risk behavior, recommend research and testing with representative users before treating the solution as resolved.

Do not perform every UX exercise by default. A method must answer a real question.

## Working Process

1. Define the primary user, task, success condition, and constraints.
2. Map the shortest credible primary path plus important alternative, recovery, and exit paths.
3. Organize content and actions before styling the screen.
4. Establish hierarchy in low fidelity: sequence, grouping, navigation, emphasis, and density.
5. Explore two or more materially different structural directions when the composition is not obvious. Do not present superficial color variations as concepts.
6. Choose a direction by how well it supports the task, content, brand, and context.
7. Define interaction behavior and applicable states.
8. Apply the visual system and add a deliberate creative idea.
9. Inspect the rendered experience at representative sizes and input modes.
10. Test, critique, and refine. Clearly distinguish expert review from actual user validation.

## Choose UX Methods Intentionally

Use methods according to the uncertainty:

- interviews or contextual inquiry to understand motivations, language, environment, and existing behavior
- task analysis or jobs-to-be-done framing to clarify what people are trying to accomplish
- journey mapping only when the experience meaningfully unfolds across time, stages, or channels
- card sorting and tree testing for uncertain or complex information architecture
- low-fidelity prototypes to answer structural questions before visual polish creates attachment
- usability testing with representative users, early and repeatedly, to observe learnability, efficiency, errors, and satisfaction
- heuristic evaluation to identify likely problems, not as a substitute for user research
- analytics or experiments after release when traffic, measurement, and ethical conditions support them
- accessibility review throughout, not as a final decoration pass

## Apply Usability Principles

Use these principles as a reasoning set:

- Keep system status visible. Acknowledge actions promptly and make progress, completion, delay, and failure understandable.
- Match the user's language and mental model. Prefer clear domain terms over internal product terminology.
- Preserve control. Provide back, cancel, close, undo, or escape where people may change their minds.
- Follow useful conventions. Similar elements should behave similarly; platform expectations should not be broken for novelty.
- Prevent errors where practical. Use constraints, previews, sensible defaults, examples, and confirmation for consequential actions.
- Make recovery specific. Preserve entered data and explain what happened, where it happened, and how to fix it.
- Favor recognition over recall. Keep choices, context, labels, and relevant information visible when needed.
- Support both new and experienced users. Add accelerators or shortcuts without making the basic path cryptic.
- Remove irrelevant competition. Minimalism means prioritization, not emptiness.
- Provide help where the task genuinely needs it, close to the moment of need.

Use common UX laws with judgment:

- **Fitts's Law:** make frequent or important targets easy to reach and select; consider size, distance, spacing, and thumb reach.
- **Hick's Law:** structure and group complex choices; do not hide necessary options merely to reduce their visible count.
- **Jakob's Law:** preserve familiar behavior for common controls and flows; put originality into the brand expression and product-specific moments.
- **Gestalt principles:** use proximity, similarity, alignment, continuity, and common region to communicate relationships before adding decoration.
- **Progressive disclosure:** reveal advanced complexity when it becomes relevant while keeping essential consequences visible.
- **Aesthetic-usability effect:** use craft to improve confidence and approachability, but never let polish conceal unclear behavior.
- **Tesler's Law:** manage unavoidable complexity deliberately instead of pushing all of it onto the user.

Do not treat Miller's 7±2 as a fixed interface limit or quote psychology as proof without context.

## Information Architecture and Content

- Organize around user goals and content relationships, not the application's internal structure.
- Use labels people can predict before clicking.
- Make the current location and available next steps clear.
- Keep navigation stable enough to build confidence.
- Lead with the information required to decide or act; move supporting detail closer to where it becomes useful.
- Write interface copy that is direct, specific, and consistent. Buttons should describe their action.
- Design with realistic content, long labels, empty values, localization, and edge cases rather than ideal placeholder text.

## Interaction and State Design

Define every state that is relevant to the experience, including:

- default, hover, focus, active, selected, and disabled
- loading, empty, partial, success, warning, and error
- permission, authentication, offline, or destructive states when applicable

Do not add states that the product cannot actually support.

Provide immediate, proportional feedback. Preserve user input through errors. Use optimistic updates only when failure is unlikely, reversible, and clearly recoverable. Never hide essential information behind hover alone.

Use confirmation selectively. Reserve interruptive confirmation for irreversible, costly, or surprising consequences; use undo for safely reversible actions.

## Accessibility Baseline

For web work, target the current WCAG 2.2 Level AA criteria unless the project specifies a stricter or platform-specific standard.

- Use semantic structure and native controls where possible.
- Support complete keyboard operation with a visible focus indicator that is not obscured.
- Give controls persistent or programmatically available names and instructions.
- Associate validation messages with the relevant field and explain recovery.
- Do not use color, motion, position, shape, or sound as the only way to communicate meaning.
- Meet applicable text and non-text contrast requirements.
- Support text resizing, zoom, reflow, and readable line lengths without loss of content or function.
- Give pointer and touch targets sufficient size and separation under the applicable standard and platform guidance.
- Respect reduced-motion preferences and avoid unnecessary vestibular triggers.
- Keep reading order, focus order, visual order, and interaction order coherent.
- Provide appropriate text alternatives, captions, transcripts, and status announcements when the content requires them.

Accessibility is a design constraint and a source of creative clarity. Do not trade it away for a visual effect.

## Responsive and Cross-Input Design

- Let content and behavior determine breakpoints; do not design only for named devices.
- Recompose hierarchy when space changes instead of shrinking a desktop composition.
- Test narrow, wide, short, zoomed, and content-heavy conditions.
- Support touch, pointer, keyboard, and assistive technology as applicable.
- Avoid accidental horizontal scrolling, clipped actions, unreachable content, and controls that depend on hover.
- Consider reachability, safe areas, browser chrome, virtual keyboards, and orientation where relevant.

## Create Distinctive Visual Design

Begin with a clear visual and behavioral concept, not a component-library demo.

Choose a small number of intentional ideas that fit the product and brand, such as:

- a distinctive typographic voice or scale relationship
- an editorial or content-led composition
- purposeful asymmetry or spatial tension
- an unusual but legible navigation rhythm
- product-specific interaction, motion, illustration, or data expression
- a meaningful relationship between imagery, interface, and content

Build hierarchy through scale, contrast, spacing, position, rhythm, and sequence before adding containers or effects.

Use a consistent system of type, color, spacing, grids, icons, radii, elevation, and motion, but do not let the system dictate every composition. Consistency belongs in rules and behavior; variety belongs in how those rules answer different content.

Do not force content into cards, dashboards, hero formulas, bento grids, pill controls, gradients, glass effects, or repeated section rhythms unless they solve a specific problem. Apply the No Slop Skill for the full anti-template critique.

Creativity must improve identity, meaning, emotion, or comprehension. If a novelty makes the task harder, revise it.

## Components and Design Systems

- Reuse tokens, behavior, and interaction patterns before reusing whole compositions.
- Create components for genuinely repeated patterns, not every isolated object.
- Define meaningful variants and states rather than duplicating near-identical components.
- Keep component APIs and names aligned with purpose, not visual appearance alone.
- Allow intentional exceptions when content or hierarchy demands them; document the reason.
- Avoid premature abstraction that locks an untested pattern into the system.

## Review the Actual Experience

Do not judge only from source code, a component list, or a single ideal screenshot. Inspect the rendered design.

At minimum, verify:

- the primary task and action are clear without explanation
- navigation, hierarchy, and labels match the user's mental model
- important feedback, errors, and recovery paths exist
- applicable interaction states are designed and functional
- keyboard order, visible focus, semantics, contrast, zoom, and target sizing are sound
- the layout survives representative viewport sizes, real content, long text, empty data, and errors
- creative choices feel connected to the brand or product rather than applied as decoration
- the interface does not resemble a generic template because of unnecessary cards, uniform blocks, stock styling, or repetitive cadence
- claims of usability are supported by evidence; untested assumptions remain labeled as assumptions

If the design passes expert review but has not been tested with users, say so. Recommend the smallest useful test rather than claiming the experience is validated.

## Output Standard

Deliver a coherent experience, not only attractive screens.

When useful, briefly state:

- the intended user and primary task
- the chosen structure and why it supports that task
- the intentional creative idea
- important interaction and accessibility decisions
- assumptions or risks that still need validation

Keep the explanation proportional to the work. The result should remain understandable without the explanation.
