"""Smoke-test the real pgzero game (code_project/build_game/game.py) by
loading and drawing it headlessly, the same way assets/capture_game_screenshot.py
does -- catches crashes in draw()/update(), not just the plain-Python World class.
"""

import os
import sys
from pathlib import Path
from types import ModuleType

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

ROOT = Path(__file__).resolve().parent.parent.parent
GAME_PATH = ROOT / "code_project" / "build_game" / "game.py"


def _load_game_module() -> ModuleType:
    import pygame
    from pgzero import loaders, builtins as pgzero_builtins
    from pgzero.game import PGZeroGame, DISPLAY_FLAGS

    src = GAME_PATH.read_text(encoding="utf-8")
    code = compile(src, GAME_PATH.name, "exec", dont_inherit=True)
    mod = ModuleType("build_game_test")
    mod.__file__ = str(GAME_PATH)
    sys.modules[mod.__name__] = mod
    loaders.set_root(mod.__file__)
    pygame.display.set_mode((100, 100), DISPLAY_FLAGS)
    mod.__dict__.update(pgzero_builtins.__dict__)
    exec(code, mod.__dict__)

    game = PGZeroGame(mod)
    game.reinit_screen()
    return mod


def test_game_draws_without_crashing():
    mod = _load_game_module()
    mod.draw()  # would raise if any sprite/asset failed to load


def test_game_update_moves_player_right():
    mod = _load_game_module()
    start_x = mod.world.player_x
    mod.keyboard.right = True
    try:
        mod.update()
    finally:
        mod.keyboard.right = False
    assert mod.world.player_x == start_x + 1
