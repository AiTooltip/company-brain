# codex-design-studio Migration Map

Use this map when the intake root is named `codex-design-studio` or its contents match these paths. Preserve source paths in provenance and keep authored code structure intact when changing it would break imports.

## Exact source map

| Legacy path | New destination | Action and review rule |
| --- | --- | --- |
| `brand-system/BRAND_GUIDELINES.md` | Split/link into `03-BRAND/BRAND.md`, `positioning.md`, `voice/`, `visual/`, and `guidelines/` | Extract by canonical topic; preserve the original as a reference/output when useful. Do not duplicate the whole file. |
| `brand-system/design-system/` | `03-BRAND/visual/design-system/` | Preserve authored tokens, components, tests, Storybook, Theme Editor, documentation, configuration, manifest, and lockfile. Exclude generated dependencies/builds. |
| `assets/brand/` | `09-ASSETS/source/` or `09-ASSETS/approved/` | Classify by editability and verified approval; keep rights/provenance. |
| `assets/inspiration/` | `08-REFERENCES/inspiration/` | Preserve as reference evidence, not approved brand rules. |
| `assets/content/` | `09-ASSETS/source/content/`, `07-CONTENT/`, or `10-OUTPUTS/` | Route source assets, editable content records, and final deliverables by substance. |
| `projects/` | `05-PROJECTS/` | Map meaningful active/historical projects to current `PROJECT.md`; exclude dependency/build directories inside them. |
| `briefs/` | Related project folder or `08-REFERENCES/briefs/` | Attach active briefs to their project; preserve unmatched briefs as references. |
| `outputs/` | `10-OUTPUTS/` | Preserve intentional deliverables with project/status links; exclude reproducible build noise. |
| `templates/` | `08-REFERENCES/legacy-templates/` or appropriate project/design-system source | Preserve only useful company-specific templates; do not replace framework templates. |

## Design-system preservation

Preserve authored:

- design tokens, themes, and presets;
- source components, stories, tests, and documentation;
- `.storybook` configuration;
- Theme Editor source, schemas, and non-secret configuration;
- package manifest and the applicable lockfile;
- third-party license and attribution notices.

Do not migrate:

- `node_modules/`, `.next/`, `dist/`, `build/`, coverage, or caches;
- `.DS_Store`, `__MACOSX`, runtime logs, or generated temporary files;
- populated `.env` files, credentials, keys, tokens, or authentication state;
- obsolete `AGENTS.md`, framework prompts, personas, or legacy setup/update instructions;
- reproducible compiled bundles when preserved source exists.

## Conflicts

If this system conflicts with `AI-DESIGN-SKILLS` or current canonical knowledge, show source A, source B, the exact difference, status/authority, and likely chronology only when supported. Do not pick a winner. Ask which is current before changing canonical files.

## Report categories

Report knowledge, skills, assets, references, design system, projects, and outputs migrated; duplicates skipped; framework files ignored; conflicts resolved by a human; and unresolved conflicts.
