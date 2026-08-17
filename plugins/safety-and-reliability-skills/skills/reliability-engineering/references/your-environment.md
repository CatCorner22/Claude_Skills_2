# Your reliability environment (sanitized template)

Fill this in with your real setup. If any entry names real systems, incidents, accounts, or
people, keep it in `your-environment.private.md` instead — that suffix is git-ignored. Commit
only sanitized, structural examples.

- **Monitored feeds/interfaces:** <e.g. overnight data feed, interface run logs, scheduled
  jobs — and where each one's failure timestamps live>
- **Repairable or non-repairable, per dataset:** <the one classification that picks the model —
  repaired-and-returned systems (feeds, jobs, services, machines) go to the NHPP; populations of
  replaceable units each observed to first failure (certificates, disks, cards) go to Weibull>
- **Clock convention:** <operating hours vs calendar time, per dataset>
- **MTTR convention:** <when the repair clock starts (failure occurrence? detection?) and
  stops (restored? verified?)>
- **Uptime commitments / SLOs:** <targets per feed or service, whether each is written
  **time-based** (minutes of downtime) or **event-based** (good ÷ valid events, with an error
  budget), and the business deadline each protects>
- **Maintenance/patch windows:** <when they fall — needed to test for post-patch infant
  mortality>
- **Deterministic expiries:** <certificates, passwords, key rotations — item, renewal owner,
  alarm lead time>
- **Claimed-redundant paths:** <each parallel pair, when failover was last exercised, and
  known common-cause couplings (shared credential, endpoint, patch cycle, person)>
