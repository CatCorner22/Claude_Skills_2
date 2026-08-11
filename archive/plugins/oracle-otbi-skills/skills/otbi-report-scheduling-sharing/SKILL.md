---
name: otbi-report-scheduling-sharing
description: >-
  Shares and distributes OTBI content through dashboards and catalog folder permissions, and flags
  OTBI's key limitation — no native scheduling, bursting, or pixel-perfect output — so scheduled,
  burst, or precisely formatted delivery is routed to BI Publisher instead. Use when sharing,
  scheduling, distributing, emailing, or setting permissions on an OTBI report or dashboard, or when
  deciding between OTBI and BI Publisher for delivery. Triggers: share an OTBI report, schedule a
  report, burst a report, email a report on a schedule, distribute a dashboard, catalog permissions,
  pixel-perfect report, BI Publisher vs OTBI, OTBI can't schedule.
---

# Share and schedule OTBI content

## When to use
- Sharing an OTBI analysis or dashboard with a team, or setting who can see/edit it.
- Being asked to schedule, email on a cadence, burst, or produce pixel-perfect output.
- Choosing between OTBI and BI Publisher for how a report is delivered.
- Not for: building the analysis itself → see `oracle-otbi-skills:otbi-report-building`. For which
  subject area to use → see `oracle-otbi-skills:otbi-subject-area-selection`.

## Do it
1. **Share by placing it in a Shared folder.** Save/move the analysis into **/Shared Folders/Custom/…**
   where the audience has access — objects in **/My Folders** are private. Group related analyses on a
   **dashboard** and share the dashboard so the team lands on one page.
2. **Set catalog permissions on the folder/object.** In Browse Catalog, use **More → Permissions** to
   grant read (or edit) to the right roles/accounts. Prefer granting to **roles**, not individuals, so
   access follows job assignments. Remember **data security still applies** — two users opening the
   same analysis each see only the bank accounts / BUs / LEs their data roles allow.
3. **Add a dashboard prompt for self-service.** One shared prompt (As-of Date, Bank Account, Currency,
   Legal Entity) lets each viewer re-scope the page without their own copy — see
   `oracle-otbi-skills:otbi-analysis-filters`.
4. **Recognize when the request exceeds OTBI.** OTBI has **no native scheduling, bursting, or
   pixel-perfect layout**. If the ask is any of:
   - **run on a schedule** (nightly / period-end),
   - **burst** (split one report and email each slice to a different recipient),
   - **pixel-perfect / precisely formatted** output (statements, letters, regulatory PDF),
   - **high-volume paginated export**,
   then it is a **BI Publisher (Oracle Analytics Publisher)** job, not OTBI. BIP schedules, bursts, and
   can join across tables via SQL.
5. **Route it correctly.** Keep interactive, ad-hoc, real-time exploration in OTBI (share via
   dashboard + permissions). Move scheduled/burst/formatted delivery to a BIP report and data model.
   For cross-pillar or historical distribution, consider **FDI/OAC**. Confirm the exact menu paths and
   options in your release.

## Why / learn
OTBI and BI Publisher are two tools for two jobs, and most "how do I send this report" confusion is
really a tool-choice question. OTBI is built for *interactive, real-time, ad-hoc* analysis: you share
it by making the object reachable — a Shared folder, a dashboard, catalog permissions — and each user
runs it live and re-scopes it with prompts. What OTBI deliberately does **not** do is unattended
delivery: it can't wake up at 2 a.m., it can't split a report by recipient and email each slice, and
it can't guarantee a to-the-pixel layout. Those are exactly BI Publisher's job — a separate reporting
engine with a scheduler, bursting, and template-driven pixel-perfect output that can also join across
tables in SQL. So the durable rule is: **share and explore in OTBI; schedule, burst, and format in
BIP.** Recognizing which side of that line a request is on saves you from bending OTBI into a delivery
engine it was never meant to be.

## Common mistakes
- Promising a scheduled/emailed OTBI report → OTBI can't schedule; use BI Publisher.
- Trying to burst from OTBI → not supported; bursting is a BIP feature.
- Leaving a shared report in /My Folders → nobody else can see it. Move it to a Shared folder.
- Granting permissions to individuals instead of roles → access breaks as people change jobs.
- Assuming permission = visibility of all rows → data security still limits rows per user.
- Using OTBI for a pixel-perfect statement/letter → formatting isn't guaranteed; that's a BIP template.

## Tailor to your environment
Record your sharing conventions in `references/your-environment.md` (or
`references/your-environment.private.md`, git-ignored): your Shared folder structure and naming, the
roles you grant read vs. edit, your standard dashboards, and which recurring outputs already run in BI
Publisher (with their schedules/bursting) versus OTBI. **Never commit real recipient lists, account
numbers, or entity names.** This skill then maps its guidance onto your catalog and delivery split.

## References
- references/your-environment.md — your Shared folders, permission roles, dashboards, and BIP vs OTBI split (add when supplied)
