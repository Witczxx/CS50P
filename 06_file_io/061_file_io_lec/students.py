with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
        # with comma, you can split the variables immediately into 2 in one line
        # Still need to use rstrip(), cause for function already adds it after each line


"""
More simple alternative:
    for line in file:
        row = line. rstrip().split(",")
        print(f"{row[O]} is in {row[1]}")
"""

"""
If you want to do changes, you need to open the file with "r",
extract all the information, let the file be closed again,
and then open it again with "w" and overwrite everything.
"""

"""
For larger files it might be quite slow.
In the future we will learn better practices.
"""
