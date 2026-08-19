---
name: realtime-and-dynamic-features
description: >-
  Adds the highly dynamic layer to full-stack apps the lean way — choosing polling vs
  Server-Sent Events vs WebSockets by actual need, streaming responses (including LLM token
  streams), live-updating dashboards, optimistic UI, and background jobs with progress
  reporting, using FastAPI primitives and minimal client code. Use when a page must update
  without reload, a response should stream, long work must run in the background with status,
  or when choosing the realtime transport. Triggers: websocket, server-sent events, SSE,
  live updates, streaming response, real-time dashboard, background job progress, optimistic
  UI, long running task API, push updates, live refresh, stream LLM tokens.
metadata:
  version: "1.1.1"
---

# Realtime and dynamic features

## When to use
- A UI must reflect changing server state without reloads: live dashboards, progress bars,
  streams, notifications.
- Long-running work (reports, imports, model runs) needs to run in the background and report
  status.
- Not for: static data fetching and forms → `full-stack-dev-skills:frontend-modern-ui`.
  Deployment concerns of long-lived connections → `full-stack-dev-skills:deploy-and-operate`.

## Do it
1. **Choose the transport by the actual requirement — in this order:**
   - **Polling** (client refetches every N seconds): updates can lag a bit and arrive
     occasionally. With TanStack Query it's one line (`refetchInterval`), with htmx one
     attribute (`hx-trigger="every 10s"`). Most "realtime" dashboards need exactly this.
   - **SSE (Server-Sent Events)**: server→client push over plain HTTP — live feeds, progress,
     token streams. Auto-reconnects natively, works through proxies, no protocol upgrade.
   - **WebSockets**: only for genuine *bidirectional* low-latency traffic — chat, collaborative
     editing, games. Everything else is cheaper one level down.
   The lean rule: every step up the ladder buys latency/direction and costs connection state,
   infra care, and reconnection logic — climb only when the requirement pushes you.
2. **Stream with SSE off a generator** (FastAPI makes it a few lines; LLM token relay is the
   same pattern):

```python
@router.get("/jobs/{jid}/events")
async def job_events(jid: str):
    async def gen():
        async for update in job_updates(jid):          # yields as work progresses
            yield f"data: {update.model_dump_json()}\n\n"
    return StreamingResponse(gen(), media_type="text/event-stream")
```

   Client: `new EventSource(url)` + one `onmessage` handler (or `hx-ext="sse"`). Send a
   comment/heartbeat every ~15s so proxies don't kill idle streams. **Check how the stream
   authenticates before you commit to `EventSource`:** its only option is `withCredentials`, so
   it sends cookies and nothing else — a `headers` option is accepted by the object literal and
   silently dropped (verified against the spec-conformant implementation in Node 22; the server
   saw no `Authorization` header at all). That is fine for the cookie-session app of
   `full-stack-dev-skills:backend-api-development`, and a dead end for the SPA half of it, which
   holds a JWT in an `Authorization` header. Options there, cheapest first: `fetch` with a
   `ReadableStream` reader (carries any header, at the cost of writing your own reconnect —
   which is the one thing `EventSource` was buying you); a short-lived single-use stream ticket
   in the query string; or moving that surface onto the cookie.
3. **Run long work as background jobs, never in the request.** Anything beyond a couple of
   seconds: enqueue, return `{job_id}` immediately (202), report progress via the job's
   status. In-process `BackgroundTasks`/asyncio for fire-and-forget on one node; a queue +
   worker (arq/Celery + Redis) once jobs must survive restarts or need retries — the
   escalation criteria live in `full-stack-dev-skills:full-stack-app-architecture`'s stack
   table. Persist job status in the DB (`queued/running/done/failed` + progress + result
   ref) so *any* transport — polling or SSE — can serve it.
4. **Make dashboards live at the right cost:** metrics that move each minute → polling;
   an activity feed → SSE from an in-process pub/sub (or Redis pub/sub when multi-node);
   htmx dashboards → fragments re-rendered on `hx-trigger="every 30s"` or SSE swap. Design
   the *server* to answer "what changed since t" cheaply (updated_at cursor) so live costs
   stay flat.
5. **Use optimistic UI where the write almost always succeeds** (toggles, small edits):
   update the view immediately, fire the mutation, roll back on error (TanStack Query's
   `onMutate`/`onError` pattern). Skip it for writes that fail meaningfully (payments,
   validations) — the rollback UX is worse than a spinner.
6. **Handle the failure modes you signed up for:** SSE reconnects natively (send event IDs
   and resume via `Last-Event-ID` if the stream is a feed); WebSockets need your
   heartbeat + reconnect-with-backoff; both need server timeouts and connection caps.
   `references/realtime-recipes.md` has the WebSocket endpoint, job-status table, optimistic
   mutation, and the transport decision table.

## Why / learn
"Realtime" is a spectrum of freshness guarantees, and the engineering cost is exponential in
the guarantee: polling is stateless HTTP (free), SSE is one long-lived response per client
(cheap), WebSockets are stateful bidirectional connections the infrastructure must love
(expensive — sticky sessions, upgrade-aware proxies, fan-out state). The discipline is
matching the *user's actual freshness need* — "the dashboard shouldn't feel stale" is a
10-second poll, not a WebSocket mesh. The jobs pattern is the backend half of the same idea:
HTTP requests are leases, not contracts for unbounded work, so long work moves to a queue
and the *status becomes data* — which elegantly decouples transport from progress (any
transport can read a status row, so you can start with polling and upgrade to SSE without
touching the job). Optimistic UI is a bet priced by failure probability: when success is
~always, paying render-now and rolling back rarely buys perceived speed almost free; when
failure is meaningful, the rollback (and the user's mental model of "it was done and then
undone") costs more than honesty. And the heartbeat/reconnect rituals exist because the
network's default state is "quietly broken" — long-lived connections don't fail loudly, they
just stop, so liveness must be manufactured.

## Common mistakes
- WebSockets for a dashboard that changes per minute → polling/SSE; climb the ladder on requirement, not vibes.
- Long work executed inside the request → timeouts and duplicate submissions; 202 + job id + status.
- Job progress only in memory → lost on restart, invisible to other nodes; status is a DB row.
- SSE streams dying silently behind proxies → heartbeat comments; resume with Last-Event-ID for feeds.
- Hand-rolled reconnect for SSE → EventSource does it natively; save the code.
- Optimistic UI on failure-prone writes → rollback whiplash; spinner honesty there.
- Live features that re-query the world each tick → design "what changed since t" queries; keep the tick cheap.
- WebSocket state on one node with multiple replicas → fan-out needs shared pub/sub (Redis) or sticky sessions; see deploy-and-operate.

## Tailor to your environment
Record your realtime map in `references/your-environment.md`: which surfaces use which
transport and why, the job queue choice and its escalation trigger, heartbeat/timeout
settings, and the multi-node fan-out mechanism if any.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/realtime-and-dynamic-features.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/realtime-recipes.md — transport decision table, WebSocket endpoint, job-status pattern, optimistic mutation
- references/your-environment.md — your transports, queue, settings (fill in)
