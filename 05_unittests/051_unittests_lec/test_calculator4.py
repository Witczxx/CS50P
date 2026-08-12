from calculator import square


def main():
    test_square()


# pytest test_calculator4.py is super good -> showed you that square(3) == 6 :D
def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0


if __name__ == "__main__":
    main()
