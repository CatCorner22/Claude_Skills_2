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

## Ownership and review cadence (the time-triggered half)
Docs-as-code only catches drift in pages a change already touches. Everything whose subject can move
without a commit here needs an owner and a clock.
- Where the owner and last-verified stamp live: <page frontmatter, a header line, an index table>
- Default cadences by form: <tutorial: each release on the path + quarterly | how-to/run sheet:
  verified on each use | reference/data dictionary: quarterly + on upstream schema change |
  explanation/method note: annual + on material change>
- Pages exempt from freshness review: <ADRs — always; anything else, with the reason>
- Is the cadence checked mechanically? <does the build warn on a page past its review date?>
- Retirement path for a stale, unowned page: <who decides delete vs deprecate-with-pointer, and
  where deprecated pages go>
- Upstream sources whose changes invalidate our docs without touching this repo: <schemas, feeds,
  vendor tools> — and how you learn they changed.

## Recurring document types in this role
- <e.g., quarterly method note — explanation; owner <name>; last verified <date>; annual cadence>
- <e.g., run sheet for the monthly extract — how-to; trigger event; verified on each use by the
  operator on rotation>
- <e.g., data dictionary — reference; owner <name>; verified by diffing against the schema>
- <e.g., decision memos — ADR-analogue; where filed; freshness-exempt>

## Audiences
- <audience 1 — what they can be assumed to know; which form they usually need>
- <audience 2 — …>
