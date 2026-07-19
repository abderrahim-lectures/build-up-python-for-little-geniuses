"""Run code_project/build_game/game.py headlessly (no visible window) and
save real screenshots of it -- not mockups, actual pgzero-rendered frames.

Usage:
    python assets/capture_game_screenshot.py
"""

import os
import sys
from pathlib import Path
from types import ModuleType

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import pygame  # noqa: E402
from pgzero import loaders, builtins as pgzero_builtins  # noqa: E402
from pgzero.game import PGZeroGame, DISPLAY_FLAGS  # noqa: E402

GAME_PATH = ROOT / "code_project" / "build_game" / "game.py"
OUT_DIR = ROOT / "assets" / "screenshots"


def load_module(path: Path) -> ModuleType:
    src = path.read_text(encoding="utf-8")
    code = compile(src, path.name, "exec", dont_inherit=True)
    name = path.stem
    mod = ModuleType(name)
    mod.__file__ = str(path)
    mod.__name__ = name
    sys.modules[name] = mod
    loaders.set_root(mod.__file__)
    pygame.display.set_mode((100, 100), DISPLAY_FLAGS)
    mod.__dict__.update(pgzero_builtins.__dict__)
    exec(code, mod.__dict__)
    return mod


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    mod = load_module(GAME_PATH)

    game = PGZeroGame(mod)
    game.reinit_screen()

    # Frame 1: the starting scene.
    mod.draw()
    pygame.image.save(game.screen, str(OUT_DIR / "game-start.png"))
    print(f"Wrote {OUT_DIR / 'game-start.png'}")

    # Frame 2: after moving the player right and down a few times, so the
    # screenshot actually shows movement working, not just a static scene.
    world = mod.world
    for _ in range(3):
        if world.player_x < mod.GRID_W - 1:
            world.player_x += 1
    for _ in range(2):
        if world.player_y < mod.GRID_H - 1:
            world.player_y += 1
    mod.player.pos = (
        world.player_x * mod.TILE + mod.TILE // 2,
        world.player_y * mod.TILE + mod.TILE // 2,
    )
    mod.draw()
    pygame.image.save(game.screen, str(OUT_DIR / "game-moved.png"))
    print(f"Wrote {OUT_DIR / 'game-moved.png'}")


if __name__ == "__main__":
    main()
