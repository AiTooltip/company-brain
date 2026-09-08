#!/usr/bin/env python3
"""Validate the portable Company Brain starter without changing it."""

from __future__ import annotations

import json
from pathlib import Path, PurePosixPath
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[2]
REQUIRED_DIRECTORIES = [
    "00-INBOX",
    "00-MIGRATE-OLD-SETUP",
    "01-COMPANY",
    "01-COMPANY/activity",
    "01-COMPANY/decisions",
    "01-COMPANY/goals",
    "01-COMPANY/history",
    "01-COMPANY/team",
    "02-DEPARTMENTS",
    "02-DEPARTMENTS/Creative",
    "02-DEPARTMENTS/Creative/skills",
    "02-DEPARTMENTS/Creative/skills/general",
    "02-DEPARTMENTS/Creative/skills/general/no-slop",
    "02-DEPARTMENTS/Creative/skills/general/vector-design",
    "02-DEPARTMENTS/Creative/skills/general/ui-ux",
    "02-DEPARTMENTS/Creative/skills/brand-specific",
    "02-DEPARTMENTS/Creative/skills/brand-specific/core-brand",
    "02-DEPARTMENTS/Creative/skills/brand-specific/web-design",
    "02-DEPARTMENTS/Creative/skills/brand-specific/social-media",
    "02-DEPARTMENTS/Creative/skills/brand-specific/presentation",
    "02-DEPARTMENTS/Creative/skills/brand-specific/print-editorial",
    "02-DEPARTMENTS/Creative/skills/brand-specific/motion",
    "02-DEPARTMENTS/Business",
    "02-DEPARTMENTS/Product-and-Development",
    "02-DEPARTMENTS/Analytics",
    "03-BRAND",
    "03-BRAND/guidelines",
    "03-BRAND/voice",
    "03-BRAND/visual",
    "04-PRODUCTS",
    "05-PROJECTS",
    "06-RESEARCH",
    "07-CONTENT",
    "08-REFERENCES",
    "09-ASSETS",
    "09-ASSETS/source",
    "09-ASSETS/working",
    "09-ASSETS/approved",
    "10-OUTPUTS",
    "11-SYSTEM",
    "11-SYSTEM/workflows",
    "11-SYSTEM/templates",
    "11-SYSTEM/schemas",
    "11-SYSTEM/scripts",
    "11-SYSTEM/reviews",
]
REQUIRED_FILES = [
    "AGENTS.md",
    "START-HERE.md",
    "README.md",
    "brain.config.json",
    "update-manifest.json",
    ".gitignore",
    ".company-brain/current-user.example.md",
    "01-COMPANY/decisions/INDEX.md",
    "02-DEPARTMENTS/Creative/skills/general/no-slop/SKILL.md",
    "02-DEPARTMENTS/Creative/skills/general/vector-design/SKILL.md",
    "02-DEPARTMENTS/Creative/skills/general/ui-ux/SKILL.md",
    "11-SYSTEM/templates/project.md",
    "11-SYSTEM/templates/decision.md",
    "11-SYSTEM/templates/product.md",
    "11-SYSTEM/templates/team-member.md",
    "11-SYSTEM/templates/research.md",
    "11-SYSTEM/workflows/initialize-company-brain.md",
    "11-SYSTEM/workflows/process-inbox.md",
    "11-SYSTEM/workflows/start-project.md",
    "11-SYSTEM/workflows/record-approved-decision.md",
    "11-SYSTEM/workflows/log-meaningful-activity.md",
    "11-SYSTEM/workflows/onboard-team-member.md",
    "11-SYSTEM/workflows/migrate-previous-ai-tooltip-setup.md",
    "11-SYSTEM/workflows/check-for-ai-tooltip-updates.md",
]
GENERATED_NAMES = {"node_modules", ".next", ".nuxt", "dist", "build", "coverage", "__pycache__", ".pytest_cache", ".turbo"}


def read_json(relative: str, errors: list[str]) -> dict:
    try:
        return json.loads((ROOT / relative).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"Invalid JSON in {relative}: {error}")
        return {}


def normalized(relative: object) -> bool:
    if not isinstance(relative, str) or not relative:
        return False
    path = PurePosixPath(relative)
    canonical = str(path) + ("/" if relative.endswith("/") else "")
    return (
        not path.is_absolute()
        and ".." not in path.parts
        and ".git" not in path.parts
        and "\\" not in relative
        and canonical == relative
    )


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    for relative in REQUIRED_DIRECTORIES:
        path = ROOT / relative
        if not path.is_dir():
            errors.append(f"Missing required directory: {relative}")
        elif not any(item.is_file() for item in path.iterdir()):
            errors.append(f"Required directory has no direct tracked-file candidate: {relative}")

    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"Missing required file: {relative}")

    config = read_json("brain.config.json", errors)
    manifest = read_json("update-manifest.json", errors)
    for json_file in sorted((ROOT / "11-SYSTEM/schemas").glob("*.json")):
        read_json(json_file.relative_to(ROOT).as_posix(), errors)

    config_version = config.get("framework", {}).get("version") if isinstance(config.get("framework"), dict) else None
    manifest_version = manifest.get("frameworkVersion")
    if config_version != manifest_version:
        errors.append(f"Framework version mismatch: config={config_version!r}, manifest={manifest_version!r}")
    expected_source = "https://github.com/AI-Tooltip/company-brain"
    if config.get("framework", {}).get("source") != expected_source or manifest.get("source") != expected_source:
        errors.append("Config and manifest must use the official AI Tooltip update source.")
    if config.get("framework", {}).get("defaultBranch") != "main" or manifest.get("defaultBranch") != "main":
        errors.append("Config and manifest must use the official main update branch.")
    expected_governance = {
        "humanApprovalRequiredForDecisions": True,
        "humanApprovalRequiredForCompanyKnowledgeReplacement": True,
        "preserveSourceProvenance": True,
        "logEveryAIInteraction": False,
        "meaningfulActivityOnly": True,
    }
    if config.get("governance") != expected_governance:
        errors.append("Governance config does not match the required human-control and meaningful-memory policy.")
    expected_statuses = {"approved", "confirmed", "proposed", "unverified", "conflicting", "superseded"}
    if set(config.get("statusVocabulary", [])) != expected_statuses:
        errors.append("Knowledge status vocabulary is incomplete or contains unsupported values.")
    expected_update_policy = {
        "checkIsReadOnly": True,
        "automaticOverwrite": False,
        "automaticDelete": False,
        "explicitApprovalRequiredToApply": True,
        "companyKnowledgeConflictRequiresExplicitApproval": True,
        "unlistedPathsDefaultToCompanyOwned": True,
    }
    if manifest.get("updatePolicy") != expected_update_policy:
        errors.append("Update policy does not preserve read-only checks and protected company ownership.")

    framework = manifest.get("frameworkOwned", {}).get("files", [])
    company_paths = manifest.get("companyOwned", {}).get("paths", [])
    company_prefixes = manifest.get("companyOwned", {}).get("prefixes", [])
    all_declared = list(framework) + list(company_paths) + list(company_prefixes)
    for relative in all_declared:
        if not normalized(relative):
            errors.append(f"Unsafe or non-normalized manifest path: {relative!r}")
    if len(framework) != len(set(framework)):
        errors.append("frameworkOwned.files contains duplicates.")
    if len(company_paths) != len(set(company_paths)) or len(company_prefixes) != len(set(company_prefixes)):
        errors.append("Company ownership lists contain duplicates.")
    for relative in framework:
        if normalized(relative) and not (ROOT / relative).is_file():
            errors.append(f"Manifest framework file does not exist: {relative}")
    for required in REQUIRED_FILES:
        if required not in framework and required not in company_paths:
            warnings.append(f"Required file has no explicit ownership entry: {required}")

    if "01-COMPANY/company-profile.md" not in company_paths:
        errors.append("The starter company profile must be explicitly company-owned.")
    if "01-COMPANY/decisions/INDEX.md" in framework:
        errors.append("The company decision index must not be framework-owned.")
    brand_skill_prefix = "02-DEPARTMENTS/Creative/skills/brand-specific/"
    if brand_skill_prefix not in company_prefixes:
        errors.append("Brand-specific skills must be protected by a company-owned prefix.")
    allowed_brand_framework_file = brand_skill_prefix + "README.md"
    for relative in framework:
        if relative.startswith(brand_skill_prefix) and relative != allowed_brand_framework_file:
            errors.append(f"Brand-specific company skill is incorrectly framework-owned: {relative}")

    gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8") if (ROOT / ".gitignore").is_file() else ""
    if ".company-brain/current-user.md" not in gitignore:
        errors.append(".gitignore must ignore .company-brain/current-user.md")
    try:
        ignored = subprocess.run(
            ["git", "check-ignore", "-q", ".company-brain/current-user.md"],
            cwd=ROOT,
            check=False,
        ).returncode == 0
        if not ignored:
            errors.append("Git does not currently ignore .company-brain/current-user.md")
        tracked = subprocess.run(
            ["git", "ls-files", "--error-unmatch", ".company-brain/current-user.md"],
            cwd=ROOT,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        ).returncode == 0
        if tracked:
            errors.append(".company-brain/current-user.md must not be tracked by Git")
    except OSError:
        warnings.append("Git was unavailable; local identity ignore behavior could not be verified.")

    for path in ROOT.rglob("*"):
        if ".git" in path.parts or "00-INBOX" in path.parts or "00-MIGRATE-OLD-SETUP" in path.parts:
            continue
        if path.is_dir() and path.name in GENERATED_NAMES:
            warnings.append(f"Generated dependency/cache directory found outside intake: {path.relative_to(ROOT)}")

    print("Company Brain validation")
    for message in errors:
        print(f"ERROR: {message}")
    for message in warnings:
        print(f"WARNING: {message}")
    if not errors and not warnings:
        print("OK: required structure, JSON, ownership, versions, and local identity rules are consistent.")
    else:
        print(f"Summary: {len(errors)} error(s), {len(warnings)} warning(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
