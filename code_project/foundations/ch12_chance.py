"""Chapter 12: Chance. Rolling a die or flipping a coin is probability in action – Python's random module lets your code do the same roll."""


def roll_die(sides: int = 6):
    """Return a random integer from 1 to sides (inclusive), like rolling a die."""
    import random

    return random.randint(1, sides)
