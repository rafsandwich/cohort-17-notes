# Blueprint
class Goblin:

    species = "Gobbus Gobbus"

    # When a new goblin is spawned
    def __init__(gob, name):
        gob.name = name

if __name__ == "__main__":
    g = Goblin("Zak")
    print(g.name)
    g = Goblin("Honore")
    print(g.name)


def do_stuff():

    do_other_stuff()

do_stuff()

def do_other_stuff():
    pass


