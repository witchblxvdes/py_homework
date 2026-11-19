"""Contains basic checks for the ObjectAnalyzer class."""
from object_analyzer import ObjectAnalyzer


# pylint: disable=too-few-public-methods
class Player:
    """Represents a player."""

    def __init__(self, name, health):
        """Initialize a player with a name and health value."""
        self.name = name
        self.health = health

    def heal(self, amount=10):
        """Increase the player's health by the specified amount."""
        self.health += amount


player = Player("Alex", 100)
analyzer = ObjectAnalyzer()

assert analyzer.get_type(player) == "Player"
assert analyzer.get_attributes(player) == ["health", "name"]
assert analyzer.get_methods(player) == {"heal": "(amount=10)"}
assert analyzer.get_inheritance(player) == ["Player", "object"]
assert analyzer.get_documentation(player) == "Represents a player."

assert analyzer.get_attribute(player, "health") == 100
assert analyzer.get_attribute(player, "mana") is None

analyzer.set_attribute(player, "health", 80)
assert player.health == 80

report = analyzer.analyze(player)
assert report["type"] == "Player"
assert report["attributes"] == ["health", "name"]

print("All checks passed!")
