# The Pencil Pass and the Graphite Test — expanded doctrine

Contents: §1 The true history · §2 The simplification ladder · §3 The Graphite Test
checklist · §4 Better-faster-cheaper triage rules · §5 Worked verdicts · §6 Voice card

## §1 The true history (the founding legend, debunked on purpose)

The myth: NASA spent millions developing a pen that writes in zero gravity; the Soviets
used a pencil. The record [snippet-only]: Paul Fisher developed the pressurized-cartridge
pen privately, at his own company's expense, and offered it to NASA; NASA had in fact
taken public criticism over the unit cost of earlier mechanical pencil procurement; and
pencils were a genuine hazard in a spacecraft — graphite dust is electrically conductive
and flammable, broken tips float, and an oxygen-rich cabin (after the Apollo 1 fire)
tolerates neither. After testing, NASA bought Fisher pens at a modest per-unit price —
and the Soviet program bought them too, for the same reasons. Both blades of the
doctrine come from this record:

- **The myth's merit**: the instinct it encodes — hunt the cheap, boring, already-
  existing solution before funding the impressive one — is correct and chronically
  underused. Most organizations really do build space pens.
- **The debunk's merit**: the armchair-simple candidate died on contact with the
  environment's hidden constraints, and the "expensive" solution existed for reasons
  invisible until examined. Simplicity is a search strategy, not a verdict.

## §2 The simplification ladder (run top to bottom; stop at the first survivor)

1. **Do nothing** — is the problem real, frequent, and costly enough to solve at all?
2. **Delete the requirement** — negotiate the spec, not the implementation.
3. **Use what already exists** — the report, query, tool, or SOP already in the building.
4. **Borrow** — another team's working solution, adopted not rebuilt.
5. **Buy, don't build** — when carry cost of building exceeds license cost of buying.
6. **The spreadsheet, not the app** — for low-volume, low-concurrency, trusted-user work.
7. **The cron job, not the platform** — one scheduled script before an orchestration layer.
8. **The checklist, not the workflow engine** — human process before automated process
   (`safety-and-reliability-skills:checklist-design` builds it properly).
9. **The phone call, not the integration** — for low-frequency cross-org exchanges.
10. **Build the simple version** — smallest thing that delivers the stated what
    (Gall's law: evolve it from something that works).

Price every rung twice: **build cost** (hours to done) and **carry cost** (maintenance,
training, failure modes, the 2 a.m. page). The ladder exists because carry cost is where
pens with heated ink hide their true price.

## §3 The Graphite Test checklist

For each surviving candidate, hunt the constraint that makes it dangerous HERE. A
candidate passes only when each line is checked against the real environment, not the
armchair:

| Constraint family | The question | Example graphite |
|---|---|---|
| Safety / compliance | What rule or regulator does this touch? | The "simple" shared spreadsheet holds PHI |
| Data integrity | What does this silently corrupt? | Excel float-coercion destroying `0006789599` join keys — the library's oldest wound |
| Security / privacy | Who can now see or change what? | The cron job running with a human's credentials |
| Scale / concurrency | What breaks at 10x, or with two users at once? | The spreadsheet's last-save-wins |
| Accessibility | Who is excluded by the shortcut? | The phone-call process failing deaf staff |
| Auditability | Can we prove what happened? | The manual step with no log |
| Chesterton's fence | Why does the complex thing exist? | The "pointless" approval step that exists because of a 2019 fraud |
| Reversibility | If wrong, how expensive is backing out? | The quick vendor whose export format locks you in |

Rules: a failed line kills the candidate or forces a mitigation whose cost is added to
the candidate's price; "we'll be careful" is not a mitigation; and the fence rule is
mandatory — the history of the existing solution is read before it is called waste.

## §4 Better-faster-cheaper triage rules

- Score survivors on the three axes against the STATED deliverable, not against
  ambitions the deliverable never claimed.
- Claim two; verify the third with a number (hours, dollars, lead-time days) or
  downgrade the claim. All three claimed = one of them is unexamined.
- Carry cost counts against "cheaper"; rework risk counts against "faster"; the
  Graphite mitigations count against both.
- Tie-breaker: the candidate easiest to REVERSE wins (cheap experiments beat committed
  bets — the library's project-command doctrine agrees).

## §5 Worked verdicts

**Case: "We need a dashboard for daily unreconciled items."**
- THE DELIVERABLE: the recon lead sees yesterday's unreconciled lines and aging each
  morning.
- THE PENCIL: rung 3 — the existing OTBI unreconciled report, subscribed... OTBI cannot
  schedule (library fact); rung 7 — a cron'd query emailing a table at 6 a.m.
- THE GRAPHITE: credentials for the cron (security line) → service account required,
  cost added; spreadsheet variant killed on float-coercion (data-integrity line —
  reference-bearing IDs).
- BETTER/FASTER/CHEAPER: claims faster (1 day vs 3 weeks) and cheaper (no new tooling);
  verifies better is NOT claimed — the dashboard's interactivity is surrendered and
  named as such.
- TRAJECTORY: kept — but the dashboard requirement is descoped to "morning visibility,"
  which the email satisfies.

**Case: "Replace the wire-approval step; it slows everything down."**
- THE PENCIL: rung 2 — delete the requirement.
- THE GRAPHITE: Chesterton's fence check finds the approval step IS a preventive barrier
  on the BEC bowtie (`safety-and-reliability-skills:bowtie-barrier-analysis`). Candidate
  killed. Verdict: the delay is real; attack it by exploiting the constraint (batch
  approval windows, `continuous-improvement-skills:theory-of-constraints`), never by
  removing the barrier.

## §6 Voice card

Dry, frugal, deadpan bureau humor: "In my bureau we had one wrench. It was a good
wrench." Pastiche stays affectionate and era-generic — no politics, no nationalism, no
mockery of any people; the Motherland it serves is the deliverable. The persona always
states plainly, once per engagement, that its founding legend is false and why that
falsity is the better teacher. Theatrics never outrank the verdict format.
