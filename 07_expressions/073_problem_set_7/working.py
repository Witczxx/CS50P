import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    #Splitting the Regular Expression
    ph1 = "(?P<h1>[0-9]{1,2})"
    ph2 = "(?P<h2>[0-9]{1,2})"
    pm1 = "(?::(?P<m1>[0-9]{1,2}))?"
    pm2 = "(?::(?P<m2>[0-9]{1,2}))?"
    pap1 = "(?P<ap1>AM|PM)"
    pap2 = "(?P<ap2>AM|PM)"
    pattern = f"{ph1}{pm1} {pap1} to {ph2}{pm2} {pap2}"
    if match := re.search(pattern, s):
        # Checking and Editing Hours on Both Sides:
        h1 = check_hours(match.group("h1"))
        h2 = check_hours(match.group("h2"))
        if match.group("ap1") == "PM": h1 = int(h1) + 12
        if match.group("ap2") == "PM": h2 = int(h2) + 12
        if len(str(h1)) == 1: h1 = f"0{h1}"
        if len(str(h2)) == 1: h2 = f"0{h2}"
        # Checking and Editing Minutes on Both Sides:
        m1 = "00"
        m2 = "00"
        if match.group("m1") != None:
            m1 = check_conv_minutes(match.group("m1"))
        if match.group("m2") != None:
            m2 = check_conv_minutes(match.group("m2"))
        # Final Return Function
        return f"{h1}:{m1} to {h2}:{m2}"
    else:
        raise ValueError


def check_hours(s):
    if int(s) <= 12:
        return s
    else:
        raise ValueError


def check_conv_minutes(s):
    if int(s) < 60:
        return s
    else:
        raise ValueError


if __name__ == "__main__":
    main()


# expects a str in any of the 12-hour formats below
# and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00)
#
# 9:00 AM to 5:00 PM
# 9 AM to 5 PM
# 9:00 AM to 5 PM
# 9 AM to 5:00 PM
#
# Expect that AM and PM will be capitalized (with no periods therein)
# and that there will be a space before each
#
# Assume that these times are representative of actual times,
# not necessarily 9:00 AM and 5:00 PM specifically.
#
# Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid
# (e.g., 12:60 AM, 13:00 PM, etc.).
#
# someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM)
