# Realtime recipes (reference)

## Contents
- Transport decision table
- Job-status pattern
- WebSocket endpoint (when truly needed)
- Optimistic mutation
- Liveness settings

## Transport decision table
| Need | Transport | Client code |
|---|---|---|
| Dashboard fresh within ~10–60s | Polling | `refetchInterval` / `hx-trigger="every 30s"` |
| Progress bar for a job | Polling the status row (or SSE if many watchers) | one query |
| Live feed / notifications | SSE | `new EventSource(url)` |
| Token/response streaming (LLM, logs) | SSE | EventSource or fetch-with-reader |
| Chat, co-editing, cursors | WebSocket | reconnect + heartbeat required |
If in doubt: start one row higher (cheaper); upgrading later is localized because status is
data (see below).

## Job-status pattern
```python
class Job(Base):
    __tablename__ = "jobs"                                   # required: SQLAlchemy 2.0 raises
    id: Mapped[str] = mapped_column(primary_key=True)        # uuid
    status: Mapped[str] = mapped_column(default="queued")    # queued|running|done|failed
    progress: Mapped[int] = mapped_column(default=0)         # 0–100
    result_ref: Mapped[str | None]                           # file path / row id
    error: Mapped[str | None]

@router.post("/reports", status_code=202)
def start_report(params: ReportIn, bg: BackgroundTasks, db=Depends(get_db)):
    job = create_job(db)
    bg.add_task(run_report, job.id, params)   # swap for queue.enqueue(...) at escalation
    return {"job_id": job.id}

@router.get("/jobs/{jid}")
def job_status(jid: str, db=Depends(get_db)):
    job = db.get(Job, jid)
    if job is None:
        raise HTTPException(404)
    return job
```
Worker updates the row as it goes; polling and SSE both just read it. Escalate from
BackgroundTasks to arq/Celery when: jobs must survive restarts, need retries, or saturate
the web process.

## WebSocket endpoint (when truly needed)
```python
@router.websocket("/ws/room/{room}")
async def ws_room(ws: WebSocket, room: str):
    await ws.accept()
    await hub.join(room, ws)                  # in-process dict; Redis pub/sub when multi-node
    try:
        while True:
            msg = await ws.receive_json()     # bidirectional: client sends too
            await hub.broadcast(room, msg)
    except WebSocketDisconnect:
        await hub.leave(room, ws)
```
Client: heartbeat ping every 20s, reconnect with exponential backoff + jitter, resubscribe
state on reconnect. If you're not using the client→server direction, this should be SSE.

## Optimistic mutation
```tsx
const toggle = useMutation({
  mutationFn: patchDone,
  onMutate: async (vars) => {
    await qc.cancelQueries({ queryKey: ["todos"] });
    const prev = qc.getQueryData<Todo[]>(["todos"]);
    // The updater is called with `undefined` when the key is not cached — guard it.
    qc.setQueryData<Todo[]>(["todos"], (old) =>
      old?.map(t => (t.id === vars.id ? { ...t, done: vars.done } : t)));
    return { prev };
  },
  onError: (_e, _v, ctx) => {
    // ctx is undefined if onMutate itself threw; only roll back what we captured.
    if (ctx?.prev !== undefined) qc.setQueryData(["todos"], ctx.prev);
  },
  onSettled: () => qc.invalidateQueries({ queryKey: ["todos"] }),
});
```
Use for near-always-successful writes; skip for meaningful-failure writes.

**Type the updater `T | undefined`, and never dereference `old` bare.** TanStack Query v5 invokes
the functional updater with `undefined` whenever the query key holds no cached data — a first
render, after `queryClient.clear()`, or once the entry is garbage-collected. Verified against
`@tanstack/query-core@5.101.4`: `setQueryData(['todos'], (old) => old.map(...))` on an empty
cache calls the updater with `undefined` and throws
`TypeError: Cannot read properties of undefined (reading 'map')`.

That throw is the dangerous part, because it happens *inside* `onMutate`: the mutation is
rejected before `mutationFn` ever runs, so **the server write silently never happens** while the
UI shows the user's click as accepted. Annotating the parameter `(old: Todo[])` does not prevent
this — TypeScript types are erased at runtime, and the annotation is simply wrong for v5, whose
updater signature is `(oldData: T | undefined) => T | undefined`. For the same reason `ctx!.prev`
in `onError` is a lie the compiler believes: if `onMutate` threw, `ctx` is `undefined` and the
non-null assertion throws a second error inside the error handler.

## Liveness settings
- SSE: heartbeat comment (`: ping\n\n`) every 15s; event ids for resumable feeds.
- WebSocket: ping/pong 20s; server idle timeout > 2× heartbeat; connection cap per node.
- Proxy notes: disable buffering for stream endpoints (nginx `X-Accel-Buffering: no`);
  long read timeouts on stream routes only, not globally.
