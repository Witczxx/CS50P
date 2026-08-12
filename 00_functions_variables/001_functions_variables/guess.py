def get_guess():
    guess = int(input("What's your guess? "))
    return guess


def main():
    guess = get_guess()
    if guess == 50:
        print("Correct!")
    else:
        print("Incorrect!")


main()


### "guess =" exists in 2 functions - that's not a problem
### Because they are in different functions/scopes, it works like this
### 50 needs to be defined as an Integer first - otherway output is "incorrect!"