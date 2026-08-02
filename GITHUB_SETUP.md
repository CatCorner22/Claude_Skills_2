# Connect to GitHub — Claude_Skills_2

This project is configured to push to:

**https://github.com/blakeReaganGH/Claude_Skills_2**

Branch: `cursor/dental-notes-standardizer-054b`

## Status (last attempt: 2026-08-02)

- Git remote `origin` → `https://github.com/blakeReaganGH/Claude_Skills_2.git`
- Local branch `cursor/dental-notes-standardizer-054b` — 5 commits ready to push
- GitHub repo `blakeReaganGH/Claude_Skills_2` — **not found** (create it or complete auth for private repo)
- GitHub authentication — **pending device login** (see below)

## Option A — Device login (fastest right now)

1. Open **https://github.com/login/device**
2. Enter code: **`B5B6-F98F`** (expires in ~15 minutes; ask agent to regenerate if expired)
3. Authorize for `blakeReaganGH`
4. Reply **"auth done"** in the agent chat so it can push and open the PR

## Option B — Connect GitHub in Cursor (recommended for future runs)

1. Open **Cursor Settings → Integrations → GitHub**
2. Connect your `blakeReaganGH` account
3. Create the repository on GitHub if it does not exist:
   - Name: `Claude_Skills_2`
   - Owner: `blakeReaganGH`
4. Re-run this cloud agent from the linked repo, or ask the agent to push again

## Option C — Add SSH deploy key

Add this public key to the `Claude_Skills_2` repo  
(**Settings → Deploy keys → Add deploy key**, allow write access):

```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIE8MLNGrKIfzDQ4KtHPNeuQutA11asfcw2qjiJrTrlV8 blakereaganlaw@gmail.com
```

Then push:

```bash
cd /agent
git push -u origin cursor/dental-notes-standardizer-054b
```

## Option D — Personal access token (HTTPS)

1. Create a GitHub PAT with `repo` scope
2. Run:

```bash
cd /agent
git remote set-url origin https://github.com/blakeReaganGH/Claude_Skills_2.git
git push -u origin cursor/dental-notes-standardizer-054b
```

## After push — open PR

```bash
gh auth login   # if not already authenticated
gh pr create --base main \
  --head cursor/dental-notes-standardizer-054b \
  --title "Dental notes standardizer benchmarked against Curve Hero" \
  --body "Adds Vite + React dental notes standardization app and Curve Hero benchmark documentation."
```

## Local commits ready to push

```
c015833 Ignore TypeScript build info artifact
a7ff44e Add downloadable Curve Hero clinical notes benchmark markdown
be8d1ad Add consolidated Curve Hero clinical notes benchmark markdown
a52dccf Implement dental notes standardizer benchmarked against Curve Hero
```
