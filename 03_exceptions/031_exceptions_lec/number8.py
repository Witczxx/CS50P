def main():
    x = get_int("What's x? ")       # Making code more reusable
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))  # int() doesn't have to know anymore, what has been asked for 
            return x
        except ValueError:
            pass


main()