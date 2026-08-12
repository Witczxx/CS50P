# Right now our split() function does not allow regular expressions
# We can change this by adding a library

name = input("What's your name? ").strip()
if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"hello, {name}")
