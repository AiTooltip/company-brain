#!/usr/bin/env python3
"""Read-only comparison of the installed framework with the official source."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import subprocess
import sys
import tempfile

OFFICIAL_SOURCE = "https://github.com/AI-Tooltip/company-brain"


def fail(message: str, code: int = 1) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(code)


def repository_root() -> Path:
    candidate = Path(__file__).resolve().parents[2]
    if not (candidate / "brain.config.json").is_file():
        fail("Could not locate brain.config.json next to the framework.")
    return candidate


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        fail(f"Cannot read valid JSON from {path}: {error}")
    return {}


def safe_paths(values: object, label: str) -> set[str]:
    if not isinstance(values, list):
        fail(f"{label} must be a list.")
    result: set[str] = set()
    for value in values:
        if not isinstance(value, str) or not value:
            fail(f"{label} contains an invalid path.")
        path = PurePosixPath(value)
        canonical = str(path) + ("/" if value.endswith("/") else "")
        if path.is_absolute() or ".." in path.parts or ".git" in path.parts or "\\" in value or canonical != value:
            fail(f"{label} contains unsafe or non-normalized path: {value}")
        result.add(value)
    return result


def framework_files(manifest: dict, label: str) -> set[str]:
    owned = manifest.get("frameworkOwned")
    if not isinstance(owned, dict):
        fail(f"{label} manifest has no frameworkOwned object.")
    return safe_paths(owned.get("files"), f"{label} frameworkOwned.files")


def digest(root: Path, relative: str) -> str | None:
    path = root / relative
    if not path.exists():
        return None
    try:
        path.resolve().relative_to(root.resolve())
    except ValueError:
        fail(f"Refusing to compare a framework path outside its repository: {relative}")
    if path.is_symlink() or not path.is_file():
        fail(f"Refusing to compare non-regular framework path: {relative}")
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_locally_changed(root: Path, files: set[str]) -> list[str]:
    if not (root / ".git").exists() or not shutil.which("git"):
        return []
    command = ["git", "status", "--porcelain=v1", "--untracked-files=all", "--", *sorted(files)]
    result = subprocess.run(command, cwd=root, text=True, capture_output=True, check=False)
    if result.returncode != 0:
        return []
    changed: list[str] = []
    for line in result.stdout.splitlines():
        if len(line) >= 4:
            changed.append(line[3:])
    return changed


def section(title: str, paths: list[str]) -> None:
    print(f"\n{title} ({len(paths)})")
    if paths:
        for path in paths:
            print(f"  - {path}")
    else:
        print("  None")


def main() -> None:
    root = repository_root()
    config = load_json(root / "brain.config.json")
    local_manifest = load_json(root / "update-manifest.json")
    framework = config.get("framework", {})
    source = framework.get("source")
    branch = framework.get("defaultBranch")
    if source != OFFICIAL_SOURCE or local_manifest.get("source") != OFFICIAL_SOURCE:
        fail(f"Configured update source must be exactly {OFFICIAL_SOURCE}")
    if branch != "main" or local_manifest.get("defaultBranch") != "main":
        fail("Configured update branch and local manifest branch must both be main.")
    if not shutil.which("git"):
        fail("Git is required for the update check but was not found.")

    local_files = framework_files(local_manifest, "local")
    locally_changed = git_locally_changed(root, local_files)

    with tempfile.TemporaryDirectory(prefix="company-brain-update-") as temp_dir:
        remote_root = Path(temp_dir) / "official"
        command = ["git", "clone", "--quiet", "--depth", "1", "--branch", branch, "--single-branch", OFFICIAL_SOURCE, os.fspath(remote_root)]
        result = subprocess.run(command, text=True, capture_output=True, check=False)
        if result.returncode != 0:
            detail = result.stderr.strip() or "unknown Git/network error"
            fail(f"Could not fetch the official public repository: {detail}", 2)

        remote_manifest = load_json(remote_root / "update-manifest.json")
        if remote_manifest.get("source") != OFFICIAL_SOURCE or remote_manifest.get("defaultBranch") != "main":
            fail("The public manifest does not declare the official source and main branch.")
        remote_files = framework_files(remote_manifest, "remote")

        added = sorted(remote_files - local_files)
        removed = sorted(local_files - remote_files)
        common = sorted(local_files & remote_files)
        local_digests = {path: digest(root, path) for path in common}
        remote_digests = {path: digest(remote_root, path) for path in common}
        missing_local = sorted(path for path in common if local_digests[path] is None)
        changed = [
            path
            for path in common
            if local_digests[path] is not None and local_digests[path] != remote_digests[path]
        ]
        addition_collisions = sorted(path for path in added if (root / path).exists())
        missing_remote = sorted(path for path in remote_files if digest(remote_root, path) is None)
        if missing_remote:
            fail("Remote manifest references missing framework files: " + ", ".join(missing_remote))

        local_version = local_manifest.get("frameworkVersion", "unknown")
        remote_version = remote_manifest.get("frameworkVersion", "unknown")
        print("AI Tooltip Company Brain update check (read-only)")
        print(f"Installed version: {local_version}")
        print(f"Latest public version: {remote_version}")
        print(f"Source: {OFFICIAL_SOURCE} ({branch})")
        section("Framework files added upstream", added)
        section("Upstream additions colliding with existing company-owned files", addition_collisions)
        section("Framework files removed upstream", removed)
        section("Framework files different from upstream", changed)
        section("Framework files missing locally", missing_local)
        section("Framework files with uncommitted local changes", sorted(locally_changed))

        if not added and not removed and not changed and local_version == remote_version:
            print("\nResult: the installed framework matches the latest public version.")
        else:
            print("\nResult: framework differences are available for review.")
        print("Company-owned and unlisted files were not candidates for replacement. No files were changed.")


if __name__ == "__main__":
    main()
