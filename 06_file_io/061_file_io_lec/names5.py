names = []

with open("names.txt") as file:  # you don't need "r", because this is the default! :D
    for line in file:  # He is automatically doing readlines() :D
        names.append(line.rstrip())
    # Compromiss of names3 and names4
    # Don't directly put the output into the "with" block.
    # Do the extraction, and continue in a new block :)

for name in sorted(names):
    print(f"Hello, {name}")


"""
### This here is also possible:
    with open("names.txt") as file:
        for line in sorted(file):
            print("Hello,", line.strip())
### But not as flexible for later editing.
"""
