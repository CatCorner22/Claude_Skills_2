# Evals — full-stack-dev-skills:realtime-and-dynamic-features

## 1. Positive trigger (should load the skill)
> "The report generation takes two minutes and times out the request, and management wants
> the ops dashboard to feel live. Do we need WebSockets everywhere?"

Expected: skill loads; moves report generation to a background job (202 + job id,
status-as-a-DB-row) with progress via polling or SSE; puts the dashboard on
polling/`refetchInterval` or SSE per the transport ladder; pushes back on
WebSockets-everywhere (bidirectional need only); heartbeats and proxy notes where streams
are used.

## 2. Near-miss (should NOT load this skill)
> "Add a standard invoice list page with filters and a form to create one."

Expected: static fetching/forms — `full-stack-dev-skills:frontend-modern-ui` (and the
backend skill). If this skill loads, sharpen the realtime framing.

## 3. Quality rubric
A good response:
- **Does the task:** job pattern implemented with persistent status, right-sized transport
  per surface, optimistic UI only on near-always-successful writes.
- **Teaches:** the freshness-vs-cost ladder, requests as leases not contracts for unbounded
  work, status-as-data decoupling transport from progress.
- **Safe:** heartbeats on streams, reconnect/backoff on WS, no in-memory-only job state,
  multi-node fan-out flagged.
