# Scripts

These utilities use only Python's standard library.

- `validate_brain.py` checks required structure, JSON, ownership declarations, version alignment, local identity ignore rules, tracked starter coverage, skill placeholder safety, and obvious generated-dependency problems. It does not change files.
- `check_for_updates.py` uses Python HTTPS to compare the installed framework with the latest stable GitHub release. It performs no writes and requires no Git installation.
- `apply_approved_update.py` applies only conflict-free framework files after the user has explicitly approved the update. It preserves company files, keeps retired files, backs up replaced files locally, validates, and rolls back on validation failure.
- `update_lib.py` contains shared safe-release download, extraction, version, comparison, and ownership logic.

Run from anywhere inside the repository with `python3 11-SYSTEM/scripts/<script>.py` when the current directory is the repository root, as documented by the workflows.
