### Syntax Improvement compared to students2.py
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)


def get_house(student):
    return student["house"]


# Very Special: We can use a key to sort the whole list
for student in sorted(students, key=get_house, reverse=True):
    print(f"{student['name']} is in {student['house']}")
    # Single Quote needed, becuase Double Quotes outside --- Helping Python to not be Confused!


"""
This key thing is very special, and this function for key get_house() is absolutely needed.
Because each time, the list jumps into a student, it uses the function to extract the "house".
We didn't sue any parenthesis for get_house, right?
And that's how it knows that is needs to sort houses.
"""
