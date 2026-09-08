# Log Meaningful Activity

**Trigger:** `Log this as meaningful activity`

**Outcome:** preserve a concise, attributable company memory without recording every AI interaction.

## Meaningfulness test

Log an event when at least one is true:

- it changed durable company, product, brand, team, or project state;
- it represents an approval, launch, handoff, major milestone, pause, completion, or reversal;
- a future teammate would reasonably need to know what changed and where to find it;
- it created or approved a significant reusable asset or deliverable;
- a research result materially changed planned work.

Do not log routine reads, formatting, ordinary draft iterations, brainstorming not adopted, tool calls, chat transcripts, failed trivial attempts, or repeated status checks.

## Procedure

1. Check `.company-brain/current-user.md` and its linked team profile. If attribution matters and identity is missing, ask the user; never guess.
2. Locate the canonical record, decision, project, asset, or output that contains detail.
3. Open or create `01-COMPANY/activity/YYYY-MM.md` with a `# YYYY-MM` heading.
4. Append one entry using `11-SYSTEM/templates/activity-entry.md`. Keep it factual and link to the durable record.
5. Name the approver only when approval actually occurred. Identity does not imply approval.
6. Avoid personal or sensitive detail that is not needed for company memory.

If the event does not pass the meaningfulness test, explain that no permanent activity entry is needed and keep the repository unchanged.
