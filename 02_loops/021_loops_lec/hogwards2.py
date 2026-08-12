# students = ["Hermione", "Harry", "Ron", "Draco"]
# houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

students = {                                            # Data Type: dict
            "Hermione": "Gryffindor",
            "Harry": "Gryffindor", 
            "Ron": "Gryffindor",
            "Draco": "Slytherin",
}

for student in students:
    print(student, students[student], sep=", ")


"""
students = {                                            # Data Type: dict
            "Hermione": "Gryffindor",
            "Harry": "Gryffindor", 
            "Ron": "Gryffindor",
            "Draco": "Slytherin",

print(students["Hermione"])                             # Hermione is the Key - Gryffindor is the Value
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])
"""