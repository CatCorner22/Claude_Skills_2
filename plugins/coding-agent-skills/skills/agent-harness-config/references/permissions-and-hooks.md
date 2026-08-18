# Permissions and hooks (reference)

## Settings files and precedence
From **highest to lowest** priority — the first match wins:

1. **Enterprise / managed settings (administrator-controlled).** Highest, and deliberately
   **not overridable** by anything below it. That is the whole point: an administrator can set
   policy a user cannot edit away.
2. Command-line arguments (this invocation only).
3. Local project settings: `.claude/settings.local.json` (git-ignored, personal/machine-specific).
4. Project settings: `.claude/settings.json` (committed, shared with the team).
5. User settings: `~/.claude/settings.json` (applies to all your projects).

So the ordering runs *narrowest scope wins*, with one exception at the top: managed policy beats
everything precisely because it is not yours to change. Read it as "the more specific and the more
authoritative, the higher."

> An earlier version of this section listed these lowest-to-highest with managed settings at the
> bottom, which said that a git-ignored `settings.local.json` overrides administrator policy. That
> is backwards, and it is the kind of error worth being loud about: someone reading it might
> conclude an enterprise `deny` rule can be worked around locally, or that a policy they shipped is
> being honoured when it is not.

Check the effective result with `/config`, `/permissions`, and `/doctor` rather than reasoning from
the list — those commands report what actually resolved.

## Permission rules
Shape:
```json
{
  "permissions": {
    "allow": ["<Tool>", "<Tool(arg-pattern)>"],
    "ask":   ["<Tool(arg-pattern)>"],
    "deny":  ["<Tool(arg-pattern)>"]
  }
}
```
- Evaluation order: **deny > ask > allow**. A matching `deny` always wins.
- Bash rules can match exact commands or prefixes, e.g. `Bash(npm test)`, `Bash(git push:*)`.
- Prefer allow-listing read-only and test/build commands; keep destructive commands in `ask`/`deny`.
- File tools can be path-scoped, e.g. `Read(./.env)` in `deny` to protect secrets.

## Hooks
Hooks are shell commands the harness runs deterministically on lifecycle events. Configure under
`hooks` in settings.json. Each entry has an optional `matcher` (e.g. a tool name) and a list of
`hooks` with `{ "type": "command", "command": "<shell>" }`.

Common events:
- `SessionStart` — prepare the workspace (install deps, fetch fixtures, print context).
- `UserPromptSubmit` — react to / augment a user prompt before the model sees it.
- `PreToolUse` — run before a tool executes; can **block** the tool (non-zero exit / JSON decision).
- `PostToolUse` — run after a tool executes (e.g. format the file that was just edited).
- `Stop` / `SubagentStop` — run when the model (or a subagent) finishes a turn.
- `Notification` — react to notifications.

Useful variables inside hook commands: `$CLAUDE_PROJECT_DIR` (project root). Keep hook scripts in
`.claude/hooks/` and make them executable. A `PreToolUse` hook that exits non-zero (or returns a
JSON block decision) prevents the tool call — use this for guardrails.

Inspect configured hooks with `/hooks`.

## MCP servers
Define project MCP servers in `.mcp.json`:
```json
{ "mcpServers": { "server-name": { "command": "npx", "args": ["-y", "@vendor/mcp"], "env": {} } } }
```
Reload/restart the session to pick up new servers. Reference MCP tools by fully-qualified name
(`ServerName:tool_name`) in skills and prompts.

## Verifying changes
- `/config` — view settings.
- `/permissions` — view effective permission rules.
- `/hooks` — view configured hooks.
- `/doctor` — health check, including the skill-listing context cost.
Some changes (new MCP servers, brand-new top-level dirs) require a session reload.

> Note: exact hook event names and payload fields evolve across Claude Code versions. Confirm
> against the current docs (https://code.claude.com/docs) or the `/hooks` output for your version.
