"""Chapter 1: Variables. A variable is like a labelled storage crate: put a value inside, write a name on it, and Python remembers it until you change it."""


def describe_player(name: str, score: int, health: int):
    """Return a one-line status string for a player."""
    return f"{name} - score: {score}, health: {health}"
