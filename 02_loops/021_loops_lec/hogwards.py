students = ["Hermione", "Harry", "Ron"]                 # data type: list

for i in range(len(students)):                         # more control over where to start and stop counting
    print(i +  1, students[i])                         # i + 1 : ranks from 1 to x ; instead of 0 to x


"""
students = ["Hermione", "Harry", "Ron"]                 # data type: list
for student in students:                                # very simple solution!
    print(student)                                      # "for" always starts counting automatically from 0 and goes through it:
"""


"""
students = ["Hermione", "Harry", "Ron"]                 # data type: list
print(students[0])                                      # non-loop solution!
print(students[1])
print(students[2])
"""