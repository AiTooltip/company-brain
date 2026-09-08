# AI-DESIGN-SKILLS Migration Map

Use this map when the intake root is named `AI-DESIGN-SKILLS` or its contents match these paths. Matching is case-insensitive where the host filesystem permits, but preserve the original source path in provenance.

## Exact source map

| Legacy path | New destination | Action and review rule |
| --- | --- | --- |
| `brand/brand-brief.md` | Split into `01-COMPANY/COMPANY.md`, `01-COMPANY/audience.md`, `01-COMPANY/strategy.md`, `03-BRAND/BRAND.md`, and `03-BRAND/positioning.md` | Extract by canonical topic; do not copy the whole brief into every file. Mark claims and ask about conflicts. |
| `brand/core-brand/SKILL.md` | `02-DEPARTMENTS/Creative/skills/brand-specific/core-brand/SKILL.md` | Preserve as company-owned; compare with canonical brand truth and require approval before activation/merge. |
| `skills/website-ui/` | `02-DEPARTMENTS/Creative/skills/brand-specific/web-design/` | Preserve real company-specific skill/resources; adapt legacy name, do not activate obsolete framework instructions. |
| `skills/social-media/` | `02-DEPARTMENTS/Creative/skills/brand-specific/social-media/` | Preserve company-specific content and provenance. |
| `skills/presentation/` | `02-DEPARTMENTS/Creative/skills/brand-specific/presentation/` | Preserve company-specific content and provenance. |
| `skills/print-editorial/` | `02-DEPARTMENTS/Creative/skills/brand-specific/print-editorial/` | Preserve company-specific content and provenance. |
| `skills/motion/` | `02-DEPARTMENTS/Creative/skills/brand-specific/motion/` | Preserve company-specific content and provenance. |
| `skills/no-slop/` | `02-DEPARTMENTS/Creative/skills/general/no-slop/` | Compare with the official current AI Tooltip skill. If customized, present preserve/merge/replace choices; never overwrite blindly. |
| `skills/vector-design/` | `02-DEPARTMENTS/Creative/skills/general/vector-design/` | Compare with the official current AI Tooltip skill. If customized, present preserve/merge/replace choices; never overwrite blindly. |
| `references/brand-taste/` | `08-REFERENCES/brand-taste/` | Preserve useful references with origin, rights, and why they matter. |
| `references/dislike/` | `08-REFERENCES/dislikes/` | Preserve as explicit negative references; do not universalize one example. |
| `references/website-ui/` | `08-REFERENCES/web-design/` | Preserve useful sources and metadata. |
| `references/social-media/` | `08-REFERENCES/social-media/` | Preserve useful sources and metadata. |
| `references/presentation/` | `08-REFERENCES/presentation/` | Preserve useful sources and metadata. |
| `references/print-editorial/` | `08-REFERENCES/print-editorial/` | Preserve useful sources and metadata. |
| `references/motion/` | `08-REFERENCES/motion/` | Preserve useful sources and metadata. |
| `references/other/` | `08-REFERENCES/other/` or a more specific canonical area | Classify by substance; keep provenance. |
| `assets/logos/` | `09-ASSETS/source/logos/` or `09-ASSETS/approved/logos/` | Preserve editable/highest-fidelity source; approval status must be evidenced. |
| `assets/fonts/` | `09-ASSETS/source/fonts/` | Preserve only when licensing permits; retain license notices and font source. |
| `assets/photography/` | `09-ASSETS/source/photography/` or `approved/` | Preserve origin, creator, license, consent, and approval status when known. |
| `assets/illustrations/` | `09-ASSETS/source/illustrations/` or `approved/` | Preserve editable source and rights/status. |
| `assets/existing-brand-material/` | `09-ASSETS/source/existing-brand-material/` and/or `08-REFERENCES/` | Separate reusable assets from reference-only historical material. |
| `brand/brand-kit.md` | `03-BRAND/guidelines/` | Preserve as sourced guideline input; reconcile with canonical files. |
| `brand/brand-kit.pdf` | `10-OUTPUTS/brand/` and link from guidelines | Preserve intentional deliverable; do not treat PDF presence as current approval. |

## General skill comparison

An existing general skill may contain user modifications. Compare its actual content with the official skill supplied in the V1 starter or stable update release. If the official skill is not yet supplied, preserve the legacy file separately and report that comparison is pending. Ask the user whether to preserve, merge, or replace; no option is automatic.

## Framework material

Do not activate legacy system prompts, agent personas, setup/update logic, or generic workflow instructions. Useful builder/refiner functionality now lives in `02-DEPARTMENTS/Creative/workflows/`.

## Conflicts

If this system conflicts with another legacy system or current canonical knowledge, show source A, source B, the exact difference, status/authority, and likely chronology when supported. Do not pick a winner. Update canonical knowledge only after the user identifies the current source.
