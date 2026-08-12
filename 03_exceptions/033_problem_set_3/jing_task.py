
### Introduction
print("Scissors Stone Paper Game")

### Shortcuts for Scissors, Stone and Paper
sc = "Scissors"
st = "Stone"
pa = "Paper"


def main():

    p1 = input("Player 1 - Turn: ")     # Input of Player 1 
    p2 = input("Player 2 - Turn: ")     # Input of Player 2
    winner = check_inputs(p1, p2)
    print(winner)


def check_inputs(s, d):

    if s == d:
        return "We have a draft."
    elif (s == sc and d == pa) or (s == st and d == sc) or (s == pa and d == st):
        return "Player 1 wins."
    else:
        return "Player 2 wins."


main()