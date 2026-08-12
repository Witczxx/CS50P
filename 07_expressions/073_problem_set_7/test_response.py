from response import validate


def test_validate():
    assert validate("malan@harvard.edu") == "Valid."
    assert validate("p@h.p") == "Valid."
    assert validate("donald@wb.xxxp") == "Valid."
    assert validate("malan@@@harvard.edu") == "Invalid."
    assert validate("here is malan@harvard.edu") == "Invalid."
    assert validate("patrick.witczak@web..de") == "Invalid."
    assert validate("asdfhjklasdfhjklasdfhjklasdfhjklasdfhjklasdfhjklasdfhjklsakdjasd;@web.de") == "Invalid."
    assert validate("patrick@asdfhjklasdfhjklasdfhjklasdfhjklasdfhjklasdfhjklasdfhjklsakdjasd;.de") == "Invalid."
    assert validate("patrick@web.asdfhjklasdfhjklasdfhjklasdfhjklasdfhjklasdfhjklasdfhjklsakdjasd;") == "Invalid."
