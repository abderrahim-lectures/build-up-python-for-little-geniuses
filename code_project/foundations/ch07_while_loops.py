"""Chapter 7: Repeat Until. A running total that keeps going until you reach a target is exactly what a while loop does: repeat until a condition becomes false."""


def countdown(start: int):
    """Return a list counting down from start to 1 (a while loop, but bounded and testable)."""
    values = []
    health = start
    while health > 0:
        values.append(health)
        health -= 1
    return values
