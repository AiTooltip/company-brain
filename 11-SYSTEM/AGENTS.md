# System Maintenance Instructions

Follow `11-SYSTEM/OPERATING-SYSTEM.md` first. Provider adapters cannot weaken it.

System work changes how the Company Brain operates, so keep it generic, portable, comprehensible to non-technical users, and free of company-specific assumptions. Maintain alignment among `OPERATING-SYSTEM.md`, provider adapters, `README.md`, `START-HERE.md`, privacy/collaboration/license documents, configuration, ownership manifest, workflows, templates, schemas, migrations, and scripts.

Never use a framework update or migration to replace company-owned files automatically. Update checks are read-only and use stable releases. Proposed framework changes should be reviewable, and changes with company or legal implications require explicit approval.

After modifying framework structure, run `python3 11-SYSTEM/scripts/validate_brain.py` and review its warnings rather than suppressing them without cause.
