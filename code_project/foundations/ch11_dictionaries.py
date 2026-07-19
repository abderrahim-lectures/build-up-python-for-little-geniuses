"""Chapter 11: Dictionaries. A lookup table – like a times table where you look up 4 × 7 and get 28 – pairs a key with a value; Python's dict does exactly that."""


def total_cost(cart: list, prices: dict):
    """Return the total price of every item in cart, looked up from prices."""
    return sum(prices[item] for item in cart)
