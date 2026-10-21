# Your environment — tailoring template for creative-workaround-genius

This file ships as a template. **Copy it to `.claude/skills-env/creative-workaround-genius.private.md`
in your own project and fill in the copy** — the `.private.md` suffix is what keeps it out of git,
and a `/plugin marketplace update` can overwrite this shipped copy. Confirm with
`git check-ignore -v` before writing anything into it. Record names and outcomes only; never a
credential, token, password or private URL.

## 1. Channel map (date checked)
Paste or summarise the output of `route_probe.py --net`, and add channels you rely on.

| Channel | Verdict | Date | Note |
|---|---|---|---|
| | reachable / refused-at-proxy / refused-by-origin / dns-fail / timeout / tls-fail | | |

## 2. On board
- Programs that matter for your work:
- Python or other modules usually present:
- Connectors usually approved (drive, mail, calendar, code host, others):
- Devices or remote sessions that can be reached, and with what consent:
- Scheduling tools available (scheduled tasks, check-ins):

## 3. Standing controls and their owners
| Control | Owner | How to ask |
|---|---|---|
| e.g. network allowlist | environment owner | settings page; one request with the host and reason |

## 4. Steps you always want to do yourself
(Anything here is treated as yours even when an agent could do it — for example signing,
submitting, paying, or sending under your name.)

## 5. Winning routes for recurring blockers
| Blocker | Winning route | Proof used | Date |
|---|---|---|---|
