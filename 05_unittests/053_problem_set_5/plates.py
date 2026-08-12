from numpy.ma.core import true_divide


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    check_a = alpha_num(s)  # Only Letters and Numbers - no dots or similar

    if check_a:
        pass
    else:
        return False

    check_b = min_two_letters(s)  # Minimum 2 letters

    if check_b:
        pass
    else:
        return False

    check_c = max_six_letters(s)  # Maximum 6 Letters

    if check_c:
        pass
    else:
        return False

    check_d = start_w_letters(s)  # Starting with 2 letters, no numbers

    if check_d:
        pass
    else:
        return False

    check_e = no_0_start(s)  # No zeros as a first appearing number

    if check_e:
        pass
    else:
        return False

    check_f = no_alpha_num_mix(s)  # No letters appearing after first number appeared

    if check_f:
        return True
    else:
        return False


def alpha_num(s):  # A # # Only Letters and Numbers - no dots or similar
    if s.isalnum():
        return True
    else:
        return False


def min_two_letters(s):  # B # Minimum 2 letters
    if len(s) >= 2:
        return True
    else:
        return False


def max_six_letters(s):  # C # Maximum 6 Letters
    if len(s) <= 6:
        return True
    else:
        return False


def start_w_letters(s):  # D  # Starting with 2 letters, no numbers
    if s[0].isalpha() and s[1].isalpha():
        return True
    else:
        return False


def no_0_start(s):  # E # No zeros as a first appearing number
    if len(s) > 2:
        if s[2] == "0":
            return False
        else:
            for n in range(len(s[3:4])):
                n = n + 3
                if s[n].isalpha() and int(s[n + 1]) == 0:
                    return False
        return True
    else:
        return True


def no_alpha_num_mix(s):  # F      # No letters appearing after first number appeared

    if len(s) > 2:
        if s[2].isdigit() and s[3:].isalpha():
            return False
        else:
            for n in range(len(s[3:])):
                n = n + 3
                if s[2:n].isdigit() and s[(n + 1) :].isalpha():
                    return False
                else:
                    pass
            return True
    else:
        return True


if __name__ == "__main__":
    main()
