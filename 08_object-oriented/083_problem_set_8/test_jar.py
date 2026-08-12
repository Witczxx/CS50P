from jar import Jar
import pytest

def test_Jar():
    assert str(Jar().deposit(5).withdraw(2)) == "🍪🍪🍪"
    assert str(Jar(5).deposit(5).withdraw(1)) == "🍪🍪🍪🍪" 
    assert str(Jar(1).deposit(1)) == "🍪"

def test_no_Jar():
    with pytest.raises(ValueError):
        str(Jar().withdraw(1))
    with pytest.raises(ValueError):
        str(Jar().deposit(13))
    with pytest.raises(ValueError):
        str(Jar(20).deposit(1).withdraw(2))
