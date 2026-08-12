from calculator import square


def main():
    test_square()


def test_square():
    if square(2) != 4:
        print("2 square was not 4.")
    if square(3) != 9:
        print(
            "3 square was not 9."
        )  # more user-friendly compared to v2 - printing a user-message


if __name__ == "__main__":
    main()
