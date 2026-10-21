# Workaround field notes — patterns that keep recurring

Each note is a pattern seen in real blocked routes, written generically: the symptom, what it
usually means, the routes worth listing, the one that tends to win, how to prove it, and the
hidden cost to name. They are starting points for the ledger, not substitutes for reading the
actual error.

## Contents
- [1. A restricted API, an open file host](#1-a-restricted-api-an-open-file-host)
- [2. The release page is unreachable but the files are not](#2-the-release-page-is-unreachable-but-the-files-are-not)
- [3. A CDN is refused; the data is public elsewhere](#3-a-cdn-is-refused-the-data-is-public-elsewhere)
- [4. A tool demands a resource it never reads](#4-a-tool-demands-a-resource-it-never-reads)
- [5. A library is missing; a system program is not](#5-a-library-is-missing-a-system-program-is-not)
- [6. Nobody accepts the format you have](#6-nobody-accepts-the-format-you-have)
- [7. Certificate errors](#7-certificate-errors)
- [8. No notifications arrive](#8-no-notifications-arrive)
- [9. The search budget or the page fetches run out](#9-the-search-budget-or-the-page-fetches-run-out)
- [10. The step seems to need the person's computer](#10-the-step-seems-to-need-the-persons-computer)
- [11. A tool's documented option is gone](#11-a-tools-documented-option-is-gone)
- [12. A rendered output looks wrong only when viewed](#12-a-rendered-output-looks-wrong-only-when-viewed)

## 1. A restricted API, an open file host
**Symptom.** An API call returns 403 with a message about scope, or the API host is refused,
while plain file downloads from the same platform work. **Routes.** The raw-file host for
individual files; `git clone --depth 1` for a repository; the platform's connector tools when the
session has them. **Proof.** The file's content matches what the API would have returned (size,
checksum, or a field you know). **Hidden cost.** A path-scoped 403 is a control on that path: do
not hunt for another API path that the scope was meant to exclude.

## 2. The release page is unreachable but the files are not
**Symptom.** The project's "latest release" page or API is refused, but the code host works.
**Routes.** `git ls-remote --tags <repo>` lists versions without any API; release assets usually
follow the project's own naming pattern, which the README, the build file or an earlier release
states; a direct download of the asset URL then confirms it. **Proof.** The asset downloads, its
size is plausible, and the archive opens and reports the expected version. **Hidden cost.** A
guessed name that 404s is information, not failure; read the build configuration rather than
guessing repeatedly.

## 3. A CDN is refused; the data is public elsewhere
**Symptom.** A content-delivery host is refused at the proxy. **Routes.** The same package from a
package registry; the source repository from the code host; the upstream dataset from its own
public repository; bundling the data with the project so it never fetches live again. **Proof.**
The same version, the same checksum or the same record count. **Hidden cost.** Name the source in
the output, and change the build to the permitted channel rather than leaving it pointed at the
refused one.

## 4. A tool demands a resource it never reads
**Symptom.** A program refuses to start without a large reference file, a licence file or a
network check, on a code path that does not use it. **Routes.** Its own flag or environment
variable for an existing copy; an offline or no-update option; reading the source to see exactly
what the check verifies; a stand-in that satisfies the check, used only when the source shows the
resource is not read on this path. **Proof.** The output equals a known answer — a run with the
real resource elsewhere, a published result, or an independent tool. **Hidden cost.** If the check
protects correctness on any path you might use later, the stand-in becomes a silent error; name it
in the report and delete it when done.

## 5. A library is missing; a system program is not
**Symptom.** `ModuleNotFoundError` for a PDF, image or document library. **Routes.** Install it
from a permitted registry; or use the system program already present (`pdftotext -layout`,
`convert`, `pandoc`, `soffice --headless --convert-to`); or the standard library for simple
formats. **Proof.** Spot-check the extracted text or the converted file against the original.
**Hidden cost.** Different programs handle tables, encodings and ligatures differently; check the
part you rely on.

## 6. Nobody accepts the format you have
**Symptom.** The best tool for the job reads a format your data is not in. **Routes.** A small
converter written for the purpose, with a self-test; an intermediate standard format both sides
understand. **Proof.** Round-trip a known record, and run the tool on a published example first so
a wrong answer is the converter's fault, not the tool's. **Hidden cost.** Converters drop what
they do not model (reference calls, missing values, strand, units); write those choices down.

## 7. Certificate errors
**Symptom.** `CERTIFICATE_VERIFY_FAILED`, "self-signed certificate in chain", PKIX errors.
**Routes.** Point the tool at the certificate bundle the environment provides (`SSL_CERT_FILE`,
`REQUESTS_CA_BUNDLE`, `PIP_CERT`, `NODE_EXTRA_CA_CERTS`, `GIT_SSL_CAINFO`, a JVM truststore);
check whether a tool config file overrides the environment. **Never** disable verification or
mark a host as trusted to skip it. **Proof.** The same request succeeds with verification on.

## 8. No notifications arrive
**Symptom.** A watcher or webhook cannot be installed, so nothing tells you when a review, build
or merge happens. **Routes.** A scheduled check-in that reads the state directly; the platform's
own read tools; a short status line to the person that check-ins are running. **Proof.** The
check-in fires and reads the real state. **Hidden cost.** Polling has a cost; check at the pace
the underlying state changes, and stop when the thing is done.

## 9. The search budget or the page fetches run out
**Symptom.** Primary pages are refused and a shared search budget is exhausted by parallel
researchers. **Routes.** Search-result excerpts with a provenance mark that says so; the
document's own repository or a public mirror on a permitted host; a primary file the person
already shared; fewer, better-briefed researchers next time. **Proof.** Every claim traces to a
retrieved record, and the report says which claims rest on excerpts. **Hidden cost.** Excerpts
can misattribute; mark them and re-verify anything a decision will rest on.

## 10. The step seems to need the person's computer
**Symptom.** A file lives on the person's machine or drive, or an app runs only there.
**Routes.** A drive or mail connector; a connected device's shell scoped to approved folders; a
launcher file written into a connected folder that the person double-clicks once; a remote
session they already run. **Proof.** The file arrives intact (size, checksum) or the app's output
lands where expected. **Hidden cost.** Each of these needs the person's consent the first time;
ask once, with everything else prepared.

## 11. A tool's documented option is gone
**Symptom.** The documented flag is "unrecognized" or "ambiguous". **Routes.** `--help` of the
installed version; the source's argument parser; the changelog; a full flag name instead of an
abbreviation. **Proof.** The command runs and does what the old option did. **Hidden cost.** Pin
the version in the instructions so the next person does not repeat the hunt.

## 12. A rendered output looks wrong only when viewed
**Symptom.** A generated chart or map passes every structural check but overlaps, clips or paints
in the wrong colour. **Routes.** Rasterise it and look at it; prefer features every renderer
supports (two stacked text elements for a halo rather than a paint-order attribute; explicit
colours rather than context-dependent ones). **Proof.** The rendered image, inspected. **Hidden
cost.** A parse-clean file is not a readable one; build the visual check into the workflow.
