import pytest
from calculator import square


def main():
    test_positive()
    test_negative()
    test_zero()
    test_str()


# By dividing pytest was more accurate -> 2 tests failed, 1 test passed
def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


# Let's pass the TypeError for Pytest for the case "cat".
def test_str():
    with pytest.raises(TypeError):
        square("cat")


if __name__ == "__main__":
    main()
