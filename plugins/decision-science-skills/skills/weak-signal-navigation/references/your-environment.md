# Your environment (sanitized template)

Wire in your current role here. This skill ships domain-neutral so it survives a job
change: whatever role you hold — analyst, attorney, operations manager, developer,
anything else — list the instruments you actually steer by and the weak cues available
when each one goes dark. Re-fill this file when your role changes; the method carries,
the cue inventory doesn't.

Keep this committed file **structural**: system and cue types, not live readings. Real
figures, client or matter names, and incident details go in
`your-environment.private.md` — that suffix is git-ignored and never committed.

## Instruments you steer by
For each instrument (dashboard, tracker, status report, feed, ledger, docket — by name):
- **Instrument:** <name>
- **What it tells you:** <the position it normally provides>
- **Decisions that need it:** <what gets decided on this reading, and how often>
- **Known failure modes:** <goes stale / lies under condition X / outage history>

## Per-instrument weak-cue inventory
For each instrument above, pre-list the cues by class so an outage starts from a
worksheet, not a blank page:
- **Class 1 — last known-good:** <where the most recent trusted reading lives>
- **Class 2 — scheduled events:** <jobs, meetings, deadlines whose occurrence you can verify indirectly>
- **Class 3 — historical rhythms:** <typical pace/latency/seasonality, and where that history lives>
- **Class 4 — side channels:** <adjacent systems or channels that co-move with the state>
- **Class 5 — absence of noise:** <who would make noise if things were bad, and where>

## Known cue correlations
Cues that share a source and must be counted once:
- <cue> and <cue> both descend from <shared source>

## Calibration log
- **Location:** <file/system, append-only>
- **Entry format:** date, blind spot, banded position held, true reading on return,
  inside/outside band, which cue earned or lost trust
- **Review cadence:** <when you re-grade the standing cue inventory from the log>
