""" To make an object, we need to define a blueprint/recipe to make one """

class Chair:
    def __init__(self, name: str):
        self.number_of_legs = 4 # the self keyword refers to itself
        self.name = name
        print(f"Wow I'm alive! My name name is {self.name}!")

    
    def sitting_on(self):
        print("You sat on me!")


class Squirrel:
    def __init__(self, colour: str):
        self.arms = True
        self.colour = colour
    
    def climb(self):
        print("WHEEEEE!")
    

chair = Chair("Pablo")
print(chair.number_of_legs)
chair.sitting_on()
chair_two = Chair("Juan")