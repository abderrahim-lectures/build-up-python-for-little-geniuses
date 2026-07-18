"""Track B, Chapter 0 unlock: character & world creation.

Plain Python only -- no `pgzero` here yet. Chapters 0-7 build this game's
data and logic without opening a window, so this module runs anywhere,
including Colab and the Little Genius Zone. The first real window shows up
in Chapter 8, once `pgzero` is installed locally (see book/08.../ when it
exists).
"""


class World:
    """The very first slice of the Build Up world: a player with a name and
    a spawn point on a grid. Everything else (inventory, crafting, blocks)
    gets added to this same class chapter by chapter.
    """

    def __init__(self, player_name: str, grid_width: int = 10, grid_height: int = 10):
        self.player_name = player_name
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.player_x = grid_width // 2
        self.player_y = grid_height // 2

    def spawn_point(self) -> tuple[int, int]:
        """Return the (x, y) grid position the player starts at."""
        return (self.player_x, self.player_y)
