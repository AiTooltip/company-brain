#!/usr/bin/env python3
"""Standard-library helpers for stable Company Brain release updates."""

from __future__ import annotations

import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import tempfile
from typing import Any
import urllib.error
import urllib.request
import zipfile

OFFICIAL_SOURCE = "https://github.com/aitooltip/company-brain"
RELEASE_API = "https://api.github.com/repos/aitooltip/company-brain/releases"
USER_AGENT = "AI-Tooltip-Company-Brain-Updater/1.0"
MAX_ARCHIVE_BYTES = 200 * 1024 * 1024
MAX_EXTRACTED_BYTES = 500 * 1024 * 1024
SEMVER_TAG = re.compile(r"^v(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")


class UpdateError(RuntimeError):
    """Expected safe update failure with a user-readable message."""


def repository_root() -> Path:
    root = Path(__file__).resolve().parents[2]
    if not (root / "brain.config.json").is_file():
        raise UpdateError("Could not locate brain.config.json next to the framework.")
    return root


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise UpdateError(f"Cannot read valid JSON from {path}: {error}") from error
    if not isinstance(value, dict):
        raise UpdateError(f"Expected a JSON object in {path}.")
    return value


def safe_paths(values: object, label: str) -> set[str]:
    if not isinstance(values, list):
        raise UpdateError(f"{label} must be a list.")
    result: set[str] = set()
    for value in values:
        if not isinstance(value, str) or not value:
            raise UpdateError(f"{label} contains an invalid path.")
        path = PurePosixPath(value)
        if (
            path.is_absolute()
            or ".." in path.parts
            or ".git" in path.parts
            or "\\" in value
            or str(path) != value
        ):
            raise UpdateError(f"{label} contains an unsafe or non-normalized path: {value}")
        result.add(value)
    return result


def safe_prefixes(values: object, label: str) -> set[str]:
    if not isinstance(values, list):
        raise UpdateError(f"{label} must be a list.")
    result: set[str] = set()
    for value in values:
        if not isinstance(value, str) or not value.endswith("/"):
            raise UpdateError(f"{label} contains an invalid prefix.")
        trimmed = value[:-1]
        path = PurePosixPath(trimmed)
        if (
            not trimmed or path.is_absolute() or ".." in path.parts or ".git" in path.parts
            or "\\" in value or str(path) != trimmed
        ):
            raise UpdateError(f"{label} contains an unsafe or non-normalized prefix: {value}")
        result.add(value)
    return result


def framework_files(manifest: dict[str, Any], label: str) -> set[str]:
    owned = manifest.get("frameworkOwned")
    if not isinstance(owned, dict):
        raise UpdateError(f"{label} manifest has no frameworkOwned object.")
    return safe_paths(owned.get("files"), f"{label} frameworkOwned.files")


def validate_manifest(manifest: dict[str, Any], label: str) -> None:
    if manifest.get("source") != OFFICIAL_SOURCE:
        raise UpdateError(f"{label} manifest does not declare the official source.")
    channel = manifest.get("updateChannel")
    if channel != "stable-releases":
        raise UpdateError(f"{label} manifest must use the stable-releases update channel.")
    version = manifest.get("frameworkVersion")
    if not isinstance(version, str) or not SEMVER_TAG.fullmatch(f"v{version}"):
        raise UpdateError(f"{label} manifest has an invalid semantic framework version: {version!r}")
    files = framework_files(manifest, label)
    if manifest.get("releaseTag") != f"v{version}":
        raise UpdateError(f"{label} manifest releaseTag does not match its framework version.")
    sensitive = safe_paths(
        manifest.get("frameworkOwned", {}).get("sensitiveReviewFiles"),
        f"{label} frameworkOwned.sensitiveReviewFiles",
    )
    if not sensitive.issubset(files):
        raise UpdateError(f"{label} manifest has a sensitive review path that is not framework-owned.")
    company = manifest.get("companyOwned")
    if not isinstance(company, dict):
        raise UpdateError(f"{label} manifest has no companyOwned object.")
    company_paths = safe_paths(company.get("paths"), f"{label} companyOwned.paths")
    safe_prefixes(company.get("prefixes"), f"{label} companyOwned.prefixes")
    if files & company_paths:
        raise UpdateError(f"{label} manifest declares a path as both framework-owned and company-owned.")
    policy = manifest.get("updatePolicy")
    required_policy = {
        "channel": "stable-releases",
        "semanticReleaseTags": True,
        "checkIsReadOnly": True,
        "gitRequiredForCheck": False,
        "automaticInstall": False,
        "automaticOverwrite": False,
        "automaticDelete": False,
        "explicitApprovalRequiredToApply": True,
        "companyKnowledgeConflictRequiresExplicitApproval": True,
        "localFrameworkCustomizationRequiresReview": True,
        "unlistedPathsDefaultToCompanyOwned": True,
    }
    if policy != required_policy:
        raise UpdateError(f"{label} manifest does not preserve the required update safety policy.")


def version_tuple(version: str) -> tuple[int, int, int]:
    match = SEMVER_TAG.fullmatch(f"v{version}")
    if not match:
        raise UpdateError(f"Invalid semantic version: {version!r}")
    return tuple(int(part) for part in match.groups())


def _request_json(url: str) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        headers={"Accept": "application/vnd.github+json", "User-Agent": USER_AGENT},
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            data = response.read(2 * 1024 * 1024 + 1)
    except urllib.error.HTTPError as error:
        if error.code == 404:
            raise UpdateError("No matching stable GitHub release has been published yet.") from error
        raise UpdateError(f"GitHub release service returned HTTP {error.code}: {error.reason}") from error
    except (urllib.error.URLError, TimeoutError, OSError) as error:
        raise UpdateError(f"Could not contact the official GitHub release service: {error}") from error
    if len(data) > 2 * 1024 * 1024:
        raise UpdateError("GitHub release metadata was unexpectedly large.")
    try:
        value = json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise UpdateError(f"GitHub returned invalid release metadata: {error}") from error
    if not isinstance(value, dict):
        raise UpdateError("GitHub returned unexpected release metadata.")
    return value


def release_metadata(tag: str | None = None) -> dict[str, Any]:
    if tag is not None and not SEMVER_TAG.fullmatch(tag):
        raise UpdateError(f"Refusing invalid release tag: {tag}")
    url = f"{RELEASE_API}/latest" if tag is None else f"{RELEASE_API}/tags/{tag}"
    metadata = _request_json(url)
    release_tag = metadata.get("tag_name")
    if not isinstance(release_tag, str) or not SEMVER_TAG.fullmatch(release_tag):
        raise UpdateError(f"Official release has a non-semantic tag: {release_tag!r}")
    if metadata.get("draft") or metadata.get("prerelease"):
        raise UpdateError(f"Release {release_tag} is not a stable published release.")
    archive = metadata.get("zipball_url")
    expected_prefix = "https://api.github.com/repos/aitooltip/company-brain/zipball/"
    if not isinstance(archive, str) or not archive.startswith(expected_prefix):
        raise UpdateError("Official release metadata contains an unexpected archive URL.")
    return metadata


def _download(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json", "User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            chunks: list[bytes] = []
            total = 0
            while True:
                chunk = response.read(1024 * 1024)
                if not chunk:
                    break
                total += len(chunk)
                if total > MAX_ARCHIVE_BYTES:
                    raise UpdateError("Official release archive exceeds the 200 MB safety limit.")
                chunks.append(chunk)
    except UpdateError:
        raise
    except (urllib.error.URLError, TimeoutError, OSError) as error:
        raise UpdateError(f"Could not download the official release archive: {error}") from error
    return b"".join(chunks)


def _safe_extract(archive: bytes, destination: Path) -> Path:
    try:
        bundle = zipfile.ZipFile(io.BytesIO(archive))
    except zipfile.BadZipFile as error:
        raise UpdateError("The official release download is not a valid ZIP archive.") from error
    roots: set[str] = set()
    extracted_bytes = 0
    for item in bundle.infolist():
        path = PurePosixPath(item.filename)
        if path.is_absolute() or ".." in path.parts or not path.parts:
            raise UpdateError(f"Release archive contains an unsafe path: {item.filename}")
        mode = (item.external_attr >> 16) & 0o170000
        if mode == 0o120000:
            raise UpdateError(f"Release archive contains an unsupported symbolic link: {item.filename}")
        extracted_bytes += item.file_size
        if extracted_bytes > MAX_EXTRACTED_BYTES:
            raise UpdateError("Official release archive exceeds the 500 MB extracted-size safety limit.")
        roots.add(path.parts[0])
    if len(roots) != 1:
        raise UpdateError("Official release archive has an unexpected root structure.")
    for item in bundle.infolist():
        path = PurePosixPath(item.filename)
        target = destination.joinpath(*path.parts)
        if item.is_dir():
            target.mkdir(parents=True, exist_ok=True)
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        with bundle.open(item) as source, target.open("wb") as output:
            shutil.copyfileobj(source, output)
    root = destination / next(iter(roots))
    if not (root / "update-manifest.json").is_file():
        raise UpdateError("Official release archive does not contain update-manifest.json.")
    return root


def download_release(metadata: dict[str, Any], parent: Path) -> Path:
    archive_url = metadata.get("zipball_url")
    if not isinstance(archive_url, str):
        raise UpdateError("Release archive URL is missing.")
    release_root = _safe_extract(_download(archive_url), parent)
    manifest = load_json(release_root / "update-manifest.json")
    validate_manifest(manifest, f"release {metadata.get('tag_name', 'unknown')}")
    expected_tag = f"v{manifest.get('frameworkVersion')}"
    if metadata.get("tag_name") != expected_tag:
        raise UpdateError(
            f"Release tag {metadata.get('tag_name')} does not match manifest version {manifest.get('frameworkVersion')}."
        )
    for relative in framework_files(manifest, "release"):
        source = release_root / relative
        if not source.is_file() or source.is_symlink():
            raise UpdateError(f"Release manifest references a missing or unsupported framework file: {relative}")
    return release_root


def digest(root: Path, relative: str) -> str | None:
    path = root / relative
    if not path.exists():
        return None
    try:
        path.resolve().relative_to(root.resolve())
    except ValueError as error:
        raise UpdateError(f"Refusing a framework path outside its repository: {relative}") from error
    if path.is_symlink() or not path.is_file():
        raise UpdateError(f"Refusing a non-regular framework path: {relative}")
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _changed(left_root: Path, right_root: Path, paths: set[str]) -> set[str]:
    return {path for path in paths if digest(left_root, path) != digest(right_root, path)}


def build_plan(root: Path, work: Path) -> dict[str, Any]:
    config = load_json(root / "brain.config.json")
    local_manifest = load_json(root / "update-manifest.json")
    validate_manifest(local_manifest, "local")
    framework = config.get("framework")
    if not isinstance(framework, dict):
        raise UpdateError("brain.config.json has no framework object.")
    if framework.get("source") != OFFICIAL_SOURCE or framework.get("updateChannel") != "stable-releases":
        raise UpdateError("Configuration must use the official stable-release update source.")
    current_version = framework.get("version")
    if current_version != local_manifest.get("frameworkVersion"):
        raise UpdateError("Configured and manifest framework versions do not match.")

    latest_metadata = release_metadata()
    latest_root = download_release(latest_metadata, work / "latest")
    latest_manifest = load_json(latest_root / "update-manifest.json")
    latest_version = latest_manifest["frameworkVersion"]
    update_available = version_tuple(latest_version) > version_tuple(str(current_version))
    local_ahead = version_tuple(latest_version) < version_tuple(str(current_version))
    local_files = framework_files(local_manifest, "local")
    latest_files = framework_files(latest_manifest, "latest")

    baseline_root: Path | None = None
    baseline_manifest: dict[str, Any] | None = None
    baseline_error: str | None = None
    if current_version == latest_version:
        baseline_root = latest_root
        baseline_manifest = latest_manifest
    else:
        try:
            current_metadata = release_metadata(f"v{current_version}")
            baseline_root = download_release(current_metadata, work / "current")
            baseline_manifest = load_json(baseline_root / "update-manifest.json")
        except UpdateError as error:
            baseline_error = str(error)

    baseline_files = framework_files(baseline_manifest, "installed release") if baseline_manifest else local_files
    added_upstream = latest_files - baseline_files
    removed_upstream = baseline_files - latest_files
    shared_releases = baseline_files & latest_files
    changed_upstream = _changed(baseline_root, latest_root, shared_releases) if baseline_root else set(shared_releases)

    local_customized: set[str] = set()
    local_missing: set[str] = set()
    if baseline_root:
        for path in local_files & baseline_files:
            local_hash = digest(root, path)
            if local_hash is None:
                local_missing.add(path)
            elif local_hash != digest(baseline_root, path):
                local_customized.add(path)
    else:
        local_customized = {path for path in local_files if digest(root, path) is not None}
        local_missing = {path for path in local_files if digest(root, path) is None}

    addition_collisions = {
        path for path in added_upstream if (root / path).exists() or (root / path).is_symlink()
    }
    customization_conflicts = local_customized & changed_upstream
    conflicts = addition_collisions | customization_conflicts | local_missing
    safe_changed = (changed_upstream - conflicts) & local_files & latest_files
    safe_added = added_upstream - addition_collisions
    if not update_available or baseline_root is None:
        safe_changed = set()
        safe_added = set()
    direct_differences = {
        path
        for path in local_files & latest_files
        if digest(root, path) != digest(latest_root, path)
    }
    sensitive_files = set(latest_manifest.get("frameworkOwned", {}).get("sensitiveReviewFiles", []))
    sensitive_changes = (added_upstream | changed_upstream | removed_upstream) & sensitive_files

    return {
        "currentVersion": current_version,
        "latestVersion": latest_version,
        "updateAvailable": update_available,
        "localAhead": local_ahead,
        "latestTag": latest_metadata.get("tag_name"),
        "releaseName": latest_metadata.get("name") or latest_metadata.get("tag_name"),
        "publishedAt": latest_metadata.get("published_at"),
        "releaseNotes": latest_metadata.get("body") or "",
        "latestRoot": latest_root,
        "latestManifest": latest_manifest,
        "baselineAvailable": baseline_root is not None,
        "baselineError": baseline_error,
        "addedUpstream": sorted(added_upstream),
        "removedUpstream": sorted(removed_upstream),
        "changedUpstream": sorted(changed_upstream),
        "localCustomized": sorted(local_customized),
        "localMissing": sorted(local_missing),
        "additionCollisions": sorted(addition_collisions),
        "customizationConflicts": sorted(customization_conflicts),
        "conflicts": sorted(conflicts),
        "safeChanged": sorted(safe_changed),
        "safeAdded": sorted(safe_added),
        "directDifferences": sorted(direct_differences),
        "sensitiveChanges": sorted(sensitive_changes),
    }


def temporary_workspace() -> tempfile.TemporaryDirectory[str]:
    return tempfile.TemporaryDirectory(prefix="company-brain-release-")
