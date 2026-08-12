students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)


for student in sorted(students, key=lambda student: student["name"], reverse=True):
    print(f"{student['name']} is in {student['house']}")


"""
lambda = "hey python, here I have a function, but it has no name"
s: sagt hier - ein einziges listenelement - wir definieren einfach ein element wie bei "for" Schleifen.
"""
