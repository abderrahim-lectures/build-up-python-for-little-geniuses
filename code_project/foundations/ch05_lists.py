"""Chapter 5: Lists. A list is an ordered sequence of values, the same idea as a numbered sequence in math – item 1, item 2, item 3."""


def add_item(inventory: list, item: str):
    """Return a new inventory list with item added to the end."""
    return inventory + [item]
