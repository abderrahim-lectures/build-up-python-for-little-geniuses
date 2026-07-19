# Handoff: Build Up: Python for Little Genius — Visual System

## Overview
A cohesive Scratch/Minecraft-styled visual system for an illustrated Python coding
book ("Build Up: Python for Little Genius") aimed at 11-year-olds. Covers the
chapter banner template, chapter badge icons, checkpoint/waypoint graphics,
mascot poses, and the "Run this chapter's notebook" (MyBinder embed) UI
treatment. This bundle is the design reference — recreate it in the book's
actual site (Eleventy/Nunjucks + plain CSS per the project's own plan) using
real assets in place of the placeholders described below.

## About the Design Files
The .dc.html files in this bundle are **HTML/CSS design prototypes** built in a
proprietary "Design Component" runtime (custom tags like <x-dc>, <x-import>,
<sc-for>, and a support.js runtime) — they will not run as-is outside that
environment. Treat them as **visual/behavioral specs**, not code to copy
verbatim: recreate the same layout, colors, typography, and interactions as
plain HTML/CSS/JS (or Nunjucks templates + a stylesheet, matching the book's
actual Eleventy stack) in the target codebase.

## Fidelity
**High-fidelity.** All colors, spacing, typography, borders, and shadow values
below are final and should be recreated pixel-for-pixel. The only "unfinished"
part is that most imagery is a labeled placeholder (drag-and-drop slot) — see
"Assets to source" below for exactly what real art goes in each slot.

## Design Tokens
- Colors: primary blue `#4C6EF5` (dark `#3B5BDB`), amber `#FFB000` (dark
  `#C98800`), outline/black `#212121`, background `#EEF1FA`.
- Type: **Baloo 2** (600/700/800 weight) for all headings/titles/badges,
  **Nunito** (400/600/700/800) for body copy. Both loaded from Google Fonts.
- Panel system (every card/panel in the book uses this): background white,
  `border: 4px solid #212121`, `box-shadow: 6px 6px 0 #212121` (flat, never
  blurred), `border-radius: 16px`, a circular badge (56px, amber or blue fill,
  3px black border, `box-shadow: 3px 3px 0 #212121`) positioned at
  `top:-20px; left:-20px` overlapping the panel's corner.
- Page background: `#EEF1FA` with a dot-grid texture:
  `radial-gradient(#21212126 1.6px, transparent 1.6px)`, `background-size: 26px 26px`.

## Screens / Views

### 1. Chapter Banner Template (`ChapterBannerTemplate.dc.html`)
- Outer frame: `border: 5px solid #212121`, `box-shadow: 8px 8px 0 #212121`,
  `border-radius: 18px`, `overflow: hidden`. Fixed height 270px.
- Circular chapter-number badge (64px, blue `#4C6EF5`, white "01" text, Baloo 2
  800) sits at `top:-24px; left:24px`, overlapping the top edge.
- Two vertical zones inside the frame:
  - **Sky (56% height)**: background image `assets/banner-sky-strip.png` (a
    1587×500 crop of the book's real cover art — stars, pixel clouds, faint
    city-silhouette — see "Assets to source" #1), `background-size: cover`,
    `image-rendering: pixelated`, plus a subtle blue-to-amber linear-gradient
    overlay for atmosphere.
  - **Wall (44% height)**: two-tone amber checkerboard
    (`conic-gradient(#D9962B 90deg, #C98800 90deg 180deg, #D9962B 180deg
    270deg, #C98800 270deg)` tiled 42×42px) plus faint grid lines
    (`repeating-linear-gradient`, `#21212155`, 39–42px steps, both axes), two
    small "lit window" accent squares (22×22px, dark navy `#2A2A45` fill, amber
    glow via `box-shadow: 0 0 10px 2px #FFB00099`), and an 8px-inset content
    area that holds the chapter-specific tile art (a labeled placeholder in
    this bundle).
  - A soft inset vignette (`box-shadow: inset 0 0 60px 10px rgba(33,33,33,.35)`)
    sits over the whole banner for depth.
  - Chapter title is plain white Baloo 2 800, 26px, centered, `text-shadow: 2px
    2px 0 #212121`, overlaid at the bottom — never baked into the art.
- **Progress hotbar** below the banner: "Chapter N of 15" label (Baloo 2 800,
  13px, blue), then a row of 15 adjacent 26×26px square slots (Minecraft-hotbar
  style, no connecting line/path — avoid anything resembling a Mario-style
  world-map trail), each with a 2px right border, current chapter's slot amber
  `#FFB000`, others pale `#EEF1FA`, whole row wrapped in a 3px black border +
  `3px 3px 0 #212121` shadow.
- Three small (140px tall) example variants below, reusing the same
  sky-image + checkerboard-wall treatment at smaller scale, each labeled
  "Ch.1 · Variables", "Ch.5 · Lists", "Ch.9 · Area & Perimeter".

### 2. Chapter Badge Icons (`BadgeIcons.dc.html`)
- Grid of circular badges, 84px diameter, white fill, 3px black border,
  `box-shadow: 4px 4px 0 #212121`, each holding a 66px icon placeholder and a
  caption (icon name + source: "game-icons" or "custom").
- 9 icons planned: target, gear, question mark, checkmark, star, trophy,
  wrench (all from Kenney's game-icons pack), plus map (game-icons) and
  blueprint (custom, matching the pack's flat single-color outline style).

### 3. Checkpoint / Waypoint Graphics (`CheckpointGraphics.dc.html`)
- Two wide panels ("Shop Economy", "Quest Log"), each: white panel (standard
  panel system), 110×110px image area on the left, title (Baloo 2 800, 19px)
  + one-line description on the right, small circular badge ($ / pencil icon)
  overlapping the top-left corner.

### 4. Mascot Poses (`MascotPoses.dc.html`)
- Row of 150×150px rounded panels (4px black border, `5px 5px 0 #212121`
  shadow, 16px radius, blue `#4C6EF5` fill behind the art).
- 4 poses: "Cover (existing)" — **already filled** with
  `assets/mascot-cover.png` (the real robot cropped out of the book's cover
  art, flag/pole removed) — plus "Mining", "Crafting", "Celebrating" as
  placeholders needing new bespoke art in the same palette/outline weight.

### 5. "Run This Notebook" Treatment (`BinderTreatment.dc.html`)
- **Trigger button**: green `#579C4C` fill, 4px black border,
  `5px 5px 0 #212121` shadow, 12px radius, a 30×30px icon slot (play/rocket
  glyph) + "Run This Chapter's Notebook" label in Baloo 2 700.
- **Loading state**: 280px-tall panel (standard panel system) on the dot-grid
  background, an amber gear badge at the top-left corner, a mascot
  "waiting/tinkering" image slot (140×140px), "Launching your Jupyter
  session…" text, and 3 bouncing dots (`@keyframes dotbounce`, staggered
  0/.15s/.3s delays, 1.1s ease-in-out infinite, `translateY(-10px)` peak).
- **Signpost caption**: amber `#FFB000` tag shape via
  `clip-path: polygon(0 0,100% 0,100% 100%,14px 100%,0 70%)` (a pennant/sign
  look, not a plain italic disclaimer), 3px black border,
  `4px 4px 0 #212121` shadow, pin emoji + bold caption text: "First launch can
  take 1–5 minutes — the workshop's warming up!"
- **Loaded state**: 220px-tall panel, blue circular corner badge with a ▶
  glyph, a diagonal-stripe placeholder standing in for the actual (unstylable,
  cross-origin) MyBinder/Jupyter iframe content — the panel's border/shadow/
  badge is what visually "owns" that embedded third-party UI.

## Interactions & Behavior
- All imagery in this bundle is a **drag-and-drop placeholder** (a custom
  "image-slot" component) — in the real site these become plain `<img>` tags
  once real assets exist.
- The dot-bounce loading animation and the "lit window" glow are the only
  animated/stateful pieces; everything else is static layout.
- No other click handlers, forms, or routing are defined in this bundle.

## Assets to source (not yet real art — currently placeholders)
1. **`assets/banner-sky-strip.png`** — already real (cropped from the book's
   own cover art). Reuse as-is; do not regenerate.
2. **`assets/mascot-cover.png`** — already real (robot cropped from cover art,
   flag removed). Reuse as-is for the "Cover (existing)" mascot slot.
3. **Kenney.nl CC0 packs** — download directly:
   - `https://kenney.nl/assets/game-icons` → badge icons (target, gear,
     question, checkmark, star, trophy, wrench, map).
   - `https://kenney.nl/assets/rpg-urban-pack` → banner tile scenes (crates /
     inventory slots / fences) and checkpoint tiles (shop-front / scroll).
   Unzip preserving each pack's own folder + `Spritesheet/*.xml` name mapping;
   read real filenames from the XML, never guess. Credit Kenney.nl CC0 in an
   `assets/kenney/ATTRIBUTION.md`.
4. **Bespoke art** (no Kenney equivalent, needs real illustration matching
   `mascot-cover.png`'s palette/outline weight): mining/crafting/celebrating
   mascot poses, the mascot "waiting" pose, a play/rocket run-button icon, and
   the custom "blueprint" badge icon.

## Files
- `Visual System Style Guide.dc.html` — main page (header, foundations, panel
  anatomy) that mounts the 5 section files below.
- `ChapterBannerTemplate.dc.html`, `BadgeIcons.dc.html`,
  `CheckpointGraphics.dc.html`, `MascotPoses.dc.html`,
  `BinderTreatment.dc.html` — the 5 section templates described above.
- `assets/banner-sky-strip.png`, `assets/mascot-cover.png` — real cropped
  cover-art assets, already wired in.
- `image-slot.js` — the placeholder component used throughout (reference only
  — not needed in the target codebase).
