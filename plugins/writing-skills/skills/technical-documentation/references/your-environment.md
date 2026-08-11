# Your environment (sanitized template)

Wire in your real documentation terrain here so this skill produces docs that land in
the right place in the right house form. Keep this file **structural** — locations,
conventions, and document types, never client names, internal system details, or
anything sensitive. Real specifics go in `your-environment.private.md` — that suffix is
git-ignored and never committed.

## Where each document type lives
- README / project docs: <repo, docs site, wiki — and which renders where>
- ADRs: <path, e.g. docs/adr/; numbering convention; current highest number>
- Changelog: <path; whether releases are tagged; who cuts them>
- Procedure docs / run sheets: <where the team actually looks for them>
- Reference material (data dictionaries, API refs): <location; what is generated vs hand-written>

## Conventions
- Versioning scheme: <SemVer, date-based, or house scheme — and what counts as "breaking" here>
- Changelog categories in use: <the Keep-a-Changelog six, or your subset>
- Review path for doc changes: <same PR as code? separate approval?>

## Recurring document types in this role
- <e.g., quarterly method note — explanation; owner; audience>
- <e.g., run sheet for the monthly extract — how-to; trigger event>
- <e.g., decision memos — ADR-analogue; where filed>

## Audiences
- <audience 1 — what they can be assumed to know; which form they usually need>
- <audience 2 — …>
