try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:                               # NameError is skipped, if the the input is sth like 'cat'
    print (f"x is {x}")

