# Build Up: Python for Little Geniuses

A book that teaches **Python programming** to 11-year-olds, using math
problems as the fun, concrete hook for each coding idea — not a math book
with code stapled on. Along the way you build **Build Up**, your own
simplified, 2D, Minecraft-like sandbox game, one small piece at a time.

**New here? Start in Google Colab — no install, no setup, just click and
run:**

- Chapter 0: *(Colab badge — coming soon)*

Prefer a full browser coding environment instead? Open the **Little Genius
Zone** (GitHub Codespaces) — also no install needed.

Want the finished, illustrated PDF? *(Download PDF badge — coming soon,
once `build-up.tex` compiles cleanly.)*

## What's inside

- **Track A — Foundations**: short, focused Python lessons, one per chapter,
  each with its own Colab notebook.
- **Track B — Build**: one game you build across the whole book, using
  `pgzero`. Chapters 0-7 run anywhere (Colab included); Chapter 8 onward
  needs a real display, so that's when you install Python locally.
- **The Little Genius Zone**: a no-install coding environment (GitHub
  Codespaces) with optional bonus "unsolved problems" for kids who finish
  early.

Not sure where to start? See
[`book/learning-paths.tex`](book/learning-paths.tex) once it's written —
it maps out a few different paths through the book depending on what you
already know.

## How this book was built

This book was written by Claude (Anthropic's AI assistant) working
interactively with a human collaborator. See [`NOTICE.md`](NOTICE.md) for
the full disclosure.

## For developers

- `code_project/` — the real, `pytest`-verified Python package mirroring
  every code block in the book.
- `book/` — the book's `.tex` source, chapter by chapter.
- `build/` — the LaTeX build tooling (`build-up.tex` is the top-level
  driver).
- `assets/` — vendored CC0 art ([Kenney.nl](https://kenney.nl/assets)) and
  the scripts that generate this book's diagrams and pixel art.

Run the tests (this project uses [`uv`](https://docs.astral.sh/uv/) for
Python dependency management):

```sh
uv run pytest code_project/
```

Build the PDF:

```sh
# In the Little Genius Zone (Codespaces) or any Linux devcontainer with `make`:
cd build && make pdf

# Locally on Windows (or anywhere without `make`), run latexmk directly:
latexmk -pdf -interaction=nonstopmode -halt-on-error -output-directory=build/pdf build-up.tex
```

## License

MIT — see [`LICENSE`](LICENSE). Covers the code and the book text alike.
