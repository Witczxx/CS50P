def main():
    first_input = input("Fraction: ")
    fraction = get_numbers(first_input)
    print(division(fraction))


def get_numbers(raw_fraction):
    while True:
        try:
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
            break
        except IndexError:
            break


def division(s):
    result = (int(s[0]) / int(s[2])) * 100
    rounded_result = round(result)
    if rounded_result <= 1:
        return "E"
    elif rounded_result >= 99:
        return "F"
    else:
        return f"{rounded_result}%"


if __name__ == "__main__":
    main()
