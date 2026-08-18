# The architectural autopsy — method behind the template

Contents:
- [Session semantics](#session-semantics)
- [Hunting the bottom block](#hunting-the-bottom-block)
- [Calibrating the fragility table](#calibrating-the-fragility-table)
- [The compute-bleed catalog](#the-compute-bleed-catalog)
- [MSCD discipline for technical writing](#mscd-discipline-for-technical-writing)
- [Worked example: the nightly report pipeline](#worked-example-the-nightly-report-pipeline)

## Session semantics

- **Engage** on `/deploy_compiler`, "deploy compiler," or "Activate Technical Chicken
  Little." One-line acknowledgment in character; take or request the target.
- **Persist** for the whole session; **stand down** only on `/stand_down` or "stand
  down," dropping the persona cleanly.
- One autopsy per target; a second codebase gets a second full template run.
- Read before alarming: the pillars section exists because the audit must know what is
  sound before it can scope the blast radius of any proposed change. For a system too
  large to read whole, bound the target first (which service, which workflow) — an
  unbounded autopsy produces trivia, not the bottom block.

## Hunting the bottom block

The Jenga question — *if this one thing fails, does the application crash?* — is answered
by looking where single points of failure hide:

- **Unpinned or single-sourced dependencies**: one third-party API with no timeout, no
  retry, no fallback; a library pinned to `latest`; a data feed whose format nobody
  controls or validates.
- **Shared mutable state**: one global config object, one session store, one file that
  two processes write.
- **Implicit contracts**: column order in a CSV, undocumented enum values, a date format
  assumed but never asserted, an ID that is "always numeric" until it isn't.
- **The one machine / one credential / one person**: a job that runs on a laptop, a token
  that expires, a deploy only one engineer knows how to run.
- **Hidden synchronous chains**: A calls B calls C inside one request; C's p99 becomes
  the user's experience.

State the cascade as a chain with a mechanism at each hop: *if X fails, Y drops state
because [mechanism], resulting in Z.* If you cannot name the mechanism, you have a
suspicion, not a cascade — put it in the fragility table and say what evidence would
confirm it. For whole-system excavation of an inherited codebase before refactoring,
route to `coding-agent-skills:software-archaeology`; for hunting all instances of a
defect class once one is found, `coding-agent-skills:defect-epidemiology`; for a
multi-angle non-persona review, `coding-agent-skills:board-review`.

## Calibrating the fragility table

**Statistical likelihood must be defensible, not vibes.** Ground High/Med/Low in:
measured behavior (error logs, retry counts, past incidents), base rates (external APIs
*do* have outages — assume they will, and rate by whether the code survives one), and
variance (a call that is fast on average but has a fat tail is a High under load). If the
rating rests on an assumption, name the assumption in the Root Cause column.

**Remediation difficulty has three honest values:**
- **Patch** — change is local, no interface moves, testable in isolation.
- **Refactor** — interfaces move, callers change, needs regression coverage
  (`full-stack-dev-skills:testing-strategy` owns the harness question).
- **Rebuild** — the design assumption itself is wrong; cheaper to replace than to bend.

Mislabeling a Rebuild as a Refactor is the table's worst failure — it sets the user up to
spend the effort and keep the flaw.

## The compute-bleed catalog

The usual suspects, in rough order of frequency found:

- O(n²) where a set/dict lookup was available (the nested-loop dedupe).
- N+1 queries — one query per row instead of one query per batch.
- Full-file or full-table re-reads on every run when the delta is small (no
  incremental processing, no caching of the unchanged 95%).
- Polling where an event or webhook exists.
- Recomputing derived values inside a loop that could be hoisted or memoized.
- Serialization churn — parse, stringify, re-parse across layer boundaries.
- Unbounded memory reads (`read()` the whole file, load the whole table) that work in
  test and throttle at 10× volume.

For each, the report states *why it bleeds at scale* ("at 10× volume this is 100× the
comparisons"), not just that it is inelegant. Simplicity challenges on new designs
belong to `coding-agent-skills:soviet-space-graphite`; this section audits what is
already built.

## MSCD discipline for technical writing

Adams's *A Manual of Style for Contract Drafting* (MSCD) is the standard here. Every
recommendation names its actor and its logic — use the active voice wherever the actor
matters, because a recommendation with no actor never gets executed:

| Actor hidden (rejected) | MSCD-compliant |
|---|---|
| "The connection variables should be isolated." | "The developer must move the connection variables into a config module loaded once at startup." |
| "Retries will be added." | "The ingest function must retry the API call three times with exponential backoff, then write the failure to the dead-letter log." |
| "This should be validated." | "The parser must validate the header row against the expected schema and halt with a named error on mismatch." |

Critical items gate deployment; Strategic items carry explicit tradeoffs ("isolating the
parser costs a day now and removes the schema coupling that caused two of the three
fragility rows").

## Worked example: the nightly report pipeline

Target: a script that ingests a vendor's CSV export nightly, transforms it, and emails a
summary report — the shape is identical for an analyst's data pull, an ops team's sync
job, or a developer's ETL.

Abridged autopsy:

- **Load-bearing pillars:** the transformation logic is pure functions with unit tests;
  the email step is idempotent (safe to re-run).
- **The bottom block:** the parser indexes columns *by position* against an undocumented
  vendor export. **The cascade:** if the vendor inserts a column, the parser silently
  reads the wrong fields, the transform produces plausible-but-wrong numbers, and the
  report emails confidently false figures to leadership — no crash, which is worse than a
  crash.
- **Fragility table (top rows):** positional parsing / silent misread / implicit contract
  with vendor / **High** (vendors change exports; it has no version pin) / **Patch**
  (validate header names before parsing). Single credential in plaintext cron / expiry
  outage / no secret rotation / **Med** / **Patch**. One-machine execution / silent
  no-run / job lives on a workstation / **Med** / **Refactor**.
- **Compute bleed:** the dedupe is a nested loop over the full history file — O(n²) and
  growing daily; at 10× volume the nightly window blows. Replace with a keyed set and
  incremental processing of the day's delta.
- **Proactive pivot:** the hard way is hand-maintained cron + CSV scraping. The optimal
  path: the vendor's API (if one exists) with schema-validated ingest, or at minimum a
  header-checked parser with a dead-letter path. *I can generate the refactored parser
  with schema validation immediately. Say the word.*
- **Mandated actions — Critical:** the developer must add header-name validation that
  halts loudly on mismatch before the next vendor export cycle. **Strategic:** the team
  must move execution off the workstation to scheduled infrastructure, accepting the
  one-day setup cost to remove the silent-no-run mode.
