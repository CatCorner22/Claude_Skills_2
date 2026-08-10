# Your environment (sanitized template)

Fill this in with your real arsenal so the playbooks start from your actual crises and
systems. Keep it **structural**: roles and mechanisms, not live values. Real trigger
thresholds, system names, account identifiers, and access paths go in
`your-environment.private.md` — that suffix is git-ignored and never committed.

## Crisis list
- **<Crisis name>**: source <which pre-mortem / incident produced it>, speed <how fast
  it develops>, playbook status <armed / drafted / none>
- **<Crisis name>**: ...

## Tripwire registry
- **<Crisis>**: metric <what is measured>, threshold <structural description, not the
  live value>, watcher <role>, cadence <how often>, location <where the number lives>,
  graduation <alert level? firing level?>
- **<Crisis>**: ...

## Playbook storage
- Primary location: <where playbooks live>
- Out-of-band secondary: <reachable when the primary or the affected system is down>
- Naming convention: <how a watcher finds the right one fast>

## Authority mechanics
- How sealed grants are implemented here: <break-glass account / escrowed credential /
  pre-approved change class / spend pre-authorization>
- Expiry mechanism: <how the re-lock happens automatically>
- Where use is logged: <system / register>

## Drill calendar
- Cadence: <e.g., quarterly>
- Owner: <role that schedules and records drills>
- Drill log location: <where the one-line-per-drill log lives>

## Chairs and comms
- Default decision chair by crisis family: <role per family>
- Comms tree template: <order of notification, channels, out-of-band fallback>
