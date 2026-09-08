# Record an Approved Decision

**Trigger:** `Record this approved decision`

**Outcome:** preserve a decision a human has explicitly made, with provenance and implications.

## Approval gate

Before creating the record, establish:

- the exact decision;
- the named human approver;
- the basis for that person's authority over this decision's scope;
- that the person explicitly approved it rather than discussed, leaned toward, or asked AI to recommend it;
- the decision date or an honest `unknown` if historical;
- the scope and important implications.

If approval is ambiguous, do not use the approved-decision template. Keep a `proposed` note in the relevant project and ask the human to approve or correct the wording.

## Procedure

1. Check existing decisions for duplicates, conflicts, and records this decision supersedes.
2. Draft the decision in direct, precise language. Separate the approver's stated reasoning from AI interpretation.
3. Show the exact decision statement and any proposed supersession when those were not already explicit.
4. Create `01-COMPANY/decisions/YYYY-MM-DD-<decision-name>.md` from the decision template only after the gate is met. If a verified historical decision has no recoverable date, use `undated-<decision-name>.md` and keep `decision_date: unknown`.
5. Update the company-owned decision index in `01-COMPANY/decisions/INDEX.md`.
6. Link the decision from affected company, brand, product, department, project, or research records; update their status only within what was approved.
7. Mark replaced decisions or guidance `superseded` without erasing their history.
8. Add one concise meaningful activity entry linking to the decision.
9. Report implications and unresolved follow-up; do not execute externally consequential follow-up unless it was also authorized.
