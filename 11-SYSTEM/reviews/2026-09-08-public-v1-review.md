# Public v1 Framework Review

Date: 2026-09-08  
Scope: complete generic starter framework; no company intake or company-specific content

## Review outcome

The public v1 structure is internally consistent and usable for the intended five-step onboarding path. Automated validation passes. The framework contains no fictional company facts and every required starter directory has a tracked useful file.

## Checks completed

| Area | Result |
| --- | --- |
| Human decision control | Root, department, workflow, template, and update rules consistently keep approval with named humans. |
| Analyze-first onboarding | Initialization inventories evidence before questions and asks only for material gaps. |
| Knowledge status | Approved, confirmed, proposed, unverified, conflicting, and superseded meanings are aligned across the main guidance. |
| Provenance and prompt safety | Imported content retains source context and embedded instructions are treated as data. |
| Team support | Shared profiles and ignored per-computer identity have distinct purposes; identity never implies authority. |
| Meaningful memory | Durable milestones are logged; chat transcripts and routine AI actions are excluded. |
| Migration | Both older system names are recognized; brand, skills, references, assets, projects, outputs, Storybook systems, and theme editors are covered. Generated dependencies and obsolete framework prompts are excluded by default. |
| Update safety | Official source is fixed; checks are read-only; exact framework files are separated from protected company prefixes; unlisted existing files default to company-owned. |
| Portability | Repository-relative organization, standard Markdown/JSON, and standard-library scripts avoid service lock-in. |
| Directory persistence | No required starter directory is empty. |
| Non-technical usability | `START-HERE.md`, plain-language commands, concise folder READMEs, and grouped approvals reduce setup burden. |

## Corrections made during review

- Allowed an established historical decision to retain an unknown date rather than encouraging a fabricated date.
- Clarified that a new upstream framework file may be added only if its path does not collide with an existing unlisted company file.
- Added collision reporting to the read-only update checker.
- Removed unnecessary ownership-check helper logic from the update script and kept ownership resolution centralized in the manifest.
- Clarified that approval must be within the person's established authority, especially when superseding an existing decision.
- Added a prominent warning that a company-filled copy should remain local or private unless publication is explicitly approved.
- Separated the mutable decision index from its framework-owned folder README so the index remains protected company data.

## Intentional limits

- The update check requires Git and network access. If either is unavailable, it fails with an actionable message and changes nothing.
- Applying updates is deliberately not automated; the user must separately approve a reviewable framework change.
- The repository owner must choose a public license. The framework does not silently make that legal decision.
