#!/usr/bin/env bash
# Lints every skill and manifest in this library against the house standard.
# Usage: bash scripts/validate.sh   (run from the repo root)
# Exit code 0 = clean, 1 = at least one ERROR.

set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT" || exit 2

errors=0
warns=0
notes=0
err()  { echo "ERROR: $1"; errors=$((errors+1)); }
warn() { echo "WARN:  $1"; warns=$((warns+1)); }
note() { echo "NOTE:  $1"; notes=$((notes+1)); }
ok()   { echo "OK:    $1"; }

json_ok() {
  # Validate a JSON file if a parser is available; otherwise skip.
  if command -v python3 >/dev/null 2>&1; then
    python3 -c "import json,sys; json.load(open(sys.argv[1]))" "$1" 2>/dev/null
  elif command -v jq >/dev/null 2>&1; then
    jq empty "$1" >/dev/null 2>&1
  else
    return 0
  fi
}

echo "== Validating manifests =="
for mf in .claude-plugin/marketplace.json plugins/*/.claude-plugin/plugin.json; do
  [ -f "$mf" ] || { err "missing manifest: $mf"; continue; }
  if json_ok "$mf"; then ok "$mf (valid JSON)"; else err "$mf is not valid JSON"; fi
done

# Manifest coherence: JSON validity alone never caught a missing plugin.json, a name that
# disagrees with its directory, a plugin absent from the marketplace, or a marketplace
# description that had drifted from the plugin's own (11 of 14 had, on 2026-08-18).
if command -v python3 >/dev/null 2>&1; then
  man_out=$(python3 - <<'MANPY' 2>&1
import json, glob, os
mk = json.load(open(".claude-plugin/marketplace.json"))
entries = {p["name"]: p for p in mk.get("plugins", [])}
dirs = {os.path.basename(os.path.dirname(os.path.dirname(f)))
        for f in glob.glob("plugins/*/.claude-plugin/plugin.json")}
alldirs = {os.path.basename(d) for d in glob.glob("plugins/*") if os.path.isdir(d)}
for d in sorted(alldirs - dirs):
    print(f"plugins/{d}: has no .claude-plugin/plugin.json")
for name in sorted(dirs - set(entries)):
    print(f"{name}: on disk but absent from marketplace.json")
for name in sorted(set(entries) - dirs):
    print(f"{name}: in marketplace.json but has no plugin directory")
for name in sorted(dirs & set(entries)):
    pj = json.load(open(f"plugins/{name}/.claude-plugin/plugin.json"))
    for field in ("name", "description", "version"):
        if not pj.get(field):
            print(f"{name}/plugin.json: missing required field '{field}'")
    if pj.get("name") and pj["name"] != name:
        print(f"{name}/plugin.json: name '{pj['name']}' != directory '{name}'")
    if "version" in entries[name]:
        print(f"{name}: marketplace.json carries a version; plugin.json is the single source")
    if pj.get("description") and entries[name].get("description") != pj["description"]:
        print(f"{name}: marketplace.json description has drifted from plugin.json")
MANPY
  )
  man_rc=$?
  if [ "$man_rc" -ne 0 ]; then
    err "manifest coherence check failed to run (exit $man_rc) — treat as UNCHECKED: $man_out"
  elif [ -n "$man_out" ]; then
    while IFS= read -r line; do err "$line"; done <<< "$man_out"
  fi
fi

echo
echo "== Validating skills =="
shopt -s nullglob
for dir in plugins/*/skills/*/; do
  skill="${dir%/}"
  base="$(basename "$skill")"
  md="$skill/SKILL.md"
  pre_errors=$errors
  [ -f "$md" ] || { err "$skill has no SKILL.md"; continue; }

  # Extract YAML frontmatter (between the first two '---' fences).
  # The closing fence must exist. Without this check the awk below never hits its exit
  # condition, the whole file becomes "frontmatter", and a truncated SKILL.md passes as OK
  # while its mangled description flows into both generated catalogs.
  fences=$(awk '$0=="---"{n++} END{print n+0}' "$md")
  if [ "$(head -n1 "$md")" != "---" ]; then
    err "$base: SKILL.md does not start with a '---' frontmatter fence"; continue
  fi
  if [ "$fences" -lt 2 ]; then
    err "$base: frontmatter has no closing '---' fence"; continue
  fi
  fm="$(awk 'NR==1 && $0=="---"{f=1; next} f && $0=="---"{exit} f{print}' "$md")"
  [ -n "$fm" ] || { err "$base: no frontmatter"; continue; }

  # name
  name="$(printf '%s\n' "$fm" | awk -F':' '/^name:/{sub(/^name:[[:space:]]*/,""); print; exit}' | tr -d '"'"'"' ' )"
  if [ -z "$name" ]; then
    err "$base: missing 'name'"
  else
    [ "$name" = "$base" ] || err "$base: name '$name' != folder name '$base'"
    printf '%s' "$name" | grep -Eq '^[a-z0-9]+(-[a-z0-9]+)*$' || err "$base: name '$name' must be lowercase alphanumeric with single hyphens"
    [ "${#name}" -le 64 ] || err "$base: name longer than 64 chars"
    printf '%s' "$name" | grep -Eiq 'anthropic|claude' && err "$base: name must not contain 'anthropic' or 'claude'"
  fi

  # description present + length
  if printf '%s\n' "$fm" | grep -q '^description:'; then
    desc="$(printf '%s\n' "$fm" | awk '
      /^description:/{flag=1; sub(/^description:[[:space:]]*/,""); gsub(/^[>|]-?[[:space:]]*$/,""); buf=$0; next}
      flag && /^[a-zA-Z_-]+:([[:space:]]|$)/{flag=0}
      flag{gsub(/^[[:space:]]+/,""); buf=buf" "$0}
      END{print buf}')"
    # Count CHARACTERS, not bytes. `wc -m` silently degrades to bytes under the C/POSIX
    # locale, which over-counts every em dash and arrow by 2 — so the "1024-char" cap was
    # really a byte cap on most runners. Prefer python3 (already required above for JSON).
    if command -v python3 >/dev/null 2>&1; then
      dlen=$(printf '%s' "$desc" | python3 -c 'import sys; print(len(sys.stdin.read()))')
    else
      dlen=$(printf '%s' "$desc" | LC_ALL=C.UTF-8 wc -m | tr -d ' ')
    fi
    if [ "$dlen" -eq 0 ]; then err "$base: empty description"; fi
    if [ "$dlen" -gt 1024 ]; then err "$base: description is $dlen chars (max 1024)"; fi
    if [ "$dlen" -gt 973 ] && [ "$dlen" -le 1024 ]; then note "$base: description is $dlen chars (within 5% of the 1024 cap — watch future edits)"; fi
  else
    err "$base: missing 'description'"
  fi

  # body under 500 lines
  # Count everything after the frontmatter's closing '---'. Only the FIRST TWO '---'
  # lines delimit frontmatter; a later bare '---' is a horizontal rule in the body and
  # must not stop the count (the old form did, reporting a 168-line file as 30 and
  # making the <500 rule bypassable by any skill that used a horizontal rule).
  body_lines=$(awk '/^---$/ && seen<2 {seen++; next} seen==2 {c++} END{print c+0}' "$md")
  [ "$body_lines" -lt 500 ] || warn "$base: body is $body_lines lines (keep under 500)"

  # references one level deep
  if [ -d "$skill/references" ]; then
    if [ -n "$(find "$skill/references" -mindepth 1 -type d 2>/dev/null)" ]; then
      err "$base: references/ must be one level deep (no subdirectories)"
    fi
  fi

  [ "$errors" -eq "$pre_errors" ] && ok "$base" || true
done

# ---------------------------------------------------------------------------
# Installed-shape path check.
#
# A skill runs from a plugin cache with the user's project as cwd, so a runnable
# path like `python scripts/thing.py` resolves to nothing once installed. Bundled
# scripts must be addressed from ${CLAUDE_PLUGIN_ROOT}. (scripts/validate.sh itself
# is exempt: it is a repo-maintenance script and is documented as such.)
# ---------------------------------------------------------------------------
# Scans .md AND .json: assets are templates users copy verbatim, and a bare path in an
# asset comment is exactly as broken as one in prose (found that way, via a nullglob
# accident that had silently disabled this filter entirely — keep the glob quoted).
# Exempt: the two repo-maintenance scripts (documented as run from the repo root), and the
# authoring standard itself, which must quote the bare form as the anti-pattern it forbids.
badpath=$(grep -rnE '(python3?|bash|sh) +"?scripts/[A-Za-z0-9_.-]+\.(py|sh)' plugins/ --include='*.md' --include='*.json' 2>/dev/null \
  | grep -vE 'scripts/(validate\.sh|gen-catalog\.py)' \
  | grep -v 'skills/writing-agent-skills/' || true)
if [ -n "$badpath" ]; then
  while IFS= read -r line; do
    err "${line%%:*}: runnable path is repo-relative; address it from \${CLAUDE_PLUGIN_ROOT}"
  done <<< "$badpath"
fi

# ---------------------------------------------------------------------------
# Cross-link resolution.
#
# Skills reference each other as `plugin-name:skill-name`. A reference can
# legitimately resolve to three things: an active skill, an active subagent
# (installed under the same plugin:name namespace), or an archived skill that
# the text marks as archived. Anything resolving to none of those is a broken
# promise to the reader, so it errors.
#
# Marked-archived references are matched by looking for "archiv" in a character
# window *preceding* the reference, not on its own line — house prose wraps, so
# the mark and the backtick reference are frequently on different lines:
#   (A complete worked map for one product is archived:
#   `continuous-improvement-skills:curve-hero-design-language`, restorable from ...)
# An archived target referenced *without* that mark still errors, because the
# reader is then sent to a skill they cannot install.
# ---------------------------------------------------------------------------
if command -v python3 >/dev/null 2>&1; then
  xlink_out=$(python3 - <<'PY'
import re, glob, os, sys

active = {f"{p.split(os.sep)[1]}:{p.split(os.sep)[3]}"
          for p in glob.glob("plugins/*/skills/*/SKILL.md")}
agents = {f"{p.split(os.sep)[1]}:{os.path.basename(p)[:-3]}"
          for p in glob.glob("plugins/*/agents/*.md")}
archived = set()
for pat, idx in (("archive/skills/*/*", (2, 3)), ("archive/*/skills/*", (1, 3))):
    for p in glob.glob(pat):
        parts = p.split(os.sep)
        if len(parts) > max(idx):
            archived.add(f"{parts[idx[0]]}:{parts[idx[1]]}")

REF = re.compile(r"`([a-z0-9-]+-skills):([a-z0-9-]+)`")
WINDOW = 160          # chars of preceding prose that may carry the "archived" mark
bad = []
for md in glob.glob("plugins/**/*.md", recursive=True):
    # errors="replace" keeps one stray byte from raising, which used to kill this whole
    # check silently: the traceback went to stderr, `|| true` swallowed the exit code, and
    # an empty $xlink_out read as "no broken links".
    text = open(md, encoding="utf-8", errors="replace").read()
    if "\ufffd" in text:
        print(f"{md}:1: file is not valid UTF-8 (decoded with replacement)")
    for m in REF.finditer(text):
        ref = f"{m.group(1)}:{m.group(2)}"
        if ref in active or ref in agents:
            continue
        marked = "archiv" in text[max(0, m.start() - WINDOW):m.start()].lower()
        # The mark alone is not enough: the target must ACTUALLY be in archive/.
        # Previously the mark short-circuited the check, so any reference in a
        # deleted plugin's namespace passed as long as the word "archived" sat
        # nearby -- `accounting-skills:this-skill-never-existed` validated clean.
        # That is exactly how a typo or an invented skill name ships, and the
        # domain plugins were DELETED rather than archived, so their namespace
        # has no valid targets at all.
        if marked and ref in archived:
            continue          # archived pointer, honestly labelled, target real
        lineno = text.count("\n", 0, m.start()) + 1
        if marked and ref not in archived:
            reason = " (marked archived, but no such skill exists in archive/ — the target was deleted, or the name is wrong)"
        elif ref in archived:
            reason = " (target is archived — mark it as archived)"
        else:
            reason = ""
        bad.append(f"{md}:{lineno}: unresolved cross-link `{ref}`{reason}")
for b in bad:
    print(b)
PY
  ) 2>&1
  xlink_rc=$?
  if [ "$xlink_rc" -ne 0 ]; then
    err "cross-link check failed to run (exit $xlink_rc) — treat as UNCHECKED, not as clean: $xlink_out"
    xlink_out=""
  fi
  if [ -n "$xlink_out" ]; then
    while IFS= read -r line; do err "$line"; done <<< "$xlink_out"
  fi
fi

# ---------------------------------------------------------------------------
# Worked arithmetic.
#
# Every skill that teaches a calculation shows it worked. Four review passes
# checked those by hand and one still shipped a table whose totals did not add
# up, so the check is mechanical now. check-arithmetic.py evaluates chains of
# the form `expr = expr = result` and reports the ones that disagree; it skips
# anything carrying variables or units, treats a bare percent as ambiguous, and
# ignores cells under a "Wrong way" column, because a checker that cries wolf on
# a deliberate trap table teaches authors to stop reading it.
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Cross-claims (advisory).
#
# check-cross-claims.py finds COUNTED claims one skill makes about another
# ("the four-step protocol"), which resolve fine as links but go silently false
# when the target gains a step. It was written, documented in the review
# checklist, and then never wired to anything -- so it only ran when someone
# remembered it, which is the same as not having it. Advisory by design: it
# reports, it does not gate, because a legitimate count is common enough that
# erroring would train authors to ignore the output.
# ---------------------------------------------------------------------------
if [ -f scripts/check-cross-claims.py ]; then
  xc_out=$(python3 scripts/check-cross-claims.py 2>&1)
  xc_rc=$?
  if [ "$xc_rc" -gt 1 ]; then
    err "cross-claims check failed to run (exit $xc_rc) — treat as UNCHECKED, not as clean: $xc_out"
  elif [ -n "$xc_out" ]; then
    while IFS= read -r line; do
      case "$line" in
        ""|"=="*) ;;
        *) note "cross-claim: $line" ;;
      esac
    done <<< "$xc_out"
  fi
fi

if [ -f scripts/check-arithmetic.py ]; then
  arith_out=$(python3 scripts/check-arithmetic.py 2>&1)
  arith_rc=$?
  if [ "$arith_rc" -gt 1 ]; then
    err "arithmetic check failed to run (exit $arith_rc) — treat as UNCHECKED, not as clean: $arith_out"
  elif [ "$arith_rc" -eq 1 ]; then
    while IFS= read -r line; do
      case "$line" in
        MISMATCH*|"         "*) err "$line" ;;
      esac
    done <<< "$arith_out"
  fi
fi

# ---------------------------------------------------------------------------
# Trigger-test protocol integrity.
#
# Tier D asks whether a persona skill is reachable by someone who does not know
# its name. A prompt in that column carrying the target's own trigger phrase
# asks a different question and passes for the wrong reason — which is exactly
# what happened on the first executed run, producing a clean Tier D result the
# tier had not earned. Checked mechanically now.
# ---------------------------------------------------------------------------
if [ -f scripts/check-trigger-test.py ] && [ -f docs/trigger-test.md ]; then
  tt_out=$(python3 scripts/check-trigger-test.py 2>&1)
  tt_rc=$?
  if [ "$tt_rc" -gt 1 ]; then
    err "trigger-test check failed to run (exit $tt_rc) — treat as UNCHECKED: $tt_out"
  elif [ "$tt_rc" -eq 1 ]; then
    while IFS= read -r line; do
      case "$line" in TRIGGER-TEST:*) err "$line" ;; esac
    done <<< "$tt_out"
  fi
fi

echo
echo "== Summary: $errors error(s), $warns warning(s), $notes note(s) =="
[ "$errors" -eq 0 ]
