"""Chapter 4: Making Choices. A number line splits into 'less than', 'equal to', and 'greater than' – if/elif/else lets your code make exactly that kind of choice."""


def health_status(health: int):
    """Return a status string for the given health value."""
    if health <= 0:
        return "defeated"
    elif health < 25:
        return "low health"
    else:
        return "ok"
