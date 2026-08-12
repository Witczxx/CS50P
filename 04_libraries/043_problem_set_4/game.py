import random


def main():
    level = get_level()
    guess = get_guess()
    result = random.randint(0, level)
    if result == guess:
        print("Just right!")
    elif result > guess:
        print("Too small!")
    else:
        print("Too large!")


def get_level():
    while True:
        level = input("Level: ")
        if is_int(level) is True:
            if int(level) >= 1:
                return int(level)
            else:
                pass
        else:
            pass


def get_guess():
    while True:
        guess = input("Guess: ")
        if is_int(guess) is True:
            if int(guess) >= 1:
                return int(guess)
            else:
                pass


def is_int(b):
    try:
        int(b)
        return True
    except (ValueError, TypeError):
        return False


main()
