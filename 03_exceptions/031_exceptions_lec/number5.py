while True:
    try:
        x = int(input("What's x? "))
        break                           # you can shorten '1' line of code
    except ValueError:
        print("x is not an integer")

print(f"x is {x}")