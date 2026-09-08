# Apply an Approved AI Tooltip Update

**Trigger:** `Apply the approved update`

**Precondition:** in the current task, the user has reviewed a fresh update report and explicitly approved that reported stable version and file set.

## Approval gate

Do not run this workflow from a general request to “update,” an old approval, or the check command alone. If the report has conflicts, missing baseline data, a changed license, or unclear local customizations, show them and obtain a specific human resolution before changing files.

## Procedure

1. Re-run the read-only checker immediately so approval is matched to the current latest stable release and local state.
2. Confirm the approved version is still latest and the reported conflict-free file set is unchanged.
3. Run `python3 11-SYSTEM/scripts/apply_approved_update.py --approved` only after the gate is met.
4. The updater may:
   - replace only framework-owned files unchanged from the installed stable baseline;
   - add a newly declared framework file only when nothing already exists at that path;
   - store recoverable local backups under ignored `.company-brain/update-backups/`;
   - update framework version/manifest information supplied by the stable release.
5. The updater must not:
   - overwrite or delete company-owned or existing unlisted files;
   - overwrite locally customized framework files;
   - delete retired framework files automatically;
   - proceed without the matching installed baseline;
   - install a draft, prerelease, arbitrary branch, or non-semantic tag.
6. Validate the repository. If validation fails, roll back applied files and report the failure.
7. Provide an exact report: prior/latest version, files replaced, files added, retired files preserved, conflicts left untouched, backup location, and validation result.

License changes or changes with company-knowledge implications must be highlighted during the check and approved knowingly; a version number alone is not consent to new legal terms or company decisions.
