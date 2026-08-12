students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

houses = set()

for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)

# In this Solution, we used the Function set()
# I do not need to write Code to make sure every House is unique
# I can simply trust that set() will take care of that for me
# BTW: set() has the same syntax as a list()
