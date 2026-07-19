"""Chapter 15: Capstone. Every math unit ends with a review that mixes every skill you've learned – this chapter does the same for everything you've built."""


def build_summary(name: str, inventory: list, prices: dict):
    """Return a one-line summary combining a player's name, inventory, and the shop's prices."""
    items = ", ".join(inventory)
    cheapest = min(prices.values()) if prices else 0
    return f"{name} is carrying: {items}. Cheapest shop item: {cheapest} coins."
