"""Chapter 14: Debugging. Checking your work – the same habit from math class – is what debugging and testing are: verifying your code's answer is actually right."""


def safe_divide(a: float, b: float):
    """Return a / b, or None instead of crashing when b is 0."""
    if b == 0:
        return None
    return a / b
