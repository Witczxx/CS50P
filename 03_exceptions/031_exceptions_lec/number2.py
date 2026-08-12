try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")        # There's a function to catch "every" error, but "bad practice"

print (f"x is {x}")                     # NameError = x is not defined - error interrupted the whole process of defining 'x'    