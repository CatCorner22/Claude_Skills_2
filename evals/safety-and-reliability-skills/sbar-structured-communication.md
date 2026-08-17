# Evals — safety-and-reliability-skills:sbar-structured-communication

## 1. Positive trigger (should load the skill)
> "A vendor payment in today's 2 PM run has new bank details we couldn't verify by callback —
> it smells like email compromise. I need to escalate this to the treasurer right now, and I'm
> also the junior person here: give me an SBAR and the graded-assertiveness wording to use if
> the senior approver waves me off."

Expected: skill loads; produces a four-part SBAR with a one-sentence Situation, pertinent-only
Background, a committed Assessment, and a Recommendation carrying an explicit action and
deadline; drafts a PACE ladder (Probe → Alert → Challenge → Emergency) phrased for the junior
analyst → senior approver relationship, with the note that an Emergency step must be acted on;
offers to roleplay the conversation; frames the analyst's challenge as the human barrier on
the business-email-compromise pathway (cross-referencing
`safety-and-reliability-skills:bowtie-barrier-analysis` where available).

## 2. Near-miss (should NOT load this skill)
> "The nightly data-file handoff from the vendor's SFTP to our warehouse loader failed again
> last night — can you troubleshoot why the load keeps erroring out?"

Expected: a technical file-transfer/load failure — data-pipeline troubleshooting, not
person-to-person communication — so this skill should NOT load. Bare "handoff" appears in many technical contexts across this library and must
never trigger alone; if this skill loads here, its trigger surface has grown past the
structured-communication vocabulary (SBAR, structured handoff, coverage notes, read-back).

## 2b. Near-miss (register-vs-protocol guard)
> "Here's my draft email to the office manager about next month's schedule change —
> tighten it up and make it clearer and more professional."

Expected: prose improvement is a writing-register task → `writing-skills:adams-smart-brevity`.
This skill is a communication *protocol* (what must be said, in what order, with what
confirmation), not a style editor. If it loads on generic "make my message better" asks,
narrow the description. (A request to *escalate a problem* to the office manager, by contrast,
is a legitimate SBAR use.)

## 3. Quality rubric
A good response:
- **Does the task:** picks the right protocol for the moment (SBAR / I-PASS / closed loop /
  PACE — one moment, one protocol); every SBAR ends in a recommendation with a deadline; every
  handoff includes if-then contingencies and ends at the receiver's synthesis/read-back, not
  the sender's monologue; closed loops run three turns with critical values repeated verbatim;
  PACE ladders are drafted for the specific relationship (analyst → approver, nurse →
  attending) and climbed in order.
- **Teaches:** explains the two failure modes the protocols attack — information loss at
  transitions and deference under authority gradients (the United 173 lesson) — and why
  structure, not heroism, is the countermeasure; cites the outcome evidence (I-PASS: errors
  −23%, preventable adverse events −30%, no workflow cost; VA team training dose-response).
- **Stays honest:** marks the evidence base as compiled from snippets [snippet-only]; states
  that the protocol works only enacted — the read-back and the decision are human acts, and a
  pasted template nobody speaks is scenery; never abbreviates crew resource management to its
  three-letter form (reserved for customer relationship management in this library).
