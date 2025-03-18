"""A class focused on the most contemptible of creatures."""

from datetime import datetime


class Goblin:
    """A pitiful wretch."""

    def __init__(self, name: str, favourite_colour: str, speed: int):

        self.validate_goblin()

        self.name = name
        self.favourite_colour = favourite_colour
        self.speed = speed
        self.collapsed = False
        self.hidden = False

    def validate_goblin(self, name, favourite_colour) -> bool:
        if len(name) < 5 or name.lower().count("g") != 2:
            raise ValueError("Invalid goblin name.")
        if favourite_colour.lower() not in ("brown", "green", "grey"):
            raise ValueError("Invalid goblin favourite colour.")
        return True
        
    def run(self, distance: int) -> None:
        """Flees in terror."""
        if distance > self.speed:
            self.collapsed = True

    def hide(self):
        """Attempts to hide."""
        now = datetime.now().time()
        if 9 <= now.hour < 20:
            raise Exception("Goblins cannot hide during the day!")
        self.hidden = True


if __name__ == "__main__":

    g = Goblin("Grzgzy", "green", 5)

    try:
        g.hide()
    except Exception:
        print("Hiding failed.")