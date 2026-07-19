# Design brief: "Build Up: Python for Little Genius" visual system

Full prompt for generating additional book art (chapter banners, badge icons,
checkpoint graphics, mascot poses, MyBinder run-button treatment) via Canva
or an equivalent design tool. Paste the prompt block below directly into the
tool; the surrounding notes are context for whoever runs it.

---

## Prompt

Design a cohesive visual system for **"Build Up: Python for Little Genius"**,
a Python coding book for 11-year-old learners taught through math, styled
like a cross between **Scratch** and **Minecraft** — blocky, chunky,
game-like, but warm and encouraging, never babyish and never
corporate-textbook.

### Established brand (must match exactly, do not reinvent)

- Primary blue `#4C6EF5` (dark variant `#3B5BDB`), amber/gold accent
  `#FFB000` (dark variant `#C98800`), hard black outline `#212121`, soft
  pale-blue background `#EEF1FA`.
- Typography: **Baloo 2** (rounded, extra-bold, chunky) for
  headings/titles, **Nunito** for body text.
- Signature look: thick 3-5px black outlines on every panel/badge, **hard
  offset drop shadows** (not soft blur — flat "game panel" shadows like
  `6px 6px 0 #212121`), circular icon badges sitting on the top-left corner
  of content boxes, a subtle dot-grid background texture (like graph paper
  / a world map).
- Existing mascot: a blocky pixel-art robot standing on clouds holding a
  flag, under a starry blue sky (see `cover.png`).
- Existing chapter banner style: blue sky + orange/tan block wall, no text
  baked into the art (text is overlaid in CSS).

### Use the vendored Kenney.nl CC0 assets directly wherever possible

This project deliberately favors real, reusable asset packs over one-off
generation:

- `assets/kenney/game-icons/` (105 flat, thick-outline, single-color icons)
  — already in use for content-box badges (target, gear, question mark,
  checkmark, star, trophy, wrench). Pull any new chapter badge icons from
  this pack first; only design a custom icon if nothing in the pack fits
  the concept.
- `assets/kenney/rpg-urban-pack/` (480 16x16 top-down tiles, CC0, vendored
  but not yet used) — this is the source material for Track B's actual
  game-world tiles (ground, walls, crates, doors, props) and should also be
  mined for chapter-banner details (e.g. Ch.1 "Variables" → labeled
  storage crates from this pack; Ch.5 "Lists" → inventory-slot tiles; Ch.9
  "Area/Perimeter" → land-plot/fence tiles) so banners feel like real
  extensions of the game world, not disconnected illustration.
- Only commission genuinely new art (via Canva) for pieces Kenney's packs
  can't cover — namely the cover mascot, the chapter-banner sky/background
  composite, and anything needing a pose or scene no flat tile can
  represent.

### What to generate

1. A **chapter banner template** (blue-sky-and-block-wall background, no
   text) for chapters 1-15, each composited with relevant
   `rpg-urban-pack` tiles reflecting that chapter's theme.
2. A **badge icon** per chapter — pulled from `game-icons` first; only
   custom-designed (matching that pack's flat single-color outline style)
   if no existing icon fits.
3. A **checkpoint/waypoint graphic** for "Shop Economy" and "Quest Log,"
   built from `rpg-urban-pack` shop/scroll-style tiles if available,
   styled to match the panel system otherwise.
4. Optional: 2-3 new **mascot poses** (mining, crafting, celebrating) in
   the same palette/outline weight as `cover.png`, since the mascot itself
   has no Kenney equivalent and needs real Canva-generated art.
5. A **"Run this chapter's notebook" button + iframe container treatment**,
   consistent with the rest of the panel system:
   - The trigger button (currently plain green `#579C4C` with a black
     outline and hard offset shadow, matching `.binder-btn`) — refine into
     a proper designed button, ideally using a Kenney `game-icons`
     "play"/rocket-style icon instead of the current `▶` unicode glyph.
   - A **loading/placeholder state** for the `.binder-frame` iframe area
     (560px tall, 4px black outline) shown while MyBinder spins up — since
     first launch can take 1-5 minutes, this needs its own illustration
     (e.g. the mascot "waiting"/tinkering, or a simple animated dot-loader
     in the panel style) so kids don't think it's broken. This is a real
     UX gap right now — the iframe currently just shows blank/browser
     default while loading.
   - A short **inline caption style** (`.binder-note`, currently plain
     italic gray text) for the "first launch can take a minute" warning —
     should look like a small in-world signpost/tooltip rather than a
     generic disclaimer line, so it fits the game aesthetic instead of
     reading as boilerplate.
   - Since the iframe embeds MyBinder's own Jupyter UI (which the book's
     design can't restyle — it's a different origin), the container
     framing (border, shadow, corner badge) needs to visually "own" that
     embedded content as a book panel, the same way a game UI frames a
     video cutscene.

### Constraints

- Flat 2D only, no 3D/isometric, no photorealism.
- Legible at small sizes (badges shrink to ~44-64px on the page).
- Warm, uncluttered, non-native-English-speaker-friendly, no
  scary/violent imagery.
- Transparent-background PNG output, ready to drop into
  `web/src/images/`.

---

## Full description (single-paragraph prose form)

Use this version when a tool expects one continuous text description
instead of a structured brief (e.g. Canva's `generate-design`).

> A cohesive visual system for "Build Up: Python for Little Genius," a
> Python coding book for 11-year-old learners taught through math, in a
> flat 2D art style that blends Scratch's friendly simplicity with
> Minecraft's blocky world — chunky, playful, game-like, warm and
> encouraging, never babyish, never corporate-textbook. Every element uses
> a fixed palette: primary blue #4C6EF5 (dark #3B5BDB), amber/gold accent
> #FFB000 (dark #C98800), hard black outline #212121, and a soft pale-blue
> background #EEF1FA with a faint dot-grid texture like graph paper or a
> world map. Panels, badges, and buttons all share one signature look:
> thick 3-5px black outlines and hard, flat offset drop shadows (like
> 6px 6px 0 #212121, never a soft blur), with circular icon badges perched
> on the top-left corner of each panel. Headings use a rounded,
> extra-bold display face (Baloo 2 in the live site); body text uses a
> clean rounded sans (Nunito). The book's mascot is a blocky pixel-art
> robot standing on clouds holding a flag under a starry blue sky, and the
> existing chapter banners show a blue sky over an orange/tan block wall
> with no text baked into the art. Wherever possible, reuse the real
> vendored Kenney.nl CC0 asset packs instead of inventing new art from
> scratch: pull chapter badge icons from the flat, thick-outline,
> single-color "game-icons" pack (target, gear, question mark, checkmark,
> star, trophy, wrench already in use) before designing anything custom,
> and build chapter-banner details and any game-world scenery from the
> "rpg-urban-pack" 16x16 top-down tile set (crates, walls, doors, shop
> fronts, fences, props) so new art reads as a real extension of the same
> game world rather than disconnected illustration. Needed outputs: a
> blue-sky-and-block-wall banner template for each of chapters 1 through
> 15, individually composited with tiles that hint at that chapter's theme
> (labeled storage crates for "Variables," inventory slots for "Lists,"
> fenced land plots for "Area/Perimeter," a blueprint stencil over a block
> for "Classes & Objects," a small finished village for the capstone
> chapter); one badge icon per chapter, pulled from the icon pack first and
> only custom-drawn, in matching style, when nothing fits; two
> checkpoint/waypoint graphics ("Shop Economy," "Quest Log") built from
> shop- and scroll-style tiles where available; two or three new mascot
> poses (mining, crafting, celebrating) in the same palette and outline
> weight as the cover art, since the mascot has no equivalent in the tile
> packs and needs real bespoke art; and a designed treatment for the
> book's "Run this chapter's notebook" feature, which embeds a live
> MyBinder Jupyter session directly on the page inside an iframe — this
> needs a proper button (ideally a Kenney play/rocket-style icon replacing
> the current plain triangle glyph), a loading/placeholder illustration for
> the iframe area shown during MyBinder's sometimes multi-minute cold
> start (the mascot waiting or tinkering, or an in-style animated dot
> loader, so kids don't think it's broken), an in-world signpost/tooltip
> styling for the short "first launch can take a minute" caption instead of
> a generic gray disclaimer line, and a panel frame (border, shadow, corner
> badge) that visually "owns" the embedded third-party Jupyter UI the same
> way a game's UI frames a cutscene it doesn't otherwise control. Keep
> everything flat 2D with no 3D or isometric perspective and no
> photorealism, legible even at the small sizes badges actually render at
> on the page (44-64px), warm and uncluttered with no scary or violent
> imagery, mindful that many readers are non-native English speakers, and
> export everything as transparent-background PNGs ready to drop into
> web/src/images/.

---

## Note: MyBinder needs a public repo

The run-button/iframe feature (item 5 above) only works end-to-end if
`abderrahim-lectures/build-up-python-for-little-geniuses` is **public** —
MyBinder cannot build from a private repo. The repo is currently private.
Flip visibility back before relying on these iframes for real readers.
