class StarSystem:
    def __init__(self, planets: list[str], name: str, mass: float, temperature: float):
        self.planets = planets
        self.name = name
        self.mass = mass
        self.temperature = temperature

    def add_planet(self, new_planet):
        return self.planets.append(new_planet)

    def calculate_classification(self):
        pass


class Planet:
    pass
