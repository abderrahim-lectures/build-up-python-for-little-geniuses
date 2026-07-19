"""Chapter 13: Blueprints. Grouping related facts about one thing – a shape's length AND width together – is what a class does: it bundles data and behavior into one blueprint."""


class Player:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def take_damage(self, amount: int) -> None:
        """Reduce health by amount, but never below 0."""
        self.health = max(0, self.health - amount)
