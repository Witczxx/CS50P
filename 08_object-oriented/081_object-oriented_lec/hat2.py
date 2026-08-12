# Before: Instance Methods
# Now: Class Methods

import random


class Hat:
    # __init__ allows to have multiple hats (hat1, hat2, hat3 running)
    # But we only need one hat - so we can make things shorter
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    # Here we also need one - so we add @classmethod
    # We change the main name from "self" to "cls", because other method
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")
