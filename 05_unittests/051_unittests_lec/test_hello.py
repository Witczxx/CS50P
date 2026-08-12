from hello import hello


def test_default():
    assert hello("David") == "hello, David"


def test_argument():
    assert hello() == "hello, world"


"""
Tests should be nice and simple.
We don't want them to be longer than our actual code.
"""
