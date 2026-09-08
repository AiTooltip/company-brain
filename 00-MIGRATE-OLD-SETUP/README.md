# Migrate an Older AI Tooltip Setup

Place a complete `AI-DESIGN-SKILLS` or `codex-design-studio` folder here, then tell Codex: **Migrate my previous AI Tooltip setup**.

The migration is extractive, not destructive. Codex should preserve useful company-owned information and leave the original folder unchanged until you approve cleanup.

Expected to preserve when useful:

- brand facts, guidelines, and brand-specific skills;
- references and source material;
- source and approved assets;
- active or historically meaningful projects;
- intentional outputs and deliverables;
- Storybook design systems, tokens, components, and documentation;
- theme editor source, configuration, presets, and documentation.

Expected to exclude unless a person asks otherwise:

- obsolete system prompts and agent instructions from the old framework;
- duplicated framework instructions and generic skills already supplied here;
- generated dependencies and caches such as `node_modules`, build output, coverage, and temporary files;
- secrets, credentials, machine-local state, and irrelevant logs;
- reproducible generated bundles when their source exists.

See `11-SYSTEM/workflows/migrate-previous-ai-tooltip-setup.md` plus the exact maps in `11-SYSTEM/migrations/ai-design-skills.md` and `11-SYSTEM/migrations/codex-design-studio.md` for the complete recognition and review process.
