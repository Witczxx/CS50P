import datetime as dt

from seasons import BirthdayCounter


def test_BirthdayCounter():
    today = dt.datetime.now(dt.timezone.utc).date()

    yto, mto, dto = str(today).split("-")
    last_year = dt.date(year=(int(yto)-1), month=int(mto), day=int(dto))
    output_last_year = BirthdayCounter(bday_str=str(last_year))
    assert str(output_last_year)  == "five hundred twenty-five thousand, six hundred minutes." or str(output_last_year) == "five hundred twenty-seven thousand forty minutes"

    two_years_ago = dt.date(year=(int(yto)-2), month=int(mto), day=int(dto))
    output_two_years_ago = BirthdayCounter(bday_str=str(two_years_ago))
    assert str(output_two_years_ago)  == "one million, fifty-one thousand, two hundred minutes." or str(output_two_years_ago) == "one million, fifty-two thousand, six hundred forty minutes."
