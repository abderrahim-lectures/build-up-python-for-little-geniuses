# PDF version history

Built PDFs archived here, one per notable milestone — same pattern as
`lean4-learning`'s `lean_book/pdf-history/`. Naming:

- `v<version>-build-up.pdf` for a tagged release (version matches
  `pyproject.toml`)
- `local-wip<N>-<short-description>.pdf` for an untagged, work-in-progress
  snapshot worth keeping around (e.g. before/after a layout change)

Unlike `build/pdf/` (the ephemeral `latexmk` output directory, gitignored),
this folder is tracked in git on purpose — it's a deliberate historical
record, not a build artifact.
