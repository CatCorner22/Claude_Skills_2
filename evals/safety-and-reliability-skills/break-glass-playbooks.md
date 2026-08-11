# Evals — safety-and-reliability-skills:break-glass-playbooks

## 1. Positive trigger (should load the skill)
> "Our pre-mortem on the new payment feed surfaced three ways it could die on us —
> feed outage on a peak day, a bad file poisoning downstream balances, and the vendor
> going dark. If any of those hit tomorrow we'd be scrambling. Turn these into
> something we can actually break glass on."

Expected: skill loads; converts each failure mode into a tripwire-plus-playbook pair;
red-checks every tripwire against the five-part quality bar (measurable, watched by a
named role, cadenced, thresholded, located) and asks "who watches this number, how
often?" where the answer is missing; drafts sealed instructions as ten read-do moves
at calm-headed quality for a cold reader; specifies the pre-granted authority WITH
automatic expiry and full logging; names comms tree and decision chair; sets a drill
date at authoring time and simulates the unsealing drill; states the re-arm loop after
any real firing; poses the design question "what must already exist when the alarm
sounds?"

## 2. Near-miss (failure-mode discovery guard)
> "We're about to commit to the new intake workflow — help us figure out everything
> that could go wrong with it before we lock it in."

Expected: `decision-science-skills:pre-mortem` owns finding the failure modes
(prospective hindsight, silent independent writing, ranking). break-glass-playbooks is
its downstream output stage — it arms failure modes already found, and should route
there rather than load. If it loads on a discovery ask, the seam is failing.

## 2b. Near-miss (adversarial-rehearsal guard)
> "We want to run an exercise where a red cell plays an attacker working around our
> fraud controls while the team responds in real time."

Expected: `decision-science-skills:tabletop-wargaming` owns multi-party exercises with
an adaptive adversary, injects, and adjudication. break-glass-playbooks drills only
the unsealing mechanics of a pre-authored response (find it, open it, authority works,
first moves executable). If it loads on an adversary-play ask, tighten the boundary.

## 3. Quality rubric
- **Does**: every crisis gets a tripwire that passes the five-part bar, with
  graduation (alert level / firing level) where the crisis develops in stages; sealed
  instructions follow the template — header (tripwire, unseals, chair, authority,
  comms, found-at) plus ten verb-first read-do moves, each with an actor role and a
  done-condition; authority grants enumerate scope and carry automatic expiry plus
  full logging; drills are scheduled with a one-line log; the re-arm loop updates
  moves, threshold, and authority after any firing.
- **Teaches**: why pre-authoring banks perishable calm-headed judgment for spending
  during the alarm; why a numeric threshold ends the "is this really it?" debate and
  why graduated triggers let response scale without reopening it; why expiry-plus-
  logging resolves the standing-power vs. 2 a.m.-permission tension rather than
  picking a side; why an untested seal fails at the crisis instead of at the drill.
- **Stays honest**: documented anchors cited with their provenance marks (HIPAA
  break-glass [gov/compliance], NIST/CIS-mapped testing [framework], contingency-plan
  triggers [regulatory]) at practice level with domain-neutral framing; the Foundation
  conceit appears only in triggers and the metadata homage note, never as a claimed
  source of the method; no invented statistics about incident outcomes; boundaries
  respected — failure-mode discovery routed to pre-mortem, checklist form to
  checklist-design, adversary play to tabletop-wargaming, rollback plumbing to
  deploy-and-operate.
