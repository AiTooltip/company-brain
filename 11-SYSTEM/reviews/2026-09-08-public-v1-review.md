# Production V1 Public Starter Review

Date: 2026-09-08

Scope: generic starter framework; no company intake or fictional company data

## 1. Non-technical solo user

**Result:** ready, with one owner-supplied content dependency.

- README starts with a five-step ZIP/Codex workflow rather than architecture.
- Git and a GitHub account are not required after download.
- Stable-release checking uses Python HTTPS, not Git, GitHub CLI, or GitHub Desktop.
- Privacy wording accurately distinguishes user-controlled persistent files from cloud AI processing.
- Local identity is configured once and ignored by Git.
- Every required directory contains a tracked useful file.
- The official general AI Tooltip skill locations are explicit, but their authentic source files still need to be inserted by the repository owner.

## 2. Team using a private repository

**Result:** ready for a controlled private-team workflow.

- `COLLABORATION.md` explains clone, pull, review, commit, and push through GitHub Desktop.
- Public framework source and private actual Company Brain are clearly distinguished.
- Shared profiles and local per-computer identity have separate purposes.
- Canonical knowledge and approved-decision conflicts require human resolution; AI cannot silently choose a Git side.
- Meaningful logging excludes surveillance-style chat/tool history.

## 3. Legacy AI Tooltip user

**Result:** both prior systems have exact path maps and an approval-led migration flow.

- AI-DESIGN-SKILLS maps brand brief, core/medium skills, general skills, taste/dislike references, assets, and brand-kit outputs.
- codex-design-studio maps guidelines, design-system source, assets, projects, briefs, outputs, and templates.
- Storybook, Theme Editor, tokens, components, tests, configuration, manifests, and lockfiles have an explicit destination.
- Generated dependencies, caches, secrets, old agents, and obsolete prompts are excluded.
- Conflicts show both sources and likely chronology when known; no automatic winner is selected.

## 4. Framework owner

**Result:** framework updates are separable and conservatively applicable.

- Provider-independent rules live once in `OPERATING-SYSTEM.md`; Codex and Claude Code use lightweight adapters.
- Canonical `01-COMPANY/**`, `03-BRAND/**`, products, projects, research, content, references, assets, outputs, every `DEPARTMENT.md`, and generated brand skills are company-owned.
- Department `AGENTS.md`, Creative framework workflows/templates, migrations, schemas, validators, and update logic are framework-owned.
- Existing unlisted files default to company-owned.
- Updates use published stable semantic releases and a three-way baseline comparison to detect local customization without Git.
- Checks are read-only; application requires a separate explicit command, refuses conflicts/missing baselines, preserves retired files, backs up replacements, validates, and rolls back validation failures.

## Contradiction and complexity audit

- Canonical company identity, audience, strategy, brand, and positioning now have one deterministic home each.
- The mutable company decision index is not framework-owned.
- Placeholder brand skills use `SKILL.template.md`; only a real generated/migrated `SKILL.md` becomes active.
- Generated approximations of the official general AI Tooltip skills were removed and replaced with unmistakable owner-supply markers.
- Goal metadata and the `GOALS → PROJECTS → DECISIONS → ACTIVITY` relationship are explicit.
- Public-source availability is not confused with privacy, offline processing, or open-source licensing.
- Update application never deletes company files or silently resolves custom framework changes.

## Remaining owner actions before v1.0.0

1. Insert the authentic full `no-slop`, `vector-design`, and `ui-ux` `SKILL.md` files and remove their marker files.
2. Obtain professional legal review of `LICENSE.md`; the repository makes no claim that the custom license has been reviewed.
3. Publish and test the stable `v1.0.0` GitHub release so the release API and ZIP-based baseline checks can be exercised end to end.
