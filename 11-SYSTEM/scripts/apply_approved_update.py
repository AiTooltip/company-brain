#!/usr/bin/env python3
"""Apply a conflict-free stable framework update after explicit approval."""

from __future__ import annotations

from datetime import datetime, timezone
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

from update_lib import UpdateError, build_plan, repository_root, temporary_workspace


def print_paths(title: str, paths: list[str]) -> None:
    print(f"{title} ({len(paths)}):")
    if not paths:
        print("  None")
    for path in paths:
        print(f"  - {path}")


def atomic_copy(source: Path, destination: Path, root: Path) -> None:
    try:
        destination.parent.resolve().relative_to(root.resolve())
    except ValueError as error:
        raise UpdateError(f"Refusing to write outside the Company Brain: {destination}") from error
    if destination.is_symlink() or (destination.exists() and not destination.is_file()):
        raise UpdateError(f"Refusing to replace a non-regular path: {destination.relative_to(root)}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    handle, temporary_name = tempfile.mkstemp(prefix=".company-brain-update-", dir=destination.parent)
    os.close(handle)
    temporary = Path(temporary_name)
    try:
        shutil.copy2(source, temporary)
        os.replace(temporary, destination)
    finally:
        if temporary.exists():
            temporary.unlink()


def main() -> int:
    if sys.argv[1:] != ["--approved"]:
        print(
            "REFUSED: this script requires --approved and may be run only after the user explicitly approves the displayed update.",
            file=sys.stderr,
        )
        return 3
    root = repository_root()
    try:
        with temporary_workspace() as temp:
            plan = build_plan(root, Path(temp))
            if not plan["updateAvailable"]:
                print("No newer stable update is available. Nothing was changed.")
                return 0
            if not plan["baselineAvailable"]:
                raise UpdateError("Cannot safely apply because the matching installed release baseline is unavailable.")
            if plan["conflicts"]:
                detail = "\n  - ".join(plan["conflicts"])
                raise UpdateError(f"Cannot automatically apply while framework/company conflicts exist:\n  - {detail}")

            candidates = sorted(set(plan["safeChanged"]) | set(plan["safeAdded"]))
            if not candidates:
                print("No conflict-free framework files require changes. Nothing was changed.")
                return 0

            latest_root = plan["latestRoot"]
            timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
            backup_root = root / ".company-brain" / "update-backups" / timestamp
            overwritten: list[str] = []
            added: list[str] = []
            validator: subprocess.CompletedProcess[str] | None = None
            try:
                for relative in candidates:
                    destination = root / relative
                    source = latest_root / relative
                    if destination.exists():
                        backup = backup_root / relative
                        backup.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(destination, backup)
                        overwritten.append(relative)
                    else:
                        added.append(relative)
                    atomic_copy(source, destination, root)

                validator = subprocess.run(
                    [sys.executable, os.fspath(root / "11-SYSTEM/scripts/validate_brain.py")],
                    cwd=root,
                    text=True,
                    capture_output=True,
                    check=False,
                )
                if validator.returncode != 0:
                    raise UpdateError("Updated framework failed validation:\n" + validator.stdout + validator.stderr)
            except (OSError, UpdateError) as error:
                for relative in overwritten:
                    atomic_copy(backup_root / relative, root / relative, root)
                for relative in added:
                    target = root / relative
                    if target.is_file() and not target.is_symlink():
                        target.unlink()
                raise UpdateError(f"Update failed and applied files were rolled back: {error}") from error

            if validator is None:
                raise UpdateError("Update validation did not run.")

            print(f"Applied AI Tooltip Company Brain v{plan['currentVersion']} → v{plan['latestVersion']} after explicit approval.")
            print_paths("Framework files updated", overwritten)
            print_paths("Framework files added", added)
            print_paths("Framework files retired upstream but preserved locally", plan["removedUpstream"])
            print_paths("Conflicts left untouched", plan["conflicts"])
            print(f"Backup: {backup_root.relative_to(root)}")
            print("Company-owned and existing unlisted files were not overwritten or deleted.")
            print("\nValidation output")
            print(validator.stdout.rstrip())
            return 0
    except UpdateError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
