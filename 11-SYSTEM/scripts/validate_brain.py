#!/usr/bin/env python3
"""Validate the production V1 Company Brain starter without changing it."""

from __future__ import annotations

import json
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[2]
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")

REQUIRED_DIRECTORIES = [
    "00-INBOX", "00-MIGRATE-OLD-SETUP",
    "01-COMPANY", "01-COMPANY/activity", "01-COMPANY/decisions", "01-COMPANY/goals", "01-COMPANY/history", "01-COMPANY/team",
    "02-DEPARTMENTS", "02-DEPARTMENTS/Creative", "02-DEPARTMENTS/Business", "02-DEPARTMENTS/Product-and-Development", "02-DEPARTMENTS/Analytics",
    "02-DEPARTMENTS/Creative/skills", "02-DEPARTMENTS/Creative/skills/general", "02-DEPARTMENTS/Creative/skills/brand-specific", "02-DEPARTMENTS/Creative/workflows",
    "02-DEPARTMENTS/Creative/skills/general/no-slop", "02-DEPARTMENTS/Creative/skills/general/vector-design", "02-DEPARTMENTS/Creative/skills/general/ui-ux",
    "02-DEPARTMENTS/Creative/skills/brand-specific/core-brand", "02-DEPARTMENTS/Creative/skills/brand-specific/web-design", "02-DEPARTMENTS/Creative/skills/brand-specific/social-media",
    "02-DEPARTMENTS/Creative/skills/brand-specific/presentation", "02-DEPARTMENTS/Creative/skills/brand-specific/print-editorial", "02-DEPARTMENTS/Creative/skills/brand-specific/motion",
    "03-BRAND", "03-BRAND/guidelines", "03-BRAND/voice", "03-BRAND/visual", "03-BRAND/visual/design-system",
    "04-PRODUCTS", "05-PROJECTS", "06-RESEARCH", "07-CONTENT", "08-REFERENCES",
    "09-ASSETS", "09-ASSETS/source", "09-ASSETS/working", "09-ASSETS/approved", "10-OUTPUTS",
    "11-SYSTEM", "11-SYSTEM/workflows", "11-SYSTEM/templates", "11-SYSTEM/schemas", "11-SYSTEM/scripts", "11-SYSTEM/migrations", "11-SYSTEM/reviews",
]

REQUIRED_FILES = [
    "README.md", "START-HERE.md", "PRIVACY.md", "COLLABORATION.md", "LICENSE.md",
    "AGENTS.md", "CLAUDE.md", "brain.config.json", "update-manifest.json", ".gitignore", ".company-brain/current-user.example.md",
    "11-SYSTEM/OPERATING-SYSTEM.md", "11-SYSTEM/RELEASING.md",
    "01-COMPANY/COMPANY.md", "01-COMPANY/audience.md", "01-COMPANY/strategy.md", "01-COMPANY/decisions/INDEX.md",
    "03-BRAND/BRAND.md", "03-BRAND/positioning.md", "03-BRAND/visual/design-system/README.md",
    "02-DEPARTMENTS/Creative/DEPARTMENT.md", "02-DEPARTMENTS/Business/DEPARTMENT.md",
    "02-DEPARTMENTS/Product-and-Development/DEPARTMENT.md", "02-DEPARTMENTS/Analytics/DEPARTMENT.md",
    "11-SYSTEM/templates/project.md", "11-SYSTEM/templates/decision.md", "11-SYSTEM/templates/product.md",
    "11-SYSTEM/templates/team-member.md", "11-SYSTEM/templates/research.md", "11-SYSTEM/templates/goal.md",
    "11-SYSTEM/schemas/project.schema.json", "11-SYSTEM/schemas/decision.schema.json", "11-SYSTEM/schemas/product.schema.json",
    "11-SYSTEM/schemas/team-member.schema.json", "11-SYSTEM/schemas/research.schema.json", "11-SYSTEM/schemas/goal.schema.json",
    "11-SYSTEM/migrations/ai-design-skills.md", "11-SYSTEM/migrations/codex-design-studio.md",
    "11-SYSTEM/workflows/initialize-company-brain.md", "11-SYSTEM/workflows/process-inbox.md", "11-SYSTEM/workflows/start-project.md",
    "11-SYSTEM/workflows/record-approved-decision.md", "11-SYSTEM/workflows/log-meaningful-activity.md", "11-SYSTEM/workflows/onboard-team-member.md",
    "11-SYSTEM/workflows/migrate-previous-ai-tooltip-setup.md", "11-SYSTEM/workflows/check-for-ai-tooltip-updates.md", "11-SYSTEM/workflows/apply-approved-update.md",
    "02-DEPARTMENTS/Creative/workflows/build-core-brand.md", "02-DEPARTMENTS/Creative/workflows/build-brand-skill.md",
    "02-DEPARTMENTS/Creative/workflows/refine-brand-skill.md", "02-DEPARTMENTS/Creative/workflows/build-brand-kit.md",
    "02-DEPARTMENTS/Creative/workflows/build-design-system.md",
    "11-SYSTEM/scripts/check_for_updates.py", "11-SYSTEM/scripts/apply_approved_update.py", "11-SYSTEM/scripts/update_lib.py",
]

GENERAL_SKILLS = ["no-slop", "vector-design", "ui-ux"]
BRAND_SKILLS = ["core-brand", "web-design", "social-media", "presentation", "print-editorial", "motion"]
COMPANY_PREFIXES_REQUIRED = [
    "01-COMPANY/", "03-BRAND/", "04-PRODUCTS/", "05-PROJECTS/", "06-RESEARCH/",
    "07-CONTENT/", "08-REFERENCES/", "09-ASSETS/", "10-OUTPUTS/",
]
GENERATED_NAMES = {
    "node_modules", ".next", ".nuxt", "dist", "build", "coverage", "__pycache__",
    ".pytest_cache", ".turbo", "__MACOSX",
}


def read_json(relative: str, errors: list[str]) -> dict:
    try:
        value = json.loads((ROOT / relative).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"Invalid JSON in {relative}: {error}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"Expected a JSON object in {relative}")
        return {}
    return value


def normalized(relative: object, prefix: bool = False) -> bool:
    if not isinstance(relative, str) or not relative:
        return False
    path = PurePosixPath(relative)
    canonical = str(path) + ("/" if prefix else "")
    return (
        not path.is_absolute() and ".." not in path.parts and ".git" not in path.parts
        and "\\" not in relative and relative.endswith("/") == prefix and canonical == relative
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

    if (ROOT / "01-COMPANY/company-profile.md").exists():
        errors.append("Obsolete company-profile.md exists; COMPANY.md is the canonical company record.")

    config = read_json("brain.config.json", errors)
    manifest = read_json("update-manifest.json", errors)
    for json_file in sorted((ROOT / "11-SYSTEM/schemas").glob("*.json")):
        read_json(json_file.relative_to(ROOT).as_posix(), errors)

    framework_config = config.get("framework", {}) if isinstance(config.get("framework"), dict) else {}
    config_version = framework_config.get("version")
    manifest_version = manifest.get("frameworkVersion")
    if config_version != manifest_version or not isinstance(config_version, str) or not SEMVER.fullmatch(config_version):
        errors.append(f"Framework semantic version mismatch/invalid: config={config_version!r}, manifest={manifest_version!r}")
    if manifest.get("releaseTag") != f"v{manifest_version}":
        errors.append("Manifest releaseTag must equal v plus frameworkVersion.")
    official_source = "https://github.com/aitooltip/company-brain"
    release_api = "https://api.github.com/repos/aitooltip/company-brain/releases"
    if framework_config.get("source") != official_source or manifest.get("source") != official_source:
        errors.append("Config and manifest must use the official AI Tooltip source.")
    if framework_config.get("releaseApi") != release_api:
        errors.append("Config must use the official GitHub releases API.")
    if framework_config.get("updateChannel") != "stable-releases" or manifest.get("updateChannel") != "stable-releases":
        errors.append("Config and manifest must use stable-releases, not an arbitrary branch, as the update channel.")
    if framework_config.get("developmentBranch") != "main":
        errors.append("The documented development branch must be main.")

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
        errors.append("Knowledge status vocabulary is incomplete or unsupported.")

    expected_update_policy = {
        "channel": "stable-releases", "semanticReleaseTags": True, "checkIsReadOnly": True,
        "gitRequiredForCheck": False, "automaticInstall": False, "automaticOverwrite": False,
        "automaticDelete": False, "explicitApprovalRequiredToApply": True,
        "companyKnowledgeConflictRequiresExplicitApproval": True,
        "localFrameworkCustomizationRequiresReview": True, "unlistedPathsDefaultToCompanyOwned": True,
    }
    if manifest.get("updatePolicy") != expected_update_policy:
        errors.append("Update policy is not the required stable, read-only-check, explicit-approval policy.")

    framework = manifest.get("frameworkOwned", {}).get("files", [])
    sensitive = manifest.get("frameworkOwned", {}).get("sensitiveReviewFiles", [])
    company_paths = manifest.get("companyOwned", {}).get("paths", [])
    company_prefixes = manifest.get("companyOwned", {}).get("prefixes", [])
    for relative in list(framework) + list(sensitive) + list(company_paths):
        if not normalized(relative):
            errors.append(f"Unsafe/non-normalized manifest file path: {relative!r}")
    for relative in company_prefixes:
        if not normalized(relative, prefix=True):
            errors.append(f"Unsafe/non-normalized company prefix: {relative!r}")
    if len(framework) != len(set(framework)) or len(company_paths) != len(set(company_paths)) or len(company_prefixes) != len(set(company_prefixes)):
        errors.append("Manifest ownership lists contain duplicates.")
    if not set(sensitive).issubset(set(framework)):
        errors.append("Every sensitiveReviewFiles path must also be framework-owned.")
    if set(framework) & set(company_paths):
        errors.append("A path is declared both framework-owned and company-owned.")
    for relative in framework:
        if normalized(relative) and not (ROOT / relative).is_file():
            errors.append(f"Manifest framework file does not exist: {relative}")

    retired_owner = "AI-" + "Tooltip"
    obsolete_repository_references = [
        f"github.com/{retired_owner}/company-brain",
        f"api.github.com/repos/{retired_owner}/company-brain",
    ]
    for relative in framework:
        path = ROOT / relative
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for obsolete in obsolete_repository_references:
            if obsolete.lower() in text.lower():
                errors.append(f"Framework file still references the retired repository location: {relative}")

    markdown_link = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    link_files = {path for path in set(framework) | set(REQUIRED_FILES) if path.endswith(".md")}
    for relative in sorted(link_files):
        document = ROOT / relative
        if not document.is_file():
            continue
        for target in markdown_link.findall(document.read_text(encoding="utf-8")):
            target = target.strip().strip("<>").split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (document.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"Local link escapes the repository in {relative}: {target}")
                continue
            if not resolved.exists():
                errors.append(f"Broken local link in {relative}: {target}")

    for prefix in COMPANY_PREFIXES_REQUIRED:
        if prefix not in company_prefixes:
            errors.append(f"Required company-owned prefix missing: {prefix}")
        for relative in framework:
            if relative.startswith(prefix):
                errors.append(f"Company knowledge path is incorrectly framework-owned: {relative}")

    for department in ["Creative", "Business", "Product-and-Development", "Analytics"]:
        context = f"02-DEPARTMENTS/{department}/DEPARTMENT.md"
        instructions = f"02-DEPARTMENTS/{department}/AGENTS.md"
        if context not in company_paths or context in framework:
            errors.append(f"Department context must be explicitly company-owned: {context}")
        if instructions not in framework:
            errors.append(f"Department instructions must be framework-owned: {instructions}")

    for canonical in [
        "01-COMPANY/COMPANY.md", "01-COMPANY/audience.md", "01-COMPANY/strategy.md",
        "03-BRAND/BRAND.md", "03-BRAND/positioning.md",
    ]:
        if canonical not in company_paths or canonical in framework:
            errors.append(f"Canonical starter must be explicitly company-owned: {canonical}")

    for name in GENERAL_SKILLS:
        folder = ROOT / "02-DEPARTMENTS/Creative/skills/general" / name
        active = folder / "SKILL.md"
        marker = folder / "OFFICIAL-SKILL-REQUIRED.md"
        if not active.is_file() and not marker.is_file():
            errors.append(f"General skill {name} needs either the official SKILL.md or the explicit owner marker.")
        if active.is_file() and marker.is_file():
            errors.append(f"General skill {name} has both an active skill and an official-skill-required marker.")

    placeholder_signals = ["[not provided]", "status: unverified", "status: proposed", "do not activate as `skill.md`", "official skill required"]
    for skill in ROOT.glob("02-DEPARTMENTS/Creative/skills/**/SKILL.md"):
        text = skill.read_text(encoding="utf-8").lower()
        if any(signal in text for signal in placeholder_signals):
            errors.append(f"Active SKILL.md appears to be a placeholder: {skill.relative_to(ROOT)}")
        relative = skill.relative_to(ROOT).as_posix()
        if "/brand-specific/" in relative and relative in framework:
            errors.append(f"Generated brand-specific skill must be company-owned: {relative}")

    for name in BRAND_SKILLS:
        template = ROOT / "02-DEPARTMENTS/Creative/skills/brand-specific" / name / "SKILL.template.md"
        if not template.is_file():
            errors.append(f"Missing inactive brand skill template: {template.relative_to(ROOT)}")

    gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8") if (ROOT / ".gitignore").is_file() else ""
    required_ignores = [
        ".company-brain/current-user.md", ".company-brain/update-downloads/", ".company-brain/update-backups/",
        ".DS_Store", "__MACOSX/", "node_modules/", ".next/", "dist/", "build/", ".env",
    ]
    for pattern in required_ignores:
        if pattern not in gitignore:
            errors.append(f".gitignore is missing required pattern: {pattern}")
    if (ROOT / ".git").exists() and shutil.which("git"):
        ignored = subprocess.run(["git", "check-ignore", "-q", ".company-brain/current-user.md"], cwd=ROOT, check=False).returncode == 0
        if not ignored:
            errors.append("Git does not ignore .company-brain/current-user.md")
        tracked = subprocess.run(
            ["git", "ls-files", "--error-unmatch", ".company-brain/current-user.md"], cwd=ROOT,
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False,
        ).returncode == 0
        if tracked:
            errors.append(".company-brain/current-user.md must not be tracked by Git")

    for path in ROOT.rglob("*"):
        if ".git" in path.parts or "00-INBOX" in path.parts or "00-MIGRATE-OLD-SETUP" in path.parts:
            continue
        if path.is_dir() and path.name in GENERATED_NAMES:
            warnings.append(f"Generated dependency/cache directory found outside intake: {path.relative_to(ROOT)}")

    license_text = (ROOT / "LICENSE.md").read_text(encoding="utf-8") if (ROOT / "LICENSE.md").is_file() else ""
    if "AI Tooltip Company Brain Limited Use License" not in license_text or "© 2026 AI Tooltip. All rights reserved." not in license_text:
        errors.append("LICENSE.md is missing its required title or copyright notice.")

    print("Company Brain V1 validation")
    for message in errors:
        print(f"ERROR: {message}")
    for message in warnings:
        print(f"WARNING: {message}")
    if not errors and not warnings:
        print("OK: production structure, ownership, privacy, license, adapters, skills, migrations, releases, and local identity rules are consistent.")
    else:
        print(f"Summary: {len(errors)} error(s), {len(warnings)} warning(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
