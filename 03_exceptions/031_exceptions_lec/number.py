x = int(input("What's x? "))    # if you don't write a number, you get a "ValueError"
print (f"x is {x}")             # "invalid literal" for int() = sth typed in for int()
                                # program defensively = assume users want to crash your program
                                # keywords "try" and "except" can be used for it 
