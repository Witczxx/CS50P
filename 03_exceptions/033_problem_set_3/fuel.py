def main():
    fraction = get_numbers("Fraction: ")
    percentage = division(fraction)
    give_answer(percentage)


def get_numbers(d):
        while True:
            try:
                raw_fraction = input(d)
                x = int(raw_fraction[0])
                y = int(raw_fraction[2])
                if not raw_fraction[1] == "/":
                    raise ValueError
                elif x < 0 or x > 4:
                    raise ValueError
                elif y <= 0 or y > 4:
                    raise ValueError
                else:
                    return raw_fraction
            except ValueError:
                pass
            except IndexError:
                pass


def division(s):
    result = (int(s[0]) / int(s[2])) * 100
    rounded_result = round(result)
    return rounded_result


def give_answer(c):
    if c <= 1:
        print("E")
    elif c >= 99:
        print("F")
    else:
        print(f"{c}%")


main()