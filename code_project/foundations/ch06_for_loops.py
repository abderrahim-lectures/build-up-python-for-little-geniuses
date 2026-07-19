"""Chapter 6: Repeat With For. Repeated addition – <code>4 + 4 + 4</code> – is multiplication; a for loop is Python's way of repeating an action a set number of times without writing it out by hand."""


def repeated_addition(value: int, times: int):
    """Add value to a running total, times times, using a for loop."""
    total = 0
    for _ in range(times):
        total += value
    return total
