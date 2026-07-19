"""Track B, Chapter 8+ milestone: the first real pgzero window.

Run with: pgzrun code_project/build_game/game.py

A small top-down scene using this book's real vendored assets (Kenney's
rpg-urban-pack for tiles/player, this project's own visual system for the
HUD colors) -- a real, playable slice of the game the book builds one
chapter at a time, not a mockup.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from code_project.build_game.world import World

TILE = 64
GRID_W, GRID_H = 10, 6
WIDTH = GRID_W * TILE
HEIGHT = GRID_H * TILE + 48  # extra strip at the bottom for the HUD

world = World(player_name="Ari", grid_width=GRID_W, grid_height=GRID_H)
player = Actor("player")
player.pos = (
    world.player_x * TILE + TILE // 2,
    world.player_y * TILE + TILE // 2,
)

# A small fenced land plot (Ch.9 Area & Perimeter) and a labeled storage
# crate (Ch.1 Variables) placed directly in the world, not just described.
FENCE_TOP_LEFT = (2, 1)
FENCE_SIZE = (3, 2)  # (length, width) -- same variables the book's area()/perimeter() take
CRATE_POS = (7, 4)


def fence_tiles():
    (fx, fy), (length, width) = FENCE_TOP_LEFT, FENCE_SIZE
    for x in range(fx, fx + length):
        yield (x, fy)
        yield (x, fy + width - 1)
    for y in range(fy, fy + width):
        yield (fx, y)
        yield (fx + length - 1, y)


def draw():
    screen.clear()
    for gx in range(GRID_W):
        for gy in range(GRID_H):
            screen.blit("ground", (gx * TILE, gy * TILE))
    for (fx, fy) in fence_tiles():
        screen.blit("fence", (fx * TILE, fy * TILE))
    screen.blit("crate", (CRATE_POS[0] * TILE, CRATE_POS[1] * TILE))
    player.draw()

    screen.draw.filled_rect(
        Rect((0, GRID_H * TILE), (WIDTH, 48)), (33, 33, 33)
    )
    screen.draw.text(
        f"{world.player_name}  HP: 100  pos: ({world.player_x}, {world.player_y})",
        (12, GRID_H * TILE + 14),
        color=(255, 255, 255),
        fontsize=22,
    )


def update():
    moved = False
    if keyboard.right and world.player_x < GRID_W - 1:
        world.player_x += 1
        moved = True
    elif keyboard.left and world.player_x > 0:
        world.player_x -= 1
        moved = True
    elif keyboard.down and world.player_y < GRID_H - 1:
        world.player_y += 1
        moved = True
    elif keyboard.up and world.player_y > 0:
        world.player_y -= 1
        moved = True
    if moved:
        player.pos = (
            world.player_x * TILE + TILE // 2,
            world.player_y * TILE + TILE // 2,
        )
