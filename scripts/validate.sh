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
    text = open(md, encoding="utf-8").read()
    for m in REF.finditer(text):
        ref = f"{m.group(1)}:{m.group(2)}"
        if ref in active or ref in agents:
            continue
        if "archiv" in text[max(0, m.start() - WINDOW):m.start()].lower():
            continue          # archived pointer, honestly labelled
        lineno = text.count("\n", 0, m.start()) + 1
        bad.append(f"{md}:{lineno}: unresolved cross-link `{ref}`"
                   + (" (target is archived — mark it as archived)" if ref in archived else ""))
for b in bad:
    print(b)
PY
  ) || true
  if [ -n "$xlink_out" ]; then
    while IFS= read -r line; do err "$line"; done <<< "$xlink_out"
  fi
fi

echo
echo "== Summary: $errors error(s), $warns warning(s), $notes note(s) =="
[ "$errors" -eq 0 ]
