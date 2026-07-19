# Attribution

Art assets in this folder are vendored from [Kenney.nl](https://kenney.nl/assets),
released under [CC0](https://creativecommons.org/publicdomain/zero/1.0/)
(public domain — no attribution legally required, credited here anyway
because Kenney's work makes this book's whole visual design possible).

## Packs vendored

- **Game Icons** (`game-icons/`, https://kenney.nl/assets/game-icons) — 105
  monochrome game UI icons, downloaded directly from Kenney.nl and unzipped
  preserving the pack's own structure (`PNG/Black|White/1x|2x/`,
  `Spritesheet/*.xml` name atlas, `Vector/`). Real filenames were read from
  `Spritesheet/sheet_black1x.xml`, never guessed. Used for the small icon
  badges on each recurring box type (`target` for objectives, `question` for
  the Socratic box, `gear` for concepts, `wrench` for the build box,
  `checkmark` for knowledge checks, `star`/`trophy` for the retrieval
  challenge) in `web/src/images/icons/`, and for the run-button/checkpoint
  icons in the visual-system design bundle (`play` = `forward.png`).
  **No `map` or `compass` icon exists in this pack** — verified against the
  real downloaded XML atlas (105 entries), not assumed from the design
  spec's mention of one. `map` and `blueprint` badge icons were hand-drawn
  instead, in the same flat single-color silhouette style, for future
  chapter badges (blueprint = Ch.9 "Classes & Objects").
- **RPG Urban Pack** (`rpg-urban-pack/`, https://kenney.nl/assets/rpg-urban-pack)
  — 480 16x16 pixel-art tiles for city/urban RPG scenes, downloaded directly
  from Kenney.nl and unzipped preserving the pack's own structure
  (`Tiles/tile_NNNN.png`, `Tilemap/`). This pack ships **without** a
  `Spritesheet/*.xml` name atlas (verified — only numbered tiles), so
  individual tiles used below were identified by visual inspection of the
  actual sprite (never guessed from an index or filename) and are recorded
  here by tile number for traceability:
  - `tile_0300.png` — wooden storage crate (Ch.1 "Variables" banner + badge
    scenes).
  - `tile_0443.png` — storage locker / cabinet with drawer compartments,
    stands in for "inventory slots" (Ch.5 "Lists" banner scene).
  - `tile_0355.png` / `tile_0356.png` / `tile_0357.png` — wire/wood fence
    sections (Ch.9 "Area & Perimeter" banner scene).
  - `tile_0328.png` / `tile_0329.png` — striped shop awning, confirmed
    against the pack's own `Sample.png` reference scene where the same tile
    fronts a storefront (checkpoint "Shop Economy" scene).
  - Composited scene PNGs built from these tiles live in
    `assets/visual-system-extracted/assets/` (`banner-tiles-generic.png`,
    `banner-thumb-variables.png`, `banner-thumb-lists.png`,
    `banner-thumb-area.png`, `checkpoint-shop-front.png`).
  - **No scroll/parchment/ledger prop exists in this pack** (it's an urban
    pack, not a fantasy one) — checked before falling back to a hand-drawn
    scroll icon for the "Quest Log" checkpoint (`checkpoint-quest-scrolls.png`,
    also used as `web/src/images/icons/scroll.png`). An earlier pass in this
    project had wrongly used `game-icons`' `scrollHorizontal.png` for this —
    that icon is actually a left/right pan-arrow glyph, not a scroll, caught
    by visually zooming it in rather than trusting the filename.

## Bespoke (non-Kenney) art

Generated via Canva (`generate-design`, `design_type: logo`, prompted to
match `mascot-cover.png`'s exact palette/outline weight — flat 2D, no
isometric/3D) since neither Kenney pack has a mascot-character equivalent:

- `assets/visual-system-extracted/assets/mascot-mining.png`,
  `mascot-crafting.png`, `mascot-celebrating.png` — new mascot poses for the
  visual system's "Mascot Poses" section.
- `assets/visual-system-extracted/assets/mascot-waiting.png` — mascot
  tinkering/waiting pose, used in the MyBinder loading-state illustration
  (also copied to `web/src/images/mascot-waiting.png` for the live site).
- Canva's free-plan export doesn't support transparent PNG, so each was
  exported flat and had its background removed locally (border flood-fill +
  a direct color-match pass for enclosed pockets, e.g. between an arm and
  the torso) rather than by hand.

## Scope

Flat top-down/pixel packs for Track B's actual game tiles, plus icon and UI
packs for badges. Any isometric-block pack is decorative only (e.g. a cover
graphic), never used for the game world itself — this book's `pgzero` game
stays 2D top-down throughout.
