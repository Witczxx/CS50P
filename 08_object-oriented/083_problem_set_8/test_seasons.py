from seasons import Birthday
import datetime as dt

def test_Birthday():
    bday1 = Birthday("1998-05-27").date_dif().convert_to_words()
    assert  str(bday1) == "fourteen million, eight hundred thirty-three thousand, four hundred forty minutes"
    bday2 = Birthday("2000-01-01").date_dif().convert_to_words()
    assert  str(bday2) == "thirteen million, nine hundred ninety-two thousand, four hundred eighty minutes"
    today = dt.date.today()
    year_dif1 = dt.date(year=today.year - 1, month=today.month, day=today.day)
    bday3 = Birthday(str(year_dif1)).date_dif().convert_to_words()
    assert str(bday3) == "five hundred twenty-five thousand, six hundred minutes" or str(bday3) == "five hundred twenty-seven thousand forty minutes"
    year_dif2 = dt.date(year=today.year - 2, month=today.month, day=today.day)
    bday4 = Birthday(str(year_dif2)).date_dif().convert_to_words()
    assert str(bday4) == "one million, fifty-one thousand, two hundred minutes" or str(bday4) == "one million, fifty-two thousand, six hundred forty minutes"
