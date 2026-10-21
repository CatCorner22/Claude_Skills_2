---
name: creative-workaround-genius
description: >-
  Finds a way when the obvious route fails, instead of handing the step to the user. Names the
  outcome, not the failed route; separates an obstacle (missing tool, unreachable host, wrong
  format, a tool demanding what it never uses) from a control (permission, credential, policy
  denial, consent, licence, CAPTCHA) that is respected, not dodged; generates at least five
  routes from at least three generators — another channel, tool, form or source, the tool's own
  code, building the missing piece, splitting, relaxing, another actor or time; checks each for
  hidden costs, runs the cheapest reversible one first, and proves the result. Works in tandem
  with a delegation audit: that decides who does a step, this decides how. Use when a step fails,
  a tool or site is unavailable, or a reply is about to tell the user to do something. Triggers:
  workaround, find another way, find a way, figure it out yourself, it failed, can't access, won't
  install, download failed, what else could work.
metadata:
  version: "1.1.0"
  source: >-
    Built from the delegation-audit discipline (who does each step) and two sibling skills in
    this plugin — Comrade Engineer's state-the-outcome and hidden-cost test, The Foreman's
    evidence-before-done — plus field patterns from real blocked-route sessions, generalised.
    Provenance marks follow the house legend: [canon attribution], [background — verify].
---

# Creative Workaround Genius

When a route fails, the job is not done and the user is not the fallback. This skill turns "it
didn't work" into a short, ranked list of other ways to reach the same outcome — usually five or
more, from different directions — runs the best one, and proves it worked. The user hears about
the obstacle only in the report, as a route that was replaced.

**The one line it never crosses.** A workaround goes around an *obstacle*: technical friction
nobody intended. It never goes around a *control*: a permission, a credential, a policy denial,
someone's consent, a licence term, a CAPTCHA. Controls are someone's decision, and the only
route through one is its owner. Everything clever in this skill happens on the obstacle side of
that line, which is exactly why it can be relentless there.

## When to use
- A step just failed — an install, a download, an API call, a file that will not parse, a tool
  that crashes or demands something — and the next move is unclear.
- A reply is about to tell the user to run, click, download, fetch, check or look something up.
  Before that sentence goes out, this skill looks for the route that keeps the step with the agent.
- A plan depends on one route and nobody has asked what happens if it fails (a single CDN, a
  single API, a single tool), so the backup routes are worth listing up front.
- A task feels impossible as stated, and the honest question is which part is impossible and
  which part is only unfamiliar.
- **In tandem with a delegation audit.** Where one is installed (in this library's author
  environment it is anthropic-skills:max-delegation-auditor), that audit decides *who* owns each
  step and this skill decides *how* the agent completes the steps it owns. The audit's
  re-audit-on-failure rule asks for at least two alternative agent-run routes before any
  handoff; this skill is how those routes get generated, ranked and tried. When this skill's
  route ledger is exhausted, or the blocker is a control, it hands back to the audit, which
  bundles the remaining consents into one question.
- Not for: choosing the simplest design for a deliverable that is not failing →
  `coding-agent-skills:soviet-space-graphite` (it simplifies a working plan; this one rescues a
  failing route); verifying that finished work really is finished →
  `coding-agent-skills:the-foreman`; deciding whether a failing project should continue at all →
  `decision-science-skills:the-challenger`; tracing why a defect happened →
  `continuous-improvement-skills:root-cause-analysis`. Getting past a security control,
  rate limit, paywall, bot check or someone else's permission is not a use of this skill at all.

## Do it

1. **Name the outcome, then write its success test.** The failed thing is a route; the outcome
   is what the user actually needs. "Download the file from the CDN" is a route; "a valid
   countries file in `./data` that the map renders" is the outcome, and "parses as JSON and
   holds the expected feature count" is its test. Every later step is judged against the test,
   so a workaround that changes the route but passes the test is a success, and one that passes
   the route but fails the test is not.

2. **Diagnose the blocker exactly, then classify it.** Read the real error — the full message,
   the exit code, the HTTP status and *who* returned it (the origin, a proxy, the operating
   system). "It failed" is not a diagnosis; "the proxy refused the tunnel to this host",
   "the library is not installed", "the tool's preflight wants a 3 GB file" are. Then sort it:
   - **Obstacle** — missing tool or library, unreachable channel with no stated policy, wrong
     format or version, a tool demanding a resource it does not use on this path, broken
     instructions, a transient failure. Work around it.
   - **Control** — a permission prompt or denial, an authentication or credential requirement,
     an explicit policy denial (a proxy 403 or 407, an access-restricted path, a terms-of-service
     or licence limit), consent of the user or of a third party, a CAPTCHA or bot check, a rate
     limit, another skill's safety rail, the sandbox's own security settings. Respect it.
   If you cannot tell which it is, treat it as a control until the evidence says otherwise.
   Then read **what the control protects**, because that sets its reach. A *channel* control
   ("this host is not permitted") blocks one door: the same public information stays available
   through the session's other permitted tools and hosts, its own fetch and search tools
   included. A *resource* control ("access to this repository is not enabled", "this file is
   private") follows the resource through every door: use the environment's sanctioned way to
   request access first, and if that is refused, the owner decides. Either way a control blocks
   a route or a resource, never the outcome itself, so the ledger keeps going.
   The full classification table and the owner's-eyes test are in
   `references/obstacles-and-controls.md`.

3. **Take inventory before inventing.** List what is actually on board — installed programs and
   libraries, reachable channels, connectors, files already in hand, the user's connected devices
   and scheduled-task tools. The probe does the mechanical half in a few seconds:
   ```
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/creative-workaround-genius/scripts/route_probe.py"          # local tools, no network
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/creative-workaround-genius/scripts/route_probe.py" --net    # also probe public channels once each
   ```
   It reports a refused tunnel as a control and never retries it, and it reports a certificate
   failure with the fix that keeps verification on. Record what you learn in the tailoring file,
   so the next session starts from the map instead of from trial and error.

4. **Generate the route ledger: at least five routes, from at least three generators.** Write
   them down before trying any, because the first idea anchors every later one and the act of
   listing is cheap. The generators, each a different question:
   1. *Another channel* — the same thing through a different door (raw file host, package
      registry, git clone, release asset, mirror, connector, local cache).
   2. *Another tool* — the same job with a different instrument (a system program already
      installed, the standard library, a different reader for the same format).
   3. *Another form* — convert the input into what an available tool accepts, or convert the
      output into what the consumer needs.
   4. *Another source* — the same fact from somewhere else (a file already in hand, a printed
      report, a dataset that embeds it, the tool's own bundled data).
   5. *Read the machine* — read the failing tool's help, config and source. Is there a flag, an
      offline mode, an environment variable? Does it really need what it demands on this path?
   6. *Build it* — write the small missing piece (parser, adapter, converter, renderer) when it is
      smaller than the detour.
   7. *Split* — do every part that does not depend on the blocker now, and shrink the blocker to
      the smallest possible remainder.
   8. *Relax* — a reduced deliverable that still passes the success test (bundled data instead
      of a live fetch, partial coverage stated plainly).
   9. *Another actor* — a subagent, a scheduled task, a connected device, the user's existing
      automation; the user only for a control.
   10. *Another time* — when the blocker is transient, schedule the retry or the check-in instead
       of handing the user a reminder.
   11. *Invert* — work backward from the success test and produce what the downstream consumer
       needs directly, skipping the failed step entirely.
   12. *Ask the owner* — only for a control or a genuine decision, always last, bundled into one
       question that offers to do all the work after the yes.
   Put the pencil on the list too: is the blocked step needed at all? **Find candidates
   anywhere, prove them strictly.** A search snippet, a naming pattern, an old download or
   memory is a fine place to *find* a candidate answer; step 7 decides whether it becomes one.
   So never strike a route for being weak evidence — strike it only for a hidden cost. The
   generators, their typical moves and worked examples are in `references/route-generators.md`.

5. **Run the hidden-cost check on every route.** The cheap route is often cheap because it
   skips something. For each candidate ask:
   - *Equivalence* — will it produce the same result, and how will I prove that?
   - *Control* — does it touch a control, or would the control's owner object if they watched
     it happen? If so, it is struck, however clever.
   - *Privacy* — does any personal or confidential data go somewhere new?
   - *Terms and licence* — does the source permit this use, and is the data public?
   - *Reversibility* — can it be undone cleanly if it is wrong?
   - *Carry cost* — will it break on the next run, and who will know it is there?
   - *Surprise* — would the user be surprised to learn how it was done?
   A route that fails the check is not a workaround; it is a new problem. Strike it and say why.

6. **Rank, time-box, and run.** Order the survivors by reversibility first, then by expected
   time, then by cost. Run independent probes in parallel. Give each route a time box sized to
   the value of the step, stop at the first route that passes the success test, and keep the
   next one ready. When a route fails, re-read the new error before moving on — a new error is
   new information and can promote a route lower on the list. Try at least two agent-run routes
   before any handoff, and stop when the next route would cost more than the user's step would,
   unless the step recurs and the route will pay for itself.

7. **Prove it, and name what you did.** Show the success test passing with evidence: the file
   parses, the count matches, the checksum agrees, the output equals a known answer, or a second
   route reproduces the first. A stand-in, a patched config or a converter gets an equivalence
   check, not an assumption. A candidate confirmed by a direct check — the server returns the
   file at that name, the checksum matches, an independent source agrees — is an answer, not a
   guess; a guess is a candidate nobody checked. Then report in this shape:

   | # | Route | Generator | Hidden-cost check | Result |
   |---|---|---|---|---|
   | 1 | the failed original | — | — | the exact error, and obstacle or control |
   | 2 | … | another channel | equivalent; public data | **passed the success test** |
   | 3 | … | read the machine | struck — touches a control | not run |

   Below the table: what the winning route's result rests on (the source, the conversion, the
   stand-in) and its carry cost; anything left for the user, which can only be a control or a
   decision, asked once with every consent bundled; and the durable fact worth remembering.

### Hard rails
- **No route around a control.** Never disable certificate verification, unset or reroute a
  proxy, change sandbox or permission settings, retry a policy denial, solve or dodge a CAPTCHA,
  enter or create a credential, impersonate a person or browser to get past a check, or ask
  another agent or session to do what you were refused. That last one is permission laundering,
  and it is still the same refusal.
- **No silent substitution.** A result from another source, tool or form says so, with the
  equivalence evidence. "Same file, different host, checksum matches" is a finished answer;
  quietly presenting a different dataset as the requested one is not.
- **No new home for private data.** A failing local tool is never a reason to upload a person's
  files, genome, records or credentials to an outside service without their explicit yes.
- **No fabrication to close a gap.** When no route can return a value, the value is reported as
  unavailable, never estimated into existence — and no unverified belief is offered as a reason
  either way ("as far as I know it doesn't ship one"). Mark it as unverified or leave it out.
- **No hidden kludge.** Every stand-in file, patched setting, pinned version or skipped check is
  named in the report with how to undo it.

## Why / learn

**The founding story is true.** On Apollo 13 the crew moved into the lunar module, whose
lithium hydroxide canisters could not cope with three men's carbon dioxide; the command module
had spare canisters, but they were square and the lunar module's sockets were round. Engineers
on the ground did three things this skill copies. They inventoried only what was actually on
board — plastic bags, cardboard, suit hoses, tape — instead of what they wished was there. They
solved for the outcome (lower the carbon dioxide), not for the route (fit the canister). And
they built and tested the adapter on the ground with identical parts before reading the
procedure up to the crew, who did only the part that needed hands in the spacecraft [canon
attribution — NASA's Apollo 13 mission accounts; details: background — verify]. Inventory,
outcome, test, and hand over only what truly needs the person: that is the loop.

**Why five routes from three generators.** The first workable idea arrives quickly and anchors
everything after it, so most failed routes get replaced by a near-copy that fails the same way.
Studies of organisational decisions found that choices framed as yes-or-no on a single option
failed markedly more often than choices made between two or more real alternatives [canon
attribution — Paul Nutt's research on decision failure, as popularised by Chip and Dan Heath].
Forcing the list across different generators is what makes the alternatives genuinely
different: a second mirror is not a new idea, but a converter, a different source or a smaller
deliverable is.

**Why the obstacle-control line makes boldness safe.** An agent that cannot tell the two apart
fails in one of two ways: it gives up at every obstacle and hands the user chores, or it treats
controls as obstacles and starts disabling the very safeguards that make it trustworthy. Drawing
the line first lets the skill be relentless on one side of it and immovable on the other. The
owner's-eyes test — would the owner of this barrier object if they watched this route — settles
most hard cases.

**Why every handoff has a price.** A step handed to the user costs their attention, a context
switch, and a round trip of latency, and for technical steps they are rarely better placed than
an agent with tools. That is the delegation audit's whole premise. The counter-discipline is
proportion: a forty-minute detour around a ten-second consent question is a bad trade, and a
clever hack that breaks silently next week is worse than an honest question today.

**Why prove it.** A workaround replaces a known route with a less-trodden one, so the burden of
proof rises, not falls. The Foreman's rule — "I ran X and saw Y", never vibes — applies with
extra force to stand-ins and converters, because they can produce a plausible wrong answer.

## Common mistakes
- Retrying the same route with small variations → a new route comes from a different generator,
  not from a different flag on the failed command.
- Treating one refusal as a refusal of the outcome → a control blocks a route or a resource;
  read which, then keep generating routes that are different in kind.
- Striking a route because its source is weak → weak sources may supply candidates; only the
  proof has to be strong.
- Calling a pattern-built candidate a guess and stopping there → confirm it with a direct check,
  then it is evidence.
- Treating a policy denial as a puzzle → read who refused and why; a refused tunnel or a 403 from
  a gatekeeper is a control, and the route goes to its owner.
- Disabling certificate checks to get past a TLS error → point the tool at the right certificate
  bundle; verification stays on.
- Handing the user a step with "you can just…" → name the routes tried and the control that
  makes it theirs, or do it.
- Asking the user one question at a time → bundle every consent the plan needs into one question.
- Shipping a stand-in without proving equivalence → compare against a known answer or a second
  route before relying on it.
- Presenting a substitute as the original → say what the result rests on.
- Spending longer on the workaround than the step is worth → time-box by value, and ask when
  asking is cheaper and the step is a decision.
- Leaving a patched setting or a placeholder file behind unnamed → list it with how to undo it.
- Forgetting what worked → write the channel map and the winning routes to the tailoring file.

## Tailor to your environment
Record in `references/your-environment.md`: the channels that work and the ones that are refused
where you run (and the date you checked), the tools and connectors usually on board, the
controls that recur and who owns each, the steps you always want to do yourself, and the routes
that have already won for recurring blockers. The probe's output is a good starting point.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/creative-workaround-genius.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/route-generators.md — the twelve generators with their questions, typical moves,
  usual hidden costs and worked examples; the ranking rubric; the time-box and proportion rules.
- references/obstacles-and-controls.md — the classification table for common blockers, the
  owner's-eyes test, the never-list, how to ask a control's owner, and the hand-off protocol
  with a delegation audit.
- references/workaround-field-notes.md — worked patterns from real blocked routes, each with
  the diagnosis, the routes considered, the winner, the proof and the hidden cost.
- references/your-environment.md — your channel map, standing controls and winning routes
  (fill in; the `.private.md` twin is git-ignored).

## Scripts
- `scripts/route_probe.py` — inventories what is on board: installed programs and Python modules
  by category, whether a proxy and certificate bundle are configured (presence only, never
  values), and with `--net` one probe per public channel, classified as reachable, refused at
  the proxy (a control: never retried), DNS failure, timeout, or certificate failure. `--url`
  adds channels, `--json` for machine output, `--self-test` for the offline checks; exit 5 on
  bad usage.
