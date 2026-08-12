import pytest
from bank import value


def test_value():
    assert value("hello") == "0$"
    assert value("hellau") == "20$"
    assert value("What's up?") == "100$"
    assert value("hellodidu") == "0$"


def test_no_value():
    with pytest.raises(IndexError):
        value("")
