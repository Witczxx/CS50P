from numb3rs import validate


def test_validate():
    assert validate("0.0.0.0") == "True."
    assert validate("255.255.255.255") == "True."
    assert validate("099.099.099.099") == "True."
    assert validate("199.199.199.199") == "True."
    assert validate("123.145.167.189") == "True."
    assert validate("256.0.0.0") == "False."
    assert validate("0.256.0.0") == "False."
    assert validate("0.0.256.0") == "False."
    assert validate("0.0.0.256") == "False."
    assert validate("1111.0.0.0") == "False."
    assert validate("0.0.0.1111") == "False."
    assert validate("0000.0.0.0") == "False."
    assert validate("0.0.0.0000") == "False."
