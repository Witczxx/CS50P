from twttr import shorten


def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("aeiou") == ""
    assert shorten("3A1B2C") == "31B2C"
