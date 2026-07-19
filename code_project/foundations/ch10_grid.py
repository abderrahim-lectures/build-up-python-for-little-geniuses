"""Chapter 10: The Grid. The coordinate plane from math class – an x and a y telling you exactly where a point is – is exactly how a 2D game world tracks where everything stands."""


def move(pos: tuple, dx: int, dy: int):
    """Return a new (x, y) position after moving by (dx, dy)."""
    return (pos[0] + dx, pos[1] + dy)
