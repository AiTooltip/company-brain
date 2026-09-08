# AI Tooltip Company Brain

A local, portable source of truth that gives a company and its AI tools shared context, history, goals, approvals, research, references, assets, and project memory.

The Company Brain is deliberately human-governed. AI may organize evidence, ask questions, propose options, execute approved work, and maintain records. It must not silently turn a suggestion, inference, or imported document into a company decision.

## Start in five steps

1. Download or clone this entire repository.
2. Put existing documents, exports, assets, or older AI Tooltip folders in `00-INBOX` (or `00-MIGRATE-OLD-SETUP` for an older setup).
3. Open the whole folder in Codex Desktop.
4. Say: **Set up my company brain**
5. Review and approve the important conclusions Codex proposes.

Codex will inspect the material first, ask only for information it cannot reliably find, and keep uncertain claims visibly marked until a person confirms them.

> **Keep company information private.** This starter is public, but a filled Company Brain may contain confidential material. Keep your working copy local or use a private repository unless your company has explicitly approved every item for public release.

Read [START-HERE.md](START-HERE.md) for the non-technical guide. The operating rules AI tools must follow are in [AGENTS.md](AGENTS.md).

## The map

| Folder | Purpose |
| --- | --- |
| `00-INBOX` | Temporary landing zone for unsorted material |
| `00-MIGRATE-OLD-SETUP` | Safe intake for AI-DESIGN-SKILLS and codex-design-studio |
| `01-COMPANY` | Canonical company profile, goals, history, team, decisions, activity |
| `02-DEPARTMENTS` | Department context and working guidance |
| `03-BRAND` | Approved brand facts, voice, visual guidance, and guidelines |
| `04-PRODUCTS` | One durable record per product or service |
| `05-PROJECTS` | Time-bounded initiatives with owners, status, and outcomes |
| `06-RESEARCH` | Questions, evidence, findings, and research status |
| `07-CONTENT` | Content plans, drafts, and approved content records |
| `08-REFERENCES` | External or internal reference material and source notes |
| `09-ASSETS` | Source, working, and approved reusable assets |
| `10-OUTPUTS` | Deliverables produced by projects and workflows |
| `11-SYSTEM` | Framework workflows, templates, schemas, scripts, and reviews |

## A few important rules

- Put raw material in the inbox; do not treat it as approved truth yet.
- Record consequential, approved decisions in `01-COMPANY/decisions`.
- Record meaningful activity, not chat transcripts or every AI action.
- Keep shared team profiles in `01-COMPANY/team`.
- Keep the current computer's user identity in `.company-brain/current-user.md`; it is intentionally not committed.
- Never store passwords, API keys, private keys, session cookies, or access tokens here, even in a private copy.

## Updates

The official framework source is [AI-Tooltip/company-brain](https://github.com/AI-Tooltip/company-brain). In Codex Desktop, say **Check for AI Tooltip updates**. The check is read-only and reports framework differences; it does not overwrite company information.

## License

Add the license selected by the repository owner before public distribution if one has not already been added.
