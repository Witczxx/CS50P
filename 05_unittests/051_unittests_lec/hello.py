def main():
    name = input("What's your name? ")
    print(hello(name))  # we put print() here to make the function editable


def hello(to="world"):  # makes sure that world is used in case there is no input
    return f"hello, {to}"  # using return instead of print() makes tings editable


if __name__ == "__main__":
    main()
