import random

cards = ["jack", "queen", "king"]

def main():
    random.seed(1)          # can involve randomness, but make sure, the outcome stay the same
    print(random.choices(cards, weights=[75, 20, 10], k=2))     # simply try out to understand :D





main()