# Scripts

These utilities use only Python's standard library.

- `validate_brain.py` checks required structure, JSON, ownership declarations, version alignment, local identity ignore rules, tracked starter coverage, and obvious generated-dependency problems. It does not change files.
- `check_for_updates.py` clones the official public source into a temporary directory and compares only manifest-declared framework files. It does not change files in the Company Brain.

Run from anywhere inside the repository with `python3 11-SYSTEM/scripts/<script>.py` when the current directory is the repository root, as documented by the workflows.
