
def main():
    if 7.00 <= convert(time) <= 8.00:
        return "Breakfast Time"
    elif 12.00 <= convert(time) <= 13.00:
        return "Lunch Time"
    elif 18.00 <= convert(time) <= 19.00:
        return "Dinner Time"
    else:
        return


def convert(s):
    minutes = float(s[-2:]) /60
    if len(s) == 4:
        return float(s[0]) + minutes
    else:
        return float(s[:2]) + minutes


time = input("What time is it? ")
print(main())