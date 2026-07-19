"""Chapter 3: Strings & Words. Word problems mix numbers and words – Python's f-strings let your code do the same, dropping a variable's value right into a sentence."""


def player_status(name: str, score: int):
    """Return a friendly status sentence combining a name and score."""
    return f"{name} has {score} points"
