students = ["Hermione", "Harry", "Ron"]

gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]


print(gryffindors)

# Same Solution, but needing much less lines of Code than before
# Not easy to get used to, but recommended
# But this is still a List Comprehension
# Next we will do thereal Dictionary Comprehension
