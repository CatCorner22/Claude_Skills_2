# Stability and redundancy

Designing the system to keep its promises when parts of it fail — because parts of it will.
Redundancy is the Swiss-cheese model in infrastructure: layered, independent, imperfect
defenses that jointly hold. Stability is the discipline that failures degrade service rather
than corrupt data or lose work.

Contents: §1 Promises first (SLOs) · §2 Stability patterns at the seams · §3 Data integrity ·
§4 Redundancy layers · §5 Release safety · §6 Degrade gracefully · §7 Verification

## §1 Promises first: SLOs and error budgets

- Define what "stable" *means* before engineering it: a few SLOs on user-visible symptoms
  ("99.9% of page loads < 2 s", "99.95% of payment posts succeed") — measured from the user's
  side, not the server's.
- The **error budget** (the allowed 0.1%) is the control mechanism: budget healthy → ship
  features; budget burning → reliability work preempts roadmap. This converts "how much
  redundancy is enough?" from taste into arithmetic — and stops both under-engineering and
  gold-plating (redundancy beyond the SLO is muda).
- Alert on budget burn rate, not on every blip — common-cause noise pages nobody.

## §2 Stability patterns at the seams

Failures concentrate where your code meets someone else's (network, DB, third-party API):

- **Timeouts everywhere.** Every network call has an explicit timeout; an unbounded wait is an
  outage in incubation. Budget them end-to-end (the sum along a path must beat the user-facing
  deadline).
- **Retries with judgment.** Retry only idempotent operations; exponential backoff + jitter;
  a retry *budget* (retry storms are self-inflicted DDoS). Distinguish retryable (timeout,
  429, 503) from non-retryable (400, 401, 422) errors.
- **Idempotency keys** on any mutation a client might repeat — the pattern that makes retries
  safe for money. Server stores the key + result; duplicates return the original result.
- **Circuit breakers** on flaky dependencies: after N failures, fail fast and serve the
  fallback; probe periodically; close on recovery. Protects both you (threads not stuck
  waiting) and them (no hammering a struggling service).
- **Bulkheads**: isolate resource pools per dependency so one slow API can't drain the
  connection pool that everything else shares.
- **Queues as shock absorbers**: buffer bursty writes (heijunka for load); consumers process
  at sustainable rate; dead-letter queue + replay for poison messages. The UI acknowledges
  receipt honestly ("submitted, processing") rather than pretending synchronous success.
- **Backpressure over collapse**: shed load explicitly (429 + Retry-After) when saturated;
  a clear "try again shortly" beats a hung spinner for every user at once.

## §3 Data integrity (stability's non-negotiable core)

An outage is recoverable; corrupted or lost data often isn't. Priority order: integrity >
availability > latency > features.

- Transactions around every multi-step invariant; the database's constraints as the last line
  (see `full-stack-standards.md` §4).
- **Autosave and draft preservation** in the UI: a session expiry, crash, or fat-fingered
  navigation must never destroy twenty minutes of form entry. Persist drafts locally or
  server-side; restore on return; say so ("Draft restored from 2:14 PM").
- Soft-delete with retention for user data that matters; hard delete is a migration-grade
  decision.
- Concurrency honesty: optimistic locking / version columns so two editors can't silently
  overwrite each other; the loser gets a merge prompt, not data loss.
- Audit trail on records of consequence (who, what, when, prior value) — append-only.

## §4 Redundancy layers

Apply where the SLO demands it, in this typical order of value:

1. **Backups + tested restore** — the floor. Automated, versioned, off-instance, encrypted;
   restore rehearsed on a schedule with a measured RTO/RPO. An untested backup is a rumor.
2. **Process/instance redundancy** — ≥2 stateless app instances behind a load balancer with
   health checks (liveness vs readiness distinguished) and automatic replacement.
3. **Database redundancy** — replication with automated failover; know your replication lag
   and what it means for read-your-writes.
4. **Zone redundancy** — spread instances/replicas across availability zones; this is the
   cost-effective tier for most business software.
5. **Region redundancy** — only when the SLO genuinely requires surviving a regional event;
   the complexity tax is real (data residency, split-brain, failover drills).
- Non-infrastructure redundancy that's often worth more: dual submission paths for critical
  workflows (API + file import), a read-only mode when writes are down, an export the user can
  take to Excel when everything else fails, and a manual runbook procedure as the human
  fallback layer.

## §5 Release safety (most instability is self-inflicted)

Change causes most incidents, so engineer the change process:

- Deploy ≠ release: **feature flags** let you ship dark and enable gradually — and kill
  instantly (the flag is the andon cord).
- **Canary / blue-green**: new version takes 1–5% of traffic under automated comparison of
  error rate and latency; promotion is earned, rollback is automatic on regression.
- Rollback rehearsed and one-command; schema changes expand-migrate-contract so app rollback
  never strands the database.
- Post-incident: blameless review; the trigger becomes a permanent test or gate (kaizen);
  MTTR and change-failure-rate on the control chart.

## §6 Degrade gracefully (partial failure as a designed state)

- Rank features by criticality: what must survive (viewing records, posting a payment) vs what
  may pause (analytics, recommendations, exports).
- Serve stale-but-marked data when fresh is unavailable ("as of 10:42 — live data delayed");
  cache critical reads with explicit staleness.
- The UI tells the truth in degraded mode: a banner, disabled-with-reason actions, and queued
  operations visible ("3 items will sync when connection returns"). Honest degradation
  preserves trust; fake success destroys it and the data.

## §7 Verification (claims aren't stability)

Every mechanism above is a claim until adversarially exercised — fault injection, gamedays,
restore drills, and failover tests per `adversarial-testing.md` §4. Schedule them; a failover
that has never run is scenery. Wire the results back into the control plan: which drill, how
often, what it proved, who owns the gap.
