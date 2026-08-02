---
name: agent-harness-config
description: >-
  Configures the Claude Code harness — settings.json layers and precedence, tool
  permission rules (allow/ask/deny), automated hooks (SessionStart, PreToolUse,
  PostToolUse, Stop, and more), MCP servers, and environment variables. Use when
  setting up a repo for Claude Code, reducing permission prompts, automating a
  behavior that should run every time X happens, or wiring up an MCP server.
  Triggers: settings.json, permissions, allow this command, hooks, run automatically,
  whenever X do Y, MCP server, .mcp.json, configure Claude Code, harness config.
---

# Configuring the Claude Code harness

## When to use
- Setting up a repository so Claude Code sessions can run its tests/linters/build.
- Reducing repeated permission prompts by allow-listing safe commands.
- Automating a behavior that must run **every time** something happens (a "whenever X, do Y"
  request) — that requires a hook, because the harness executes it, not the model's memory.
- Adding or configuring an MCP server, or setting environment variables for sessions.
- Not for: writing skills themselves → see `coding-agent-skills:writing-agent-skills`; general
  prompt wording → see `coding-agent-skills:prompt-engineering`.

## Do it
1. **Pick the right settings file (they layer; later overrides earlier):**
   - Enterprise/managed (admin) → user `~/.claude/settings.json` → project `.claude/settings.json`
     (committed, shared) → project `.claude/settings.local.json` (git-ignored, personal).
   - Put team-wide rules in the committed project file; keep personal or machine-specific rules
     in `settings.local.json`.
2. **Set permissions** to cut prompts without going unsafe. In `settings.json`:
   ```json
   {
     "permissions": {
       "allow": ["Bash(npm test)", "Bash(npm run lint)", "Read", "Grep"],
       "ask":   ["Bash(git push:*)"],
       "deny":  ["Read(./.env)", "Bash(rm -rf:*)"]
     }
   }
   ```
   Scope Bash rules to specific commands/prefixes; prefer allow-listing read-only and test
   commands. `deny` beats `ask` beats `allow`. See `references/permissions-and-hooks.md`.
3. **Automate behaviors with hooks** (the only way to make something happen *every time*):
   ```json
   {
     "hooks": {
       "PreToolUse": [
         { "matcher": "Bash",
           "hooks": [ { "type": "command", "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/guard.sh" } ] }
       ],
       "SessionStart": [
         { "hooks": [ { "type": "command", "command": "make bootstrap" } ] }
       ]
     }
   }
   ```
   Common events: `SessionStart` (prepare the workspace), `UserPromptSubmit`, `PreToolUse` /
   `PostToolUse` (guard or react to tool calls; a `PreToolUse` hook can block), `Stop` /
   `SubagentStop`, `Notification`. A hook is a shell command the harness runs; exit codes and
   JSON output control whether the action proceeds. Keep hook scripts in `.claude/hooks/`.
4. **Configure MCP servers** in `.mcp.json` (project) so Claude can use external tools:
   ```json
   { "mcpServers": { "my-db": { "command": "npx", "args": ["-y", "@acme/mcp-db"], "env": {} } } }
   ```
   Restart or reload the session to pick up new servers.
5. **Set environment/session behavior** via `env` in settings.json (e.g. non-secret config) and
   keep secrets out of committed files. Verify with `/config`, `/permissions`, `/doctor`, and
   `/hooks`.
6. **Validate:** re-open a session (or reload), trigger the behavior, and confirm the hook fires
   / the prompt no longer appears / the MCP tools are listed.

## Why / learn
The harness is the runtime around the model, and this matters because of a hard boundary: the
**model** decides what to do next, but only the **harness** can guarantee something happens on a
schedule or on an event. That is why a request like "every time you edit a file, run the
formatter" cannot live in a memory note or a skill instruction — the model might forget or a
compaction might drop it — and must be a `PostToolUse` hook the harness fires deterministically.
Permissions work the same way: they are enforced by the harness before a tool runs, so an
allow-list is a *safety and friction* control, not a suggestion to the model. Understanding the
settings **layering** (enterprise → user → project → local, later wins) is what lets you put
shared guarantees in the committed project file while keeping personal tweaks local and
git-ignored. Once you see the harness as "the deterministic shell that the probabilistic model
runs inside," you know where each kind of rule belongs.

## Common mistakes
- Trying to automate a recurring behavior via a memory/preference instead of a hook → it won't
  reliably fire. Use `hooks` in settings.json.
- Over-broad allow rules (`Bash(*)`) → removes the safety net. Scope to specific commands/prefixes.
- Putting secrets or machine-specific paths in the committed `settings.json` → use
  `settings.local.json` (git-ignored) or environment variables.
- Editing settings and expecting live pickup → some changes (new MCP servers) need a reload/restart.
- Forgetting precedence → a `deny` or a local-file override silently wins; check with `/permissions`.

## Tailor to your environment
Record your repo's real setup in `references/your-environment.md` (git-ignore anything sensitive
as `*.private.md`): the exact test/lint/build commands to allow-list, the SessionStart bootstrap
your project needs, any MCP servers you use, and behaviors you want automated. This skill then
writes the precise `settings.json` entries for your stack. If you only need a simple settings
change (theme, model), the `/config` command is faster.

## References
- references/permissions-and-hooks.md — permission rule syntax, precedence, and the hook events with examples
- references/your-environment.md — your project's commands, bootstrap, MCP servers (add when supplied)
