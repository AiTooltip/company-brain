# Check for AI Tooltip Updates

**Trigger:** `Check for AI Tooltip updates`

**Official source:** `https://github.com/aitooltip/company-brain`

**Stable channel:** published, non-prerelease GitHub releases tagged `vMAJOR.MINOR.PATCH`

**Outcome:** show a read-only three-way comparison without requiring Git, GitHub CLI, GitHub Desktop, or a GitHub account.

## Procedure

1. Read the operating system, `brain.config.json`, `update-manifest.json`, and this workflow.
2. Run `python3 11-SYSTEM/scripts/check_for_updates.py`.
3. The checker uses standard-library HTTPS to retrieve the latest stable release temporarily. When versions differ, it also retrieves the stable release matching the installed version so it can distinguish local framework customizations from official upstream changes.
4. Show the user:
   - current and latest stable versions;
   - published release notes;
   - framework files added, changed, or retired upstream;
   - possible local framework customizations or missing files;
   - company-owned path collisions and customization conflicts;
   - files that could change safely after approval.
5. State that company-owned and existing unlisted files are not overwrite candidates and nothing was changed.
6. If a safe update exists, ask whether to apply it. Do not interpret the original check request as installation approval.

If the matching installed release cannot be retrieved, customization detection becomes conservative and the update must not be applied automatically. A network/API/release error changes nothing.
