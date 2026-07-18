"""Generate the CPA "pictorial" diagrams used throughout the book: number
bonds and bar models, drawn with matplotlib and saved as PNGs for now.

(The book itself is authored directly in LaTeX with `tikz`/`tikz-cd` -- see
the plan this book was built from. This script is the quick, iterable way to
prototype a diagram's content and layout before it gets hand-ported to
`tikz` for the actual chapter file, the same way `lean4-learning` prototypes
diagrams before porting them to `tikz-cd`.)

Usage:
    python assets/generate_diagrams.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "book" / "00-welcome" / "images"

# Colorblind-safe palette (see assets/generate_sprites.py for the same check).
WHOLE_COLOR = "#4C6EF5"  # blue
PART_COLOR = "#FFB000"  # amber
OUTLINE = "#212121"


def number_bond(whole: int, part_a: int, part_b: int) -> plt.Figure:
    """Draw a simple number-bond diagram: whole on top, two parts below,
    connected by lines -- the classic CPA "pictorial" stage for addition
    facts like `whole = part_a + part_b`.
    """
    assert part_a + part_b == whole, "parts must add up to the whole"

    fig, ax = plt.subplots(figsize=(4, 3))
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 3)
    ax.axis("off")

    circle_radius = 0.5

    def draw_circle(x: float, y: float, value: int, color: str) -> None:
        circle = plt.Circle((x, y), circle_radius, facecolor=color, edgecolor=OUTLINE, linewidth=2)
        ax.add_patch(circle)
        ax.text(x, y, str(value), ha="center", va="center", fontsize=18, color="white", weight="bold")

    draw_circle(2, 2.3, whole, WHOLE_COLOR)
    draw_circle(1, 0.7, part_a, PART_COLOR)
    draw_circle(3, 0.7, part_b, PART_COLOR)

    ax.plot([2, 1], [1.85, 1.15], color=OUTLINE, linewidth=2, zorder=0)
    ax.plot([2, 3], [1.85, 1.15], color=OUTLINE, linewidth=2, zorder=0)

    fig.tight_layout()
    return fig


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    fig = number_bond(whole=5, part_a=2, part_b=3)
    out_path = OUTPUT_DIR / "number-bond-5.png"
    fig.savefig(out_path, dpi=150, transparent=True)
    plt.close(fig)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
