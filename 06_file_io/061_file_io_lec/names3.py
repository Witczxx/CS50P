with open("names.txt", "r") as file:
    lines = file.readlines()  # reading all the lines of the file, and returning them as a list - each line - list element
    # actually you can skip this by putting the code below simply into the "with" command block

for line in lines:
    print(
        "Hello, ", line.rstrip()
    )  # otherway: extra space lines - bc \n done before -- you could also use end=""


# "r" means reading - let's you access the content of a file
