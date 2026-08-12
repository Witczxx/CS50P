import random

cards = ["jack", "queen", "king"]

def main():
    print(random.choices(cards, weights=[75, 20, 10], k=2))         # add weight to appear probabilities!





main()