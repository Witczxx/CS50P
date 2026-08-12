import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        num_1 = generate_integer(level)
        num_2 = generate_integer(level)
        correct = False
        for _ in range(3):
            answer = input(f"{num_1} + {num_2} = ")
            if is_int(answer) is True:
                if int(answer) == num_1 + num_2:
                    score = score + 1
                    correct = True
                    break
                else:
                    print("EEE")
            else:
                print("EEE")
        if correct is True:
            pass
        else:
            print(f"{num_1} + {num_2} = {num_1 + num_2}")
    print(f"Score: {score}")


def get_level():
    while True:
        lvl_input = input("Level: ")
        if is_int(lvl_input) is True:
            if 1 <= int(lvl_input) and int(lvl_input) <= 3:
                return int(lvl_input)
            else:
                pass
        else:
            pass


def generate_integer(level):
    if level == 1:
        return int(random.randint(0, 9))
    elif level == 2:
        return int(random.randint(10, 99))
    else:
        return int(random.randint(100, 999))


def is_int(s):
    try:
        int(s)
        return True
    except (ValueError, TypeError):
        return False


if __name__ == "__main__":
    main()
