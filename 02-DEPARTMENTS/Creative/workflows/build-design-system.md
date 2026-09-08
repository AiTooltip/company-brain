# Build a Design System

**Outcome:** create or migrate an editable, reproducible visual design system at `03-BRAND/visual/design-system/`.

1. Read approved brand/visual guidance, relevant product and goals, current design-system sources, technical decisions, user research, examples, dislikes, and the owning project.
2. Inventory existing tokens, components, Storybook, Theme Editor, documentation, tests, package manifests, lockfiles, licenses, and generated dependencies.
3. Propose scope, supported platforms, token architecture, component priorities, accessibility baseline, ownership, and success criteria. Durable system choices require human approval.
4. Build only the approved scope. The destination may contain tokens, source components, tests, Storybook, Theme Editor, visual documentation, configuration, package manifests, and the applicable lockfile.
5. Never copy `node_modules`, `.next`, `dist`, `build`, caches, coverage, secrets, or reproducible temporary output into the canonical destination.
6. Preserve source editability, component states, theming, accessibility behavior, responsive behavior, and third-party notices. Link rather than duplicate canonical brand facts.
7. Present the system and material implications for review. Do not silently promote a component pattern or generated theme to an approved standard.
8. After approval, record affected decisions, link products/projects/assets, validate reproducibility in an authorized environment, and log the meaningful milestone.
