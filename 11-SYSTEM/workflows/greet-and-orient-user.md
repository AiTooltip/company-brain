# Greet and Orient the User

**Trigger:** a message whose primary intent is a greeting, such as `Hi`, `Hello`, `Hey`, `Good morning`, or a close equivalent.

**Outcome:** welcome the established local user by name, summarize what changed recently in the company, and offer a few relevant ways to continue.

## Procedure

1. Read `.company-brain/current-user.md`.
   - If it contains a real `name` and a valid `team_profile` path, use that name and read the linked profile for work context.
   - If it is missing, still contains placeholders, or points to a missing profile, do not guess. Give a friendly unpersonalized greeting, explain that local identity is not established, and ask for the person's name so setup can be completed once. Do not block the company update or suggestions if they can still be produced safely.
2. Build a quick company update from durable, dated records. Start with the newest entries in `01-COMPANY/activity/YYYY-MM.md`. Use up to three meaningful items, newest first.
   - If activity is empty or sparse, supplement it with newer dated approved decisions, active project milestones or status changes, and approved goals.
   - Prefer the date recorded inside a file. Never use filesystem modification time as proof that a company event occurred.
   - Label uncertainty or missing dates. Do not present proposals, drafts, inbox material, or unverified claims as completed company changes.
   - If there are no recorded recent changes, say so plainly and suggest logging meaningful milestones when they happen.
3. Suggest two to four useful next actions. Personalize and prioritize them using, in order:
   - the user's current projects/products, responsibilities, departments, and collaboration preferences from the linked team profile;
   - active company goals, projects, and approved decisions relevant to that work context;
   - visible workflow opportunities such as processing a non-empty inbox, starting or advancing a project, recording an approved decision, or researching an open question.
4. Keep the response compact and conversational. Use this shape unless the context calls for a smaller answer:
   - `Hi, [Name].`
   - `Recently: ...` with dated items.
   - `You could: ...` with actionable suggestions.
5. Do not claim that the user approved a decision or has authority merely because of their identity or role. Do not expose unnecessary personal data from the team profile.
6. Do not add an activity entry for the greeting, file reads, or the generated digest.

## Recency and relevance

“Recently” means the latest recorded meaningful events, not necessarily events within a fixed number of days. Always show each event's recorded date so the user can judge its age. Favor items connected to the user's responsibilities, but include a company-wide change when it is materially important.

This workflow is read-only unless the user chooses a suggested action or supplies the missing identity information needed for local setup.
