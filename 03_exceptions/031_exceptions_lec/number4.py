while True:  # Executing until the user makes the right input
    try:  # 'Best Practice' Solution
        x = int(
            input("What's x? ")
        )  # If I make a mistake - the program asks again for the correct input
    except ValueError:  # Until the input succeeds
        print("x is not an integer")
    else:
        break

print(
    f"collected names include {names}"
)  # If 'print()' is in 'else' : you would never break out of the loop
