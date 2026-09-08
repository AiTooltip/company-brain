# System Maintenance Instructions

Apply the root `AGENTS.md` first.

System work changes how the Company Brain operates, so keep it generic, portable, comprehensible to non-technical users, and free of company-specific assumptions. Maintain alignment among `AGENTS.md`, `START-HERE.md`, `brain.config.json`, `update-manifest.json`, workflows, templates, schemas, and scripts.

Never use a framework update or migration to replace company-owned files automatically. Update checks are read-only. Proposed framework changes should be reviewable, and changes with company implications require explicit approval.

After modifying framework structure, run `python3 11-SYSTEM/scripts/validate_brain.py` and review its warnings rather than suppressing them without cause.
