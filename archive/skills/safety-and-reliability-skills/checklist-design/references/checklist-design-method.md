# Checklist design method (reference)

## Contents
- Killer-item selection heuristics
- Format choice: read-do vs. do-confirm
- Pause-point identification
- Drafting rules
- Field-test protocol
- Failure catalog — why checklists fail
- Evidence base (with provenance)
- Worked sketches: treasury and dental

## Killer-item selection heuristics
A step earns a line on the card only if it passes **both** gates:

1. **Severity gate** — missing it causes serious, hard-to-reverse harm (money leaves, patient
   harmed, data lost, period closed wrong), not mere inconvenience.
2. **Omission gate** — it is *actually skipped in practice*: it has been missed before, or it is the
   kind of step that gets dropped under load (interruptions, handoffs, end-of-shift, "just this
   once" pressure).

Steps that pass severity but not omission (people never forget to log in) stay in training. Steps
that pass omission but not severity (a cosmetic field left blank) stay in the SOP. Sources for the
omission gate: incident and near-miss records, exception reports, audit findings, and asking the
crew "which step have you seen skipped?"

Working from a long SOP with a model: paste the full procedure and require (a) a shortlist of killer
candidates, (b) *a written rationale per cut* — why each dropped step fails a gate, and (c) flags
where the model is guessing about omission frequency. The owner then challenges every rationale
against real incident data. The model's cut is a draft, never the decision.

Target count: **5–9 items per pause point**. Below 5, ask whether the pause point is worth a card;
above 9, the card is becoming the SOP again — recut. The count is per card, not per process: the
19-item WHO Surgical Safety Checklist is three cards at three pause points (sign-in, time-out,
sign-out), each inside this range. If your list will not fit in 9, look for a second pause point
rather than a longer card.

## Format choice: read-do vs. do-confirm

| Dimension | Read-do | Do-confirm |
|---|---|---|
| How it runs | Read an item, do it, next item | Work from memory/flow, then pause and verify |
| Best for | Infrequent, novel, or interruptible tasks; sequence-critical setup | Skilled crews on routine, flow-critical work |
| Failure it guards | Wrong order, dropped setup step | Killer step silently skipped in a familiar flow |
| Feel to experts | Can feel insulting if overused | Respects expertise; interrupts only once |
| Examples | Aircraft engine start; sterilizer load/cycle; new-system cutover | Pre-incision time-out; wire release "before send" card; pre-close lock |

Rule of thumb: if the task is done rarely or by rotating staff → read-do. If the task is done daily
by the same skilled people and the risk is a skipped verification → do-confirm at the pause point.

## Pause-point identification
A pause point must be a moment where the team **already stops or can be made to stop naturally**:
- a control transfer (handing the patient over, submitting the batch for approval),
- an irreversibility threshold (before incision, before pressing "release payments"),
- a physical or system gate (door of the operatory, the release screen itself).

Tests for a candidate pause point: Does everyone needed for the check already gather there? Can the
action physically wait 60 seconds there without cost? Is it *before* the harm becomes irreversible?
If no natural pause exists, create a hard gate (the system will not release without the card) —
otherwise the checklist will be run after the fact, as paperwork.

## Drafting rules
- One verifiable action per line, imperative voice: "Confirm beneficiary against the vendor master."
- Precise nouns — name the screen, the file, the threshold. No "consider", no "as appropriate".
- The expected response is binary: checked / challenged. If a line needs a paragraph, it is SOP
  material, not a checklist line.
- One page, readable at arm's length, no branching. Branches mean two checklists.
- Title = the pause point ("BEFORE RELEASE"), not the department.

## Field-test protocol
1. Run the card live with the crew that will use it, on real work, at the real pause point.
2. Observe, don't help: time the run (target under ~90 seconds), note skipped lines, hesitations,
   items read but not actually verified, and any line that triggers discussion (ambiguity signal).
3. Debrief the crew: which line felt pointless? what almost-miss does the card not catch?
4. Revise wording, order, and count; re-test. Two to three cycles is normal.
5. Only then roll out — with a named caller, a rehearsal, and a skip-data review cadence.

## Failure catalog — why checklists fail
- **Too long** — the card restates the SOP; crews sample it or skip it. Recut to killer items.
- **No pause point** — run from memory afterward, as documentation. Anchor or gate it.
- **Never trialed** — ambiguous lines and wrong order surface in production instead of the pilot.
- **Serves auditors, not the crew** — items chosen for evidence value, not harm prevention; the crew
  learns the card is theater and treats it accordingly.
- **Mandate without ritual** — the artifact ships, the behavior doesn't; see Ontario below. The
  enacted team ritual — pause together, speak aloud, license to challenge — *is* the method.
- **No owner** — the process drifts, the card doesn't, credibility dies.

## Evidence base (with provenance)
- **B-17 origin** [snippet-only]: Boeing's Model 299 crashed on its 1935 Army evaluation flight with
  the elevator/rudder gust locks still engaged. Two of the five aboard died — the Army's chief of
  flight testing, Maj. Ployer Hill, and, of his injuries, Boeing's chief test pilot Leslie Tower;
  three survived. Judged "too much airplane for one man to fly," the type was nearly cancelled; the
  surviving test pilots' remedy was the first pre-flight checklist, and the aircraft went on to fly
  safely at scale as the B-17.
- **WHO surgical checklist — Haynes et al., NEJM 2009** [snippet-only]: prospective study in eight
  hospitals across eight cities, ~7,700 patients; after introducing the 19-item WHO Surgical Safety
  Checklist, mortality fell 1.5% → 0.8% and inpatient complications 11.0% → 7.0%.
- **Ontario mandated rollout — Urbach et al., NEJM 2014** [snippet-only]: after Ontario mandated
  surgical safety checklists, comparison of ~100 (101) hospitals before/after found **no significant
  change** in operative mortality or complications. The standing interpretation: mandated adoption
  produced the artifact without the team ritual and local ownership present in the 2009 study —
  the counter-case proving the ritual is the method.
- **Human-factors basis** [snippet-only]: Degani & Wiener's NASA-sponsored work on flight-deck
  checklists (c. 1990) established the design variables used here — checklist as memory *and* team
  device, format (read-do vs. do-confirm), pacing, and the hazards of checklist-as-ceremony. Boorman
  (Boeing) and Gawande (*The Checklist Manifesto*, 2009) carried the design discipline to medicine.

Provenance note: items marked [snippet-only] were verified against abstracts, summaries, or
secondary accounts — not the full primary texts. Treat exact figures as reported values to re-verify
before quoting in anything formal.

## Worked sketches: treasury and dental
**Wire release — do-confirm card at "before send":** killer candidates: beneficiary confirmed
against vendor master (not against the email); callback done to a number from the master file, not
from the instruction; amount and currency match the approved instruction; dual approval present in
the bank platform; no changes to bank details in the last N days without re-verification. Caller:
the releasing approver. Pause point: the release screen, before the final click.

**Instrument sterilization — read-do card:** rotating staff, sequence-critical, interruptible —
read-do. Killer candidates come from the omission gate on the practice's own near-miss log (cycle
not completed, indicator not checked, load released early). Pause point: before the cassette
returns to the operatory.
