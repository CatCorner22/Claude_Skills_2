# Your realtime map (sanitized template)

- **Surfaces and transports:** <page/feature → polling/SSE/WebSocket, and why>
- **Job runner:** <BackgroundTasks / arq / Celery; the escalation trigger you honor>
- **Job store:** <where status lives; retention of finished jobs>
- **Stream auth:** <cookie session / fetch-with-reader + bearer / stream ticket — EventSource
  can only carry cookies, so this decides the transport for authenticated surfaces>
- **Heartbeats/timeouts:** <SSE and WS settings; proxy config notes>
- **Multi-node fan-out:** <none / Redis pub/sub / sticky sessions>
- **Optimistic-UI surfaces:** <where it's used; where deliberately not>
