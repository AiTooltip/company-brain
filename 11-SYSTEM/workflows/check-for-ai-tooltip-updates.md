# Check for AI Tooltip Updates

**Trigger:** `Check for AI Tooltip updates`

**Official source:** `https://github.com/AI-Tooltip/company-brain`

**Outcome:** compare this installed framework with the latest public `main` version and report a safe update plan. This workflow is read-only unless the user later explicitly approves an update.

## Procedure

1. Read the root manual, `brain.config.json`, `update-manifest.json`, and this workflow.
2. Confirm the configured source is exactly the official repository above. Do not silently switch sources.
3. Run:

   `python3 11-SYSTEM/scripts/check_for_updates.py`

4. The script fetches the official public repository into a temporary directory, reads its manifest, and compares framework-owned files. It must not edit Company Brain files.
5. Report:
   - installed and latest framework versions;
   - added, removed, and changed framework-owned files;
   - locally modified framework files that need careful review;
   - any manifest/config error or unavailable network state;
   - a reminder that unlisted and company-owned files were not compared for replacement.

## If the user asks to apply an update

That is a separate, explicit operation. Before writing:

1. Ensure the worktree can be reviewed and preserve unrelated changes.
2. Use the **remote manifest's framework-owned list only** for candidate framework files. A newly declared framework path may be added after approval only when no file already exists there.
3. Show locally modified framework files and meaningful behavior changes.
4. Never delete or replace an existing path classified as company-owned by the local manifest. If an upstream addition collides with an existing unlisted file, preserve the local company file and report the collision.
5. Treat every existing unlisted path as company-owned. A currently absent path is not company knowledge and may receive a newly declared framework file after review and explicit approval.
6. If a framework change implies a change to company knowledge or brand-specific skills, preserve the company file and request explicit approval for any later reconciliation.
7. Apply only what the human approved, validate the brain, and provide a reviewable diff.

An update version number is not permission to overwrite anything.
