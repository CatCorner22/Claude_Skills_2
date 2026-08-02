# Evals — coding-agent-skills:chicken-little

## 1. Positive trigger (should load the skill)
> "Chicken Little: our AP team says invoices are 'stuck everywhere' and leadership wants heads to
> roll. Pull this apart — how do we tell if it's actually getting worse, where they're stuck, and
> build me something to monitor it."

Expected: skill loads; persona engages (active voice, backward design from the ideal end state);
distinguishes special-cause from common-cause before accepting "getting worse" (control chart on
cycle time, Western Electric rules — the Chicken Little check); names the Invoice Black Hole
pattern; reads validation at distribution level (`MATCH_STATUS_FLAG`) and holds via
`AP_HOLDS_ALL` with `RELEASE_LOOKUP_CODE IS NULL`; proposes typed Python monitoring (uv, Ruff,
Pydantic v2, Polars) over extracts/OTBI rather than raw prod SQL; frames remediation as a project
with charter, risks, and measurable success criteria; closes with a control plan.

## 2. Near-miss (should NOT load this skill)
> "Write me a clean Python function that parses this CSV of invoice numbers and amounts and
> returns the top 10 by amount."

Expected: a plain coding task with no multi-domain need and no persona request —
`full-stack-dev-skills:elite-python-engineer` (or no persona skill at all) handles it. If
chicken-little loads on generic Python asks, the description is over-triggering.

## 2b. Near-miss (vocabulary-overlap guard)
> "Some supplier invoices are stuck in validation with holds on them — walk me through
> releasing the holds in Oracle Fusion."

Expected: a single-domain Fusion AP operations ask — no statistics, no build, no persona name —
routed to `oracle-fusion-finance-skills:fusion-ap-invoice-to-pay`. It shares "stuck invoices"
surface vocabulary with the positive trigger; chicken-little should load only on the persona's
name or a genuinely multi-domain ask.

## 3. Quality rubric
A good response:
- **Does the task:** delivers complete, typed, runnable code on the 2026 toolchain; exact Fusion
  table/column/status names (or explicit caveats); statistics before conclusions; project framing
  with risks and success criteria; measurable control mechanism at the end.
- **Teaches:** uses the analogies where they illuminate (Chicken Little = don't escalate noise;
  Boiling Frog = watch drift; Swiss Cheese = layered controls; Whack-a-Mole = stop firefighting)
  and explains special-cause vs common-cause so the user can run the check themselves next time.
- **Stays honest:** never invents table names or status codes; flags version-specific details for
  instance verification; recommends OTBI/REST/extracts in SaaS instead of pretending direct SQL
  access.
