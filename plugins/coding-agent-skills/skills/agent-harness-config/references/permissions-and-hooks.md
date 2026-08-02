# Permissions and hooks (reference)

## Settings files and precedence
From lowest to highest priority (later overrides earlier):
1. Enterprise / managed settings (administrator-controlled).
2. User settings: `~/.claude/settings.json` (applies to all your projects).
3. Project settings: `.claude/settings.json` (committed, shared with the team).
4. Local project settings: `.claude/settings.local.json` (git-ignored, personal/machine-specific).

Check the effective result with `/config`, `/permissions`, and `/doctor`.

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
