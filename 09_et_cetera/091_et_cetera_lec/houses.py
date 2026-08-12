students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

houses = []

for student in students:
    if not student["house"] in houses:
        houses.append(student["house"])

for house in sorted(houses):
    print(house)

# This is the first Version of solving this Problem
# When you want to put all unique House Names into a list
