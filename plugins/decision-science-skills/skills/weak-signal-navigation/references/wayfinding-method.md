# The wayfinding method

How to run a position from weak signals when the instruments are down: the mental
model, the cue inventory, the weighting, the fusion protocol, the commentary, and the
calibration check.

## Contents
1. [The etak mental model, honestly](#1-the-etak-mental-model-honestly)
2. [Cue inventory taxonomy (five classes)](#2-cue-inventory-taxonomy-five-classes)
3. [Independence and reliability weighting](#3-independence-and-reliability-weighting)
4. [The fusion protocol](#4-the-fusion-protocol)
5. [Worked example — project status, tracker stale two weeks](#5-worked-example--project-status-tracker-stale-two-weeks)
6. [The navigator's-commentary format](#6-the-navigators-commentary-format)
7. [Calibration follow-up](#7-calibration-follow-up)

## 1. The etak mental model, honestly

The documented facts, all [snippet-only] provenance (cross-checked across independent
sources, including archive.hokulea.com): in 1976 Hokule'a sailed Hawaii→Tahiti,
~2,500 nautical miles in 31 days, instrument-free, navigated by Mau Piailug of Satawal
(Weriyeng school, trained from age four); landfall at Mataiva was predicted a day out
by three navigators using different methods. David Lewis documented the technique in
*We, the Navigators*; Edwin Hutchins analyzed it as distributed cognition.

Etak itself is a moving-reference-island technique. The navigator pictures a real
island lying off to one side of the course — not the origin, not the destination — and
divides the voyage into segments by which star bearing that island currently sits
under. The canoe is imagined stationary; the reference island "moves" backward through
star positions as the voyage proceeds. Position is therefore never a coordinate; it is
a maintained relationship ("the reference island is now under that star, so we are in
the third etak of the voyage"), re-derived continuously from whatever the environment
offers:

- **Star bearings** at rising and setting (precise, but clouds kill them).
- **Swell trains** — long-period ocean swells hold direction for days and are read
  through the hull even in fog or at night.
- **Birds** — species that sleep ashore and fish at sea point toward land at dusk.
- **Clouds and light** — cloud stacks and lagoon glare over unseen islands.

No single cue is trusted; the fix is the agreement of many weak ones, and when a cue
class dies (overcast → no stars) the others still carry a usable position. That is
graceful degradation as a design property — the exact opposite of a single
authoritative instrument whose outage is total blindness.

Transfer rule: keep the mechanism, drop the romance. You are not "sailing"; you are
maintaining a belief about a state you cannot read directly, from many weak
independent observations, updated as each arrives, stated with its uncertainty.

## 2. Cue inventory taxonomy (five classes)

Work all five classes every time. The classes exist so the inventory is exhaustive —
under stress people grab the two loudest cues and stop.

| # | Cue class | What it is | Everyday examples (any role) |
|---|-----------|------------|------------------------------|
| 1 | Last known-good state | The most recent reading you trust, plus its age | The tracker as of two weeks ago; the last statement that reconciled; the last passing test run |
| 2 | Scheduled events that must have happened | Things that fire on a calendar or cron, whose occurrence you can verify indirectly | A weekly build that emails on completion; a standing meeting that wasn't cancelled; a filing deadline that passed without an extension request |
| 3 | Historical rhythms | What this process usually does over an interval like this one | Typical weekly throughput; how long this counterpart usually takes to respond; seasonal slowdowns |
| 4 | Side-channel indicators | Activity in adjacent systems that co-moves with the state you want | Commit or document-edit activity; message volume in the relevant channel; who has been asking questions; badge/login activity |
| 5 | Absence of expected noise | Complaints, escalations, or alarms that WOULD exist if things were bad — and don't | No client complaints; no incident pages; nobody asking for help; the other side not filing anything |

Class 5 discipline: absence of noise is evidence only where trouble would have been
loud. Before admitting a silence cue, name who would have made the noise and confirm
they had the means and motive to make it. Silence from someone who wouldn't have
spoken anyway is not a cue; it is wishful thinking.

## 3. Independence and reliability weighting

Two questions per cue, answered in writing:

**Independence — does this cue share a source with another cue?** Trace each cue to
its origin. Two status pages fed by the same collector are ONE cue. A manager's verbal
update sourced from the same stale tracker you already counted is ZERO new cues.
Group cues by shared source and count each group once; agreement across groups is what
raises confidence, agreement within a group raises nothing.

**Reliability — how often has this cue been wrong before?** Grade coarsely; three
levels are enough:

- **Strong** — direct, hard to fake by accident (a build artifact exists; money
  visibly left the account; a signed document arrived).
- **Moderate** — usually right, with known failure modes (calendar says the meeting
  happened — but it may have been held and useless).
- **Weak** — suggestive only (channel chatter volume; tone of the last message).

Weighting rule of thumb: a position may LEAN on strong cues, must be CHECKED against
moderate ones, and uses weak ones only in aggregate — many weak cues agreeing across
independent sources is a real signal; one weak cue alone is noise.

## 4. The fusion protocol

1. State the blind spot and the decision (from the skill's step 1) at the top of the
   worksheet. Everything below serves that decision.
2. List cues by class (all five), each with: source, independence group, reliability
   grade, and what it implies for the position.
3. Strike or merge cues that share an independence group. What remains is your
   effective cue set.
4. Draft the position as a range: "between X and Y, most likely Z." The band's width
   comes from how much the independent groups disagree; the center from where the
   strong cues point.
5. Attach a confidence word calibrated to the cue set: *high* only when several
   independent groups agree and at least one is strong; *moderate* when groups agree
   but none is strong; *low* when groups conflict or the set is thin. Say which.
   - **Grade the cue that sizes the quantity, not the cue set as a whole.** Broad agreement
     across groups tells you the *direction* — the thing is progressing, the risk is not
     materialising. It does not tell you the *number*. Where a single cue supplies the
     magnitude, the confidence word tracks that cue, and drops a band when it is **aged**,
     **weak or moderate**, or **from the same source family as your anchor** — three ways for
     an estimate to inherit one source's error twice while looking corroborated. The worked
     example in §5 is exactly this shape: five groups agree and one is Strong, which reads as
     *high* on the rule above, but the only cue sizing the increment is a moderate, aged,
     same-family-as-the-floor cue, so it publishes **moderate**. Say which cue you graded.
6. Write the navigator's commentary (section 6) — the leaned-on cue and its failure
   story.
7. Write the confirm/deny line: the instrument reading that would confirm the band,
   and the reading that would refute it.
8. Re-run from step 2 whenever a new cue lands or an old one dies. Re-estimation is
   cheap; that is the method working, not the method failing.

## 5. Worked example — project status, tracker stale two weeks

Situation (deliberately generic — swap in your own role): you have inherited a
project mid-flight. The tracker was last updated two weeks ago, when it showed 30 of
50 work items complete. The owner is unreachable. A steering meeting tomorrow will
decide whether to add people to the project, and needs a position on where it really
stands. All figures below are illustrative, not benchmarks.

**Blind spot:** true completion state; decision = staff up or hold, tomorrow.

**Cue inventory:**

| Class | Cue | Source / independence group | Grade | Implication |
|---|---|---|---|---|
| 1 | Tracker: 30/50 done, 14 days ago | Tracker (group A) | Strong (but aged) | Floor: at least 30 done |
| 2 | Weekly integration build ran twice since; both completion emails exist | Build system (group B) | Strong | Work was flowing both weeks |
| 2 | Thursday demo held (not cancelled; notes doc exists) | Calendar + docs (group C) | Moderate | Enough progress to demo |
| 3 | Team's historical pace ~3 items/week; slows before demos | Tracker history (group A) | Moderate | Expect roughly +4–6 items over two weeks |
| 4 | Repository commit activity steady across both weeks | Repo (group B*) | Moderate | Effort continued; *partially shares infrastructure with the build cue — treat B and B* as one group when they merely restate each other |
| 4 | Two new bug threads opened in the project channel | Chat (group D) | Weak | Late-stage testing behavior, mildly positive |
| 5 | No escalations, no deadline-slip emails, sponsor has not complained | Inboxes (group E) | Weak-moderate | Trouble would have been loud here; silence is mildly reassuring |

**Fusion:** floor 30 (group A, aged) + rhythm says +4–6 (group A history, aged the
same way) + independent groups B, C, D, E all consistent with continued normal
progress, none suggesting a stall. Position: **"34 to 36 of 50 items complete, most
likely around 35 — moderate confidence."** Why *moderate* and not *high*, when five
independent groups agree and one of them is Strong: the agreeing groups establish the
direction (work flowed, nothing stalled) and none of them sizes the increment. Rhythm is the
only cue that does, and it is moderate-grade, aged the same way the floor is, and from the
same source family as the floor — so the floor and the increment share one source's error.
That is the rule-5 clause, and it sets both the band width and the confidence word.

**Confirm/deny:** when the owner returns or the tracker is updated, a count of 33–37
confirms the method; below 33 means a stall the side channels missed — investigate
which silence lied.

**The decision:** the meeting can proceed on "on pace, no stall detected, position
moderate-confidence" — a materially better footing than either "the tracker says 30"
(stale) or "we don't know" (false blindness).

## 6. The navigator's-commentary format

Three sentences, spoken or written alongside every position:

1. **The lean:** "This position leans hardest on ⟨cue⟩, because ⟨most direct /
   strongest grade / only cue that sizes the increment⟩."
2. **The failure story:** "If ⟨cue⟩ is wrong, it is most plausibly because ⟨the
   specific way it fails⟩, and the position would then be ⟨direction and rough size of
   the error⟩."
3. **The watch:** "The next cue that should arrive is ⟨cue⟩ at ⟨when⟩; if it doesn't
   show, that absence is itself a signal."

Example, for section 5: "This position leans hardest on the historical pace, because
it is the only cue that sizes the two-week increment. If it is wrong, it is most
plausibly because the team diverted to unlogged rework after the demo, and the true
count would then sit at or below the 30-item floor. The next cue is Monday's
integration-build email; if it doesn't arrive, treat that absence as a signal, not a
glitch."

The commentary is what makes failure legible. Without it, a wrong position discredits
the whole method; with it, a wrong position indicts one cue, whose weight you correct.

## 7. Calibration follow-up

When the instrument returns:

1. Record the true reading next to the banded position you held.
2. Score it: inside the band / outside the band, and by how much.
3. Attribute: which cue earned trust (pointed right), which lied (pointed wrong), and
   whether an independence assumption failed (two "independent" groups turned out to
   share a source).
4. Adjust the standing cue inventory in `your-environment.md`: promote, demote, or
   merge cues based on what the check showed.
5. Keep the log append-only. A handful of scored outages teaches more about your
   environment's cue reliability than any amount of theory — and it is the only
   defense against the drift toward overconfidence that unchecked estimators suffer.

If the same instrument keeps going dark, the calibration log doubles as the
requirements document for fixing or replacing it — at which point the job becomes
building an instrument, and that belongs to `machine-learning-skills:anomaly-detection`
or plain engineering, not to this skill.
