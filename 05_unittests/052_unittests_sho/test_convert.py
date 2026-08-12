import pytest
from convert import convert


# we count by function, even though multiple tests run through
def test_int_convert():
    assert convert(1) == 149597870700
    assert convert(50) == 7479893535000


# make sure everything starts with test_
def test_error():
    with pytest.raises(TypeError):
        convert("1")


# makes a test for floats (infinite numbers after dot) with some tolerance that we can set)
def test_float_conversion():
    assert convert(0.001) == pytest.approx(149597870.691, abs=1e-2)
