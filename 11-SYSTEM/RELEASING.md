# Stable Release Process

This is for the AI Tooltip framework owner, not ordinary Company Brain users.

1. Develop and test framework changes on `main` without using `main` as the user update channel.
2. Update the semantic framework version consistently in `brain.config.json` and `update-manifest.json`.
3. Confirm every new framework file is declared and company-owned files remain protected.
4. Insert and validate the authentic official general AI Tooltip skills; never release marker files as if they were skills.
5. Run `python3 11-SYSTEM/scripts/validate_brain.py` and the four-perspective release tests.
6. Review privacy, license, migration, and update behavior. Obtain professional license review before commercial/public launch.
7. Publish a non-draft, non-prerelease GitHub release with a semantic tag such as `v1.0.0` and useful release notes.
8. From a clean ZIP installation of the preceding stable version, test both update checking and an approved update to the new release.

Development path: `main → validation/testing → stable GitHub release → explicit user update`.
