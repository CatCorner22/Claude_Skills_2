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
    return db.get(Job, jid) or raise_(HTTPException(404))
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
    const prev = qc.getQueryData(["todos"]);
    qc.setQueryData(["todos"], (old: Todo[]) =>
      old.map(t => t.id === vars.id ? { ...t, done: vars.done } : t));
    return { prev };
  },
  onError: (_e, _v, ctx) => qc.setQueryData(["todos"], ctx!.prev),
  onSettled: () => qc.invalidateQueries({ queryKey: ["todos"] }),
});
```
Use for near-always-successful writes; skip for meaningful-failure writes.

## Liveness settings
- SSE: heartbeat comment (`: ping\n\n`) every 15s; event ids for resumable feeds.
- WebSocket: ping/pong 20s; server idle timeout > 2× heartbeat; connection cap per node.
- Proxy notes: disable buffering for stream endpoints (nginx `X-Accel-Buffering: no`);
  long read timeouts on stream routes only, not globally.
