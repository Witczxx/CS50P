from plates import is_valid


def test_is_valid():
    assert is_valid("PA")
    assert is_valid("JY1234")
    assert is_valid("ADAD10")
    assert not is_valid("PA.123")
    assert not is_valid("P")
    assert not is_valid("PA12345")
    assert not is_valid("J2345")
    assert not is_valid("YJ0")
    assert not is_valid("YJ34P")


# Only Letters and Numbers - no dots or similar
# Minimum 2 letters
# Maximum 6 Letters
# Starting with 2 letters, no numbers
# No zeros as a first appearing number
# No letters appearing after first number appeared
