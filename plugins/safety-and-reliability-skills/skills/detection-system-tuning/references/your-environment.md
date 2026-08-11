# Your environment (sanitized template)

Wire in your current role here. This skill is domain-neutral by design — the method
attaches to whatever detection systems you operate in the job you hold now, and moves with
you to the next one. Keep this committed file **structural**: system kinds, roles, and
mechanisms. Real rule names, live thresholds, incident details, client or employer
identifiers, and sample firings belong in `your-environment.private.md` — that suffix is
git-ignored and never committed.

## Detection systems you operate
- **<System>** (queue / inbox / monitor / filter / screen / bot): what it watches, who
  operates it, rough firing volume per <period>
- **<System>**: ...

## Rules and ownership
- Where the rules live: <config, mailbox rules, platform, code>
- Who may change a rule or threshold: <role>
- Layer assignment convention: <how you mark log / digest / queue / page per rule>

## Dispositions
- Where dispositions are recorded (or will be): <location>
- Disposition vocabulary in use: <e.g., acted / benign-known / benign-new / duplicate / unread>
- Audit cadence and owner: <e.g., quarterly, role>

## Paging path and danger signals
- What counts as a page here: <channel, who is interrupted>
- Danger signals available in context: <damage evidence your systems can actually see>
- Queue service level backing the gate: <everything dispositioned within N days>

## Tolerance list
- Where it lives: <location>
- Approver role and default expiry: <role; e.g., one audit cycle>

## Memory cells
- Postmortem/after-action form the memory-cell step is attached to: <which process>
- Where memory-cell rules are implemented and reviewed: <location, cadence>
