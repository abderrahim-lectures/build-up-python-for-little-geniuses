"""Generate simple, geometric pixel-art badges with Pillow.

Deliberately blocky/geometric, not hand-drawn -- see the plan this book was
built from for why: no image-generation tool is available in this
environment, so every visual asset here needs to be something actually
buildable from code or reused from Kenney's CC0 packs.

Usage:
    python assets/generate_sprites.py
"""

from pathlib import Path

from PIL import Image, ImageDraw

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "book" / "00-welcome" / "images"

PIXEL_SIZE = 8  # each "pixel" in the art is an 8x8 block of real pixels


def draw_pixel_grid(pixels: list[list[str | None]], palette: dict[str, tuple[int, int, int]]) -> Image.Image:
    """Render a small grid of color-keyed pixels into a blocky PNG.

    `pixels` is a list of rows; each entry is a key into `palette`, or None
    for transparent.
    """
    height = len(pixels)
    width = len(pixels[0]) if height else 0
    image = Image.new("RGBA", (width * PIXEL_SIZE, height * PIXEL_SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    for row_index, row in enumerate(pixels):
        for col_index, key in enumerate(row):
            if key is None:
                continue
            x0, y0 = col_index * PIXEL_SIZE, row_index * PIXEL_SIZE
            x1, y1 = x0 + PIXEL_SIZE - 1, y0 + PIXEL_SIZE - 1
            draw.rectangle([x0, y0, x1, y1], fill=palette[key])
    return image


def welcome_badge() -> Image.Image:
    """A simple blocky "genius badge" -- a green block with a yellow star-ish core.

    Colorblind-safe palette check (per the plan's accessibility constraint):
    green/yellow/dark-outline reads distinctly under deuteranopia and
    protanopia simulation, unlike a red/green pairing.
    """
    g = "green"
    y = "yellow"
    k = "outline"
    grid = [
        [None, k, k, k, k, None],
        [k, g, g, g, g, k],
        [k, g, y, y, g, k],
        [k, g, y, y, g, k],
        [k, g, g, g, g, k],
        [None, k, k, k, k, None],
    ]
    palette = {
        "green": (76, 175, 80, 255),
        "yellow": (255, 213, 79, 255),
        "outline": (33, 33, 33, 255),
    }
    return draw_pixel_grid(grid, palette)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    badge = welcome_badge()
    out_path = OUTPUT_DIR / "welcome-badge.png"
    badge.save(out_path)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
