from calculator import square


def main():
    test_square()


def test_square():
    try:
        assert square(3) == 9  # try is giving us same result as V1 BUT multiple errors!
    except AssertionError:
        print("3 squared was not 9")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared was not 9")


if __name__ == "__main__":
    main()
