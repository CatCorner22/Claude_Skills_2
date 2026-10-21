# Obstacles and controls — where the workaround stops

Every blocker is one of two things. An **obstacle** is friction nobody intended: a missing
library, a format mismatch, an unreachable host with no stated policy, a tool that demands
something it never uses. A **control** is somebody's decision: a permission, a credential, a
policy, a consent, a licence, a check that a human is present. This skill works around obstacles
relentlessly and never around controls. This file is how to tell them apart and what to do with
each.

## Contents
- [§1 The owner's-eyes test](#1-the-owners-eyes-test)
- [§2 Classification table](#2-classification-table)
- [§3 Hard cases](#3-hard-cases)
- [§4 The never-list](#4-the-never-list)
- [§5 How to ask a control's owner](#5-how-to-ask-a-controls-owner)
- [§6 Hand-off protocol with a delegation audit](#6-hand-off-protocol-with-a-delegation-audit)

## §1 The owner's-eyes test

Ask: **if the person or system that owns this barrier watched this route happen, would they
object?** If yes, or if you cannot tell, it is a control, and the route goes to the owner.

Two refinements make the test usable:
- **Read who refused.** The same "403" means different things when the origin server sent it
  (that path is restricted), when a proxy sent it (the destination is not permitted for this
  session), or when it is a rate limit (slow down; do not dodge). The probe's verdicts carry that
  distinction: `refused-by-origin`, `refused-at-proxy`, and so on.
- **Read what it protects: a channel or a resource.** A refusal that names a host or a path
  ("this destination is not permitted") is a channel control; one that names a thing ("access to
  this repository is not enabled for this session", "this document is private") is a resource
  control. The same public information may travel through any other permitted channel; a
  controlled resource may not, and its route is the environment's sanctioned access request,
  then the owner. A control never forbids the outcome itself: public information about a
  controlled resource, published elsewhere by its owner or a third party (a package index entry,
  a public announcement, a search result), remains a legitimate source.
- **A permitted channel is not evasion; a disguised one is.** When a network allowlist blocks a
  content-delivery host but permits a package registry or a public code host, fetching the same
  **public** file from the permitted host is using the channel the owner allowed. Changing the
  request so a refused host stops recognising it — another user agent, a tunnel, a proxy hop, a
  borrowed credential — is evasion. The difference is whether the route works *within* the rules
  or works by hiding from them.

## §2 Classification table

| Blocker | Usually | The right move |
|---|---|---|
| Module or program not installed | obstacle | install from a permitted registry, or use an installed alternative |
| Package registry reachable, one CDN refused at the proxy | control on that host, obstacle for the data | fetch the same public artefact from a permitted channel; state the source |
| Proxy refuses the tunnel (`Tunnel connection failed: 403/407`) | control | do not retry; use a permitted channel or ask the owner to allow the host |
| Origin answers 401 / 403 on a path | control | do not retry; find a public path or ask for access through the owner |
| HTTP 429 or a rate-limit header | control | back off and schedule a later retry; never rotate identities to dodge it |
| Certificate verification failed | obstacle (configuration) | point the tool at the configured certificate bundle; verification stays on |
| Name does not resolve | obstacle, possibly policy | another channel first; report if the host is required |
| Wrong file format or schema | obstacle | convert it (generator 3) and prove the conversion |
| Tool's preflight demands a resource it does not read on this path | obstacle | read the code; satisfy the check with a verified stand-in or a flag; prove equivalence |
| Documentation describes an option that no longer exists | obstacle | read the tool's help and source for the current mechanism |
| Permission prompt, or the user denied a tool call | control | do not try the same action another way; ask once, with the reason |
| An automated permission reviewer denies an action | control | stop that action; do not rephrase or reroute it; continue only with routes different in kind, each stating its purpose plainly |
| "Access to this <resource> is not enabled for this session" | resource control | use the environment's sanctioned access request (an attach or add tool); if refused, ask the owner; public information published elsewhere stays usable |
| Login, password, API key, two-factor code | control | the person enters it, or a connector they approved is used |
| CAPTCHA or bot detection | control | never solve or evade; use an official API or connector, or ask |
| Terms of service forbid automated access | control | use the official API or export, or ask the person to export |
| Licence restricts redistribution or commercial use | control | use a permissively licensed alternative, or link instead of bundling |
| A third party's personal data or consent | control | only with that person's consent; never route around them through the user |
| Another skill's safety rail (no dosing, no relatedness tests) | control | it stands; offer what the rail permits |
| A sandbox setting (network policy, file-system scope) | control | work inside it; ask the owner to change it if the task truly needs it |
| A service is down, a CI run is pending, a merge has not happened | obstacle (time) | schedule a check-in or retry (generator 10) |
| A step needs physical hands, a device the agent cannot reach, or a signature | control (by nature) | prepare everything, then ask for only that step |

## §3 Hard cases

- **"The download failed, just turn off SSL verification."** The request is for a control change
  even though the person asking owns the task. Disabling verification removes the protection
  against a tampered download for every request the tool makes. The route is to give the tool
  the right certificate bundle, which almost always fixes it; if it does not, say exactly what
  failed and why verification must stay on.
- **"Use my account; here's the password."** Credentials stay with their owner. Offer a
  connector the person approves, a token they paste into the tool's own prompt, or a step they
  perform themselves with everything prepared.
- **A preflight check for a file the tool never reads.** Satisfying it with a stand-in is a
  workaround of an obstacle only when the code shows the file is not read on the path in use
  and the output is proven equivalent (same answer as a run with the real file, or as an
  independent result). Otherwise the check may be protecting correctness, and the stand-in is a
  silent wrong answer waiting to happen.
- **A mirror of blocked content.** Public data republished on a permitted host is fine and gets
  cited as such. A copy of restricted content (paywalled, private, licensed) is not public just
  because someone mirrored it.
- **A subagent or another session "could just try it".** If you were refused, the refusal
  covers every agent acting for the same person. Asking a teammate to do it is permission
  laundering.
- **The person says "do whatever it takes".** That widens the obstacle side, not the control side.
  It is permission to try harder, not permission to bypass safeguards.

## §4 The never-list

Never: disable or weaken certificate verification; unset, change or chain proxies; edit
permission or sandbox settings; retry a policy denial; rotate identities or user agents to evade a
block or rate limit; solve or route around a CAPTCHA; enter, create or store credentials on the
person's behalf; scrape against stated terms; impersonate a person or a client; move private data
to a new service without consent; ask another agent to do what you were refused; present a
substitute result as the original; fabricate a value no route could return.

## §5 How to ask a control's owner

Ask once, late, and bundled — the delegation audit's rule. The question carries:
1. the outcome and what is already done;
2. the single control in the way, and who owns it;
3. what the agent will do immediately after the yes, so the person's part is one action;
4. the routes already tried, in one line, so the person can see this is not the first resort.

Template: "Everything for X is ready except one thing only you can do: Y (because it needs your
credential / your consent / a setting you own). After you do it, I will run Z and send the
result. I tried A and B first; both hit the same control."

## §6 Hand-off protocol with a delegation audit

A delegation audit (in this library's author environment, anthropic-skills:max-delegation-auditor)
marks each step as the agent's, the agent's with consent, or the person's only. The two skills
interlock at three points:
1. **Before execution.** For every step the audit leaves with the person, this skill asks whether
   the step is a control or merely an unfamiliar obstacle. Obstacles come back to the agent with a
   route ledger.
2. **On failure.** The audit's re-audit rule wants at least two alternative agent-run routes before
   any handoff. This skill generates the ledger, runs it, and reports which routes were tried.
3. **At the end.** Whatever remains is a control or a decision. The audit bundles those into one
   consent question; this skill supplies the "what I tried" line and the "what I do after the yes"
   line.
