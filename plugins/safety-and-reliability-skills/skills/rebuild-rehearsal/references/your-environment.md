# Your environment (sanitized template)

Wire in your current role here. This skill is domain-neutral by design — an analyst, an
attorney, an operations manager, or a developer can each fill this file with their own
capabilities and rebuild units. Keep the committed file **structural**: roles and
capability types, not names, system identifiers, or access details. Real names, system
paths, credentials, and anything sensitive go in `your-environment.private.md` — that
suffix is git-ignored and never committed.

## Bus-factor census
- **<Capability>**: who can do it <role(s)>, who could learn it <role(s)>, written
  record <what and where>, last done by a non-primary <date or "never">, criticality
  <halts / degrades / annoys>
- **<Capability>**: ...

## Rebuild units
- **<Capability>**: unit <restore-from-backup / recreate-deliverable-from-raw /
  environment-from-docs / process-with-newcomer-driving>, success test <what proves it
  worked>, can-fail check <what a failure would look like>
- **<Capability>**: ...

## Cadence
- **<Capability>**: cadence <e.g., quarterly>, rationale <tenure and criticality it is
  shorter than>, simulated-rebuild interval between real runs <e.g., monthly>
- Typical tenure in this team: <e.g., ~3 years> (the ceiling every cadence must beat)

## Learn-lead-teach roster
- **<Capability>**: driver <role>, lead <role>, corrector <role>, next rotation <when>
- Compression rule if the team is small: <who drives, who corrects, how "lead" rotates>

## Rehearsal log (one line per rehearsal)
- <date> — <capability> — driver <role> — time to complete — gaps found/fixed
- Log location: <where this lives>

## Funding owner
- Owner of the cycle: <role, not a person's name>
- Budget line / hours allocation: <how the rehearsals are resourced>
- Transfer rule: <what happens to the calendar and log when the owner changes roles>
