# Build Up: Python for Little Geniuses

**Build Up: Python for Little Geniuses** teaches **Python programming** to
11-year-olds, using math problems as the fun, concrete hook for each coding
idea — not a math book with code stapled on. Along the way you build your
own simplified, 2D, Minecraft-like sandbox game, one small piece at a time.

**New here? Run it on MyBinder — no install, no setup, just click and run:**

[![Launch on MyBinder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/abderrahim-lectures/build-up-python-for-little-geniuses/master?filepath=notebooks/ch00_welcome.ipynb)

Prefer a full browser coding environment instead? Open the **Little Genius
Zone**:

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/abderrahim-lectures/build-up-python-for-little-geniuses)

Want to just read the book? *(Live site link — coming soon, once the book
has enough chapters to publish.)*

## What's inside

- **Track A — Foundations**: short, focused Python lessons, one per chapter,
  each with its own MyBinder-powered notebook, runnable inline right on the
  chapter's page.
- **Track B — Build**: one game you build across the whole book, using
  `pgzero`. Chapters 0-7 run anywhere (MyBinder included); Chapter 8 onward
  needs a real display, so that's when you install Python locally. Here's a
  real, playable slice of it today — a fenced land plot (Ch.9), a labeled
  storage crate (Ch.1), and a moveable player with a live HUD (Ch.1/3/10),
  all built from this repo's actual vendored art, not a mockup:

  <p>
    <img src="web/src/images/screenshots/game-start.png" width="360" alt="pgzero game window: starting scene with a fenced land plot, a storage crate, and the player character on a grass grid, HUD showing Ari, HP 100, position (5, 3).">
    <img src="web/src/images/screenshots/game-moved.png" width="360" alt="Same pgzero game window after the player moved right and down, HUD showing the updated position (8, 5).">
  </p>

  Run it yourself: `uv run pgzrun code_project/build_game/game.py`
  (arrow keys move the player).
- **The Little Genius Zone**: a no-install coding environment (GitHub
  Codespaces) with optional bonus "unsolved problems" for kids who finish
  early.

Not sure where to start? See the book's own "How to read this book" page
once it's written — it maps out a few different paths through the book
depending on what you already know.

## How this book was built

This book was written by Claude (Anthropic's AI assistant) working
interactively with a human collaborator. See [`NOTICE.md`](NOTICE.md) for
the full disclosure.

## For developers

- `code_project/` — the real, `pytest`-verified Python package mirroring
  every code block in the book.
- `web/` — the book itself: an [Eleventy](https://www.11ty.dev/) static
  site (chapters are Nunjucks templates in `web/src/`), styled with real
  CSS Grid "zones" and columns for a genuine magazine layout, not a docs
  template.
- `notebooks/` — one MyBinder-ready notebook per chapter, mirroring
  `code_project/foundations/`.
- `assets/` — vendored CC0 art ([Kenney.nl](https://kenney.nl/assets)) and
  the scripts that generate this book's diagrams and pixel art.

Run the tests (this project uses [`uv`](https://docs.astral.sh/uv/) for
Python dependency management):

```sh
uv run pytest code_project/
```

Run the book site locally:

```sh
cd web && npm install && npx @11ty/eleventy --serve
```

## License

MIT — see [`LICENSE`](LICENSE). Covers the code and the book text alike.
