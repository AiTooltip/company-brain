#!/usr/bin/env python3
"""Read-only stable-release comparison; works without Git."""

from __future__ import annotations

import json
from pathlib import Path
import sys

from update_lib import UpdateError, build_plan, repository_root, temporary_workspace


def section(title: str, paths: list[str]) -> None:
    print(f"\n{title} ({len(paths)})")
    if not paths:
        print("  None")
    for path in paths:
        print(f"  - {path}")


def serializable(plan: dict) -> dict:
    return {key: value for key, value in plan.items() if key not in {"latestRoot", "latestManifest"}}


def main() -> int:
    try:
        root = repository_root()
        with temporary_workspace() as temp:
            plan = build_plan(root, Path(temp))
            if "--json" in sys.argv[1:]:
                print(json.dumps(serializable(plan), indent=2))
                return 0

            print("AI Tooltip Company Brain update check (read-only)")
            print(f"Current version: v{plan['currentVersion']}")
            print(f"Latest stable version: v{plan['latestVersion']}")
            print(f"Release: {plan['releaseName']}")
            if plan["publishedAt"]:
                print(f"Published: {plan['publishedAt']}")
            notes = str(plan["releaseNotes"]).strip()
            if notes:
                print("\nRelease changes")
                print(notes[:4000])
                if len(notes) > 4000:
                    print("[Release notes truncated]")
            section("Framework files added in the release", plan["addedUpstream"])
            section("Framework files changed in the release", plan["changedUpstream"])
            section("Framework files retired upstream (not automatically deleted)", plan["removedUpstream"])
            section("Possible local framework customizations", plan["localCustomized"])
            section("Missing local framework files", plan["localMissing"])
            section("Upstream additions colliding with existing company-owned files", plan["additionCollisions"])
            section("Customization conflicts requiring human review", plan["customizationConflicts"])
            section("Sensitive operating, privacy, or license files changed", plan["sensitiveChanges"])
            section("Files that can be safely changed after approval", plan["safeChanged"] + plan["safeAdded"])
            if not plan["baselineAvailable"]:
                print("\nWARNING: The matching installed release could not be retrieved.")
                print(f"Reason: {plan['baselineError']}")
                print("Local customization detection is conservative; do not apply automatically.")

            if plan["localAhead"]:
                print("\nResult: the installed framework version is ahead of the latest stable release; no stable update will be applied.")
            elif not plan["updateAvailable"] and not plan["directDifferences"]:
                print("\nResult: this framework matches the latest stable release.")
            elif not plan["updateAvailable"]:
                print("\nResult: no newer stable release exists, but local framework files differ from the stable baseline. Review local customizations; nothing was changed.")
            elif plan["conflicts"] or not plan["baselineAvailable"]:
                print("\nResult: an update or framework differences exist, with conflicts requiring human review.")
            else:
                print("\nResult: a stable framework update is available for explicit approval.")
                print('After reviewing this report, say: "Apply the approved update."')
            print("Company-owned and existing unlisted files were not overwrite candidates. No files were changed.")
        return 0
    except UpdateError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        print("No files were changed.", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
