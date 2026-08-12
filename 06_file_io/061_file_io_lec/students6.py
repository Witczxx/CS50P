import csv

# Switching to Students3.csv
students = []

with open("students2.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})


for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")


# DictReader creates dicts instead of Lists - so the syntax changes
# That's how we add header - with lists it's not possible
# Even if later rows flip or change, dicts are much more robust (Coding Defensively)
