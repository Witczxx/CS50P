def main():                             # The "program" is broken down into 3 lines of code, by a defined function
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:                               # You can also put 'return' right before 'int(input())' ! - Both ways ok 
            x = int(input("What's x? "))   # Return is like "Break + Return" -> you can skip break by using return
            return x                       # Once you define a function, you need 'return' to return a value
        except ValueError:
            print("x is not an integer")


main()