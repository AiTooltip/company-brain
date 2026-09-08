# Collaboration

Choose the simplest workflow that fits the people using the Company Brain.

## Solo

`Download ZIP → keep locally → open the whole folder with Codex Desktop`

1. On the official repository, choose **Code → Download ZIP**.
2. Unzip the download and keep the folder somewhere backed up.
3. Add existing material to `00-INBOX`.
4. Open the whole folder in Codex Desktop and say **Set up my company brain**.

No Git, GitHub account, GitHub CLI, or GitHub Desktop is required after download. The update checker also works without Git.

## Team

The public AI Tooltip repository is the **framework and update source**. Your actual Company Brain should be a **private repository** unless your company explicitly approves public release of every file.

For non-technical teams, GitHub Desktop is the recommended interface:

1. One responsible team member creates a new private GitHub repository for the actual Company Brain and adds the starter files.
2. Invite only appropriate team members.
3. Each person installs GitHub Desktop, accepts the invitation, and chooses **File → Clone repository** to download the private repository.
4. Each person configures their own ignored `.company-brain/current-user.md` once.

Normal team rhythm:

`Pull/sync → work → review meaningful changes → commit → push`

- Pull before beginning work.
- Review canonical knowledge, decisions, and generated assets before committing.
- Use a clear commit summary that describes the meaningful change.
- Push so teammates receive the approved shared memory.
- Pull again before beginning another significant block of work.

## Conflicts

If Git reports a meaningful conflict involving canonical company knowledge, an approved decision, goal, team authority, brand rule, product truth, or company-owned skill, AI must not silently choose a version.

Show the human:

- both versions and their sources;
- the exact difference;
- likely chronology when it is supported;
- affected records and implications.

A human with appropriate authority must resolve the conflict. Preserve both versions until that happens.

## Important warning

**Do not use a public fork of AI Tooltip Company Brain for confidential company data.** To share the framework itself, link people to `https://github.com/aitooltip/company-brain`. Do not mirror or redistribute it; see `LICENSE.md`.
