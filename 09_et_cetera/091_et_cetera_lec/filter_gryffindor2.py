students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]


def is_gryffindor(s):
    return s["house"] == "Gryffindor"


gryffindors = filter(is_gryffindor, students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])

# We define a Function, which filter() can use
# Compared to map(), filter() won't output all results, but only the ones fitting our Conditions

# Do you remember keys and lambda from the past?
# Can be used similar to filter the results we want to have.

# When I want to use filter without defining a function, I can just paste the text after "return"
# But I need to do it like this: lambda s: s["house"] == "Gryffindor"
