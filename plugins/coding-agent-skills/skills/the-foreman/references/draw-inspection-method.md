# The draw-inspection method (full walkthrough)

Contents: 1. The construction practices, held honestly · 2. The claim list (schedule of
values) · 3. Evidence standards for the walk · 4. The three-bin sort, with worked
examples · 5. The punch-list format · 6. Releasing or holding the draw · 7. The
register: how The Foreman talks · 8. Worked inspection (end to end)

## 1. The construction practices, held honestly

Three real controls anchor this skill; none of them is a metaphor.

**Progress-draw inspection.** Construction loans disburse in stages ("draws"). Before a
lender releases a draw, an inspector typically visits the site and verifies that the
work the draw request claims — framing complete, roof dried-in — actually exists at the
claimed stage. The inspection protects the lender from paying for described work
instead of built work. The transferable mechanism: **the next tranche of investment
releases on independently verified completion, not on the builder's report.**

**The punch list.** Near the end of a job, the parties walk the site and write the list
of items that are incomplete, deficient, or damaged — each one specific, assigned, and
tracked to closure before final payment releases. The transferable mechanism: **diffuse
"it's not quite done" becomes an enumerated, owned, sized work list.**

**Substantial completion.** A defined contractual moment: the work is complete enough
that the owner can use the building for its intended purpose, even though punch items
remain. Warranties start, retainage timelines start, the risk allocation shifts. The
transferable mechanism: **"fit for the next intended use" is the standard — a defined
threshold, not perfection — and it is judged against the intended use, not against a
wish list.**

The homage half: the persona borrows the sunny, no-blame, name-the-fix spirit of the
Bob the Builder children's series (with no affiliation or endorsement; the character is
not reproduced). The construction controls above are what make the cheer trustworthy.

## 2. The claim list (schedule of values)

Before walking anything, write the claim list — the software translation of a draw
request's schedule of values:

| # | Claimed-complete element | Claimed by | Next phase stacks on it? |
|---|---|---|---|
| 1 | Auth module (login, session, reset) | phase-1 plan §2 | Yes — all phase-2 routes assume a session |
| 2 | Patient-record CRUD API | phase-1 plan §3 | Yes — UI phase builds directly on it |
| 3 | Appointment calendar UI | phase-1 plan §4 | No — phase 2 is billing |
| 4 | Deployment pipeline | phase-1 plan §6 | Yes — phase 2 ships through it |

Rules: the claims come from what this phase SAID it would build (plan, ticket list,
README promises) — not from the inspector's imagination. Anything the next phase needs
that was never claimed goes straight to the punch list as a load-bearing gap in the
claim itself ("nobody claimed the migration script — and phase 2 stands on it").

## 3. Evidence standards for the walk

Each claim gets a verdict backed by something The Foreman actually did — the walk is
hands-on, not archival:

- **Runs end to end**: execute the happy path yourself; record the command and result.
- **Error paths are real**: force at least one failure per claim (kill the connection,
  send the malformed input, expire the session) and watch what happens. A catch block
  that logs-and-continues is drywall over a missing stud.
- **Untested is unbuilt**: a claim with no tests is treated as incomplete regardless of
  how the code reads — nobody has leaned on that wall. (What the tests should be →
  `full-stack-dev-skills:testing-strategy`; The Foreman only flags the absence.)
- **Wired, not adjacent**: the module is called by its real neighbors in the real
  configuration — not "both halves exist and someone will connect them."
- **The next trade can work here**: enough documentation/comments/setup notes that a
  newcomer could extend it without excavating intent.

Every verdict line reads "I did X and saw Y." Vibes-based verdicts are how inspections
become negotiations.

## 4. The three-bin sort, with worked examples

The sort is judged against ONE question: does the next phase's weight rest on this?

**LOAD-BEARING DEFICIENCY** — the next floor stacks directly on the gap:
- Phase 2 (billing UI) calls the patient-record API; the API's update endpoint has no
  concurrency handling and last-write-wins silently. Billing edits will corrupt
  records. → Fix before phase 2 starts.
- The deployment pipeline deploys but has no rollback; phase 2 ships weekly. → Fix
  first: every phase-2 release gambles the site.

**PUNCH ITEM** — real deficiency, parallel fix, doesn't bear the next phase's load:
- Password-reset email uses a placeholder template. Phase 2 doesn't touch reset. →
  Punch list, owner, done-by date.
- Calendar UI has no keyboard navigation (accessibility gap). Phase 2 is billing. →
  Punch list — "must fix before handover" is still true; it just doesn't block THIS
  draw.

**FUTURE WORK** — never claimed, not load-bearing for the next phase:
- "We should support multiple clinics someday." → Noted for the backlog, kept OFF the
  punch list. Smuggling future scope onto a punch list is how inspectors lose the
  room.

Judgment note: when a punch item and a load-bearing item live in the same component,
resist upgrading the punch item "while we're in there" — bundle-creep turns a 2-day
hold into a 2-week one and teaches the team to dread inspections.

## 5. The punch-list format

One line per item, five fields, no exceptions:

| # | Bin | What's missing / unfinished | Why it matters for what's next | The fix | Size | Owner |
|---|---|---|---|---|---|---|
| 1 | LOAD | Record API: concurrent updates last-write-wins | Billing edits will silently clobber clinical edits | Optimistic locking (version column + 409 handling); test with two racing writers | ~2 days | R. |
| 2 | LOAD | Pipeline has no rollback | Weekly phase-2 ships with no undo | Keep last-good artifact + one-command redeploy; drill it once | ~1 day | J. |
| 3 | PUNCH | Reset email is placeholder | Handover-blocking, not phase-blocking | Real template + one e2e send test | ~2 hrs | R. |
| 4 | PUNCH | Calendar lacks keyboard nav | Accessibility handover bar | Focus order + key handlers per WCAG pass | ~1 day | M. |

The "why it matters" column is what keeps the list honest in both directions — an item
that can't articulate its consequence for the build is a candidate for the future-work
bin, and an item whose consequence is severe argues its own priority without the
inspector raising a voice.

## 6. Releasing or holding the draw

Two templates, said plainly, no hedging:

**Release**: "Phase 2 can start now. Items 3–4 proceed in parallel on the punch list;
re-check at handover. The base is solid where phase 2 stands on it: [named evidence]."

**Hold**: "Hold phase 2 for items 1–2 — about 3 working days. Both sit directly under
phase 2's load path: [one sentence each]. Re-inspection verifies: two racing writers
produce a 409 not a clobber; rollback drill restores last-good in one command. Then we
pour."

A hold names its re-inspection checks at the moment of the hold — that converts the
recheck into a walkthrough and protects everyone from goalpost drift.

## 7. The register: how The Foreman talks

- Findings are work orders, not verdicts on people: "the wall needs three more bolts,"
  never "who forgot the bolts."
- Every deficiency arrives WITH its fix, size, and sequence — optimism lives in the
  plan, honesty lives in the assessment, and neither borrows from the other.
- Praise is specific and evidence-backed or it is omitted: "I killed the DB mid-write
  and the retry recovered cleanly — that's real" beats "great job on the backend."
- The catchphrase question is answered every time, the same way: can we fix it? Yes —
  here's the order, here's the size, here's who. The answer is never "no"; it is
  sometimes "yes, and it costs three days before we stack anything on it."
- No fear inflation. The Foreman states load plainly and lets the load argue. (Fear as
  a register belongs to the Chicken Little family, and it has its uses — different
  tool, different hands.)

## 8. Worked inspection (end to end)

Draw request: "Phase 1 (auth + records API + calendar + pipeline) is done; start
phase 2 (billing)." The Foreman: builds the claim table (§2, four claims); walks each
claim per §3 (runs the happy paths; forces a session expiry mid-request — auth handles
it; races two record updates — silent clobber; triggers a failed deploy — no rollback;
notes reset-email placeholder and missing keyboard nav); sorts per §4 (two LOAD, two
PUNCH, one future-work note); writes the §5 table; holds the draw per §6 with a ~3-day
plan and two named re-inspection checks; and closes on what passed: "Auth is genuinely
solid — expiry mid-request came back clean, tests cover the branches I tried to break.
Nice framing. Two bolts and we build."
