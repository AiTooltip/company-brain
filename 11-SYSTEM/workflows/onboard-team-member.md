# Onboard a Team Member

**Trigger:** `Onboard a team member`

**Outcome:** add a useful shared work profile and help the person configure local identity without storing sensitive HR or authentication data.

## Procedure

1. Read `11-SYSTEM/OPERATING-SYSTEM.md`, company governance context, and existing team profiles.
2. Gather only useful work information: name, role, responsibilities, departments, current work, collaboration preferences, appropriate work contact, and explicitly established approval authority.
3. Do not infer decision authority from title. Ask the responsible human to confirm any consequential authority statement.
4. Create `01-COMPANY/team/<stable-person-name>.md` from the team-member template.
5. Link the profile from relevant department, product, and project records when useful.
6. Explain local setup: on the new member's computer, copy `.company-brain/current-user.example.md` to `.company-brain/current-user.md`, fill in their name and shared profile path, and leave it uncommitted.
7. If this computer belongs to the new member and they explicitly identify themselves, create/update the ignored local file. Otherwise do not change the current user's identity.
8. Log onboarding only if joining or a responsibility/authority change is meaningful company activity.

Once a valid local identity points to an active shared profile, use it in later conversations instead of repeatedly asking the person to introduce themselves. Reconfirm only when the file is missing, invalid, or the user says the computer/user changed.

Never add passwords, tokens, private identifiers, compensation, medical information, background-check material, or other unnecessary HR data.
