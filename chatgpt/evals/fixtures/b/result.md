# Recovered reference artifact

- Release: `1.2`
- Declared status: `stable`
- Source: `mirror/release-1.2.txt`, selected by the release `1.2` entry in `manifest.json` after `primary/release.txt` returned `FileNotFoundError`.
- Declared identity: `fixture-release-1.2`
- Identity proof: the source's SHA-256 is `83fe037273d14a69d23d0c3669e4b332fbb85245a8744f32e94b37763cd95ce4`, exactly matching the manifest's expected SHA-256 for release `1.2`.
- Saved copy: `recovered.txt` (55 bytes).

Verification completed by the assistant: the saved copy was read back, matched the source byte for byte, and matched the manifest hash. The release, declared status, and identity were checked against the recovered content. All original source files were rehashed and remained unchanged.
