from fuel import division, get_numbers


def test_get_numbers():
    assert get_numbers("1/4")
    assert get_numbers("2/3")
    assert get_numbers("0/4")
    assert get_numbers("4/4")
    assert not get_numbers("4/5")
    assert not get_numbers("11/2")


def test_division():
    assert division("3/4") == "75%"
    assert division("4/4") == "F"
    assert division("0/4") == "E"
    assert division("1/2") == "50%"
    assert division("1/3") == "33%"
    assert not division("1/4") == "50%"
