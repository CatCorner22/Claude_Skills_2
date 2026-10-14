# Your environment — mscd-contract-drafting (template)

Fill this in for your current role, and keep the filled copy outside the plugin at
`.claude/skills-env/mscd-contract-drafting.private.md` (git-ignored by the `*.private.*` pattern —
confirm your own repository ignores it too). Nothing identifying a client, a deal or a counterparty
belongs in the shipped file.

## House style decisions
- Verb of obligation: `shall` (MSCD default) or `must` — one choice, held for the whole instrument.
  Pass it to the linter as `--house-style`.
- Defined terms: quotation marks and bold where defined; plain capitals thereafter. Definitions
  section at the front / at the back / integrated (say which, and when).
- Numbering: articles 1, 2 …; sections 1.1; (a), (b); (i), (ii). Automatic numbering on.
- Numbers: digits except whole numbers one through ten in prose; digits always for money,
  percentages, times, lists.
- Dates and times: *October 1, 2026*; *11:59 p.m. Eastern Time*.
- Pronouns: repeat the defined term; *it* for entities.

## Prescribed-wording clauses (always flag, never edit)
List the clauses in your forms that a rule requires verbatim or conspicuously (warranty disclaimers
under UCC § 2-316, statutory notices, consumer or employment notices, safe-harbour text), with the
instrument that requires them.

## Risk-allocation positions the firm has taken
Where the firm has a settled view (for example, keep *defend* always; use *indemnify and hold
harmless* in jurisdictions that have distinguished them), record it so the note can say "house
position" rather than re-arguing it.

## Known terms
Terms defined in master agreements or standard schedules that a reviewed document may use without
defining. One per line in a file passed to the linter as `--known-terms`.

## Templates in force
Which forms are live (edits there are flags), who owns each, and the governing law each assumes.

## Deliverable preferences
Tracked changes or the three-column table; whether the cover note goes in the email body or as a
first page; who signs off on flags.
