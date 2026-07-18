"""Chapter 0: Welcome. Your very first Python code -- runs anywhere, no install."""


def greet(name: str) -> str:
    """Return a friendly welcome message for the given name."""
    return f"Welcome, {name}! You just ran your first line of Python."


if __name__ == "__main__":
    print(greet("Little Genius"))
