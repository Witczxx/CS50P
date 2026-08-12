balance = 0


def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)

def deposit(n):
    balance =+ n

def withdraw(n):
    balance =- n

if __name__ == "__main__":
    main()

# We have here this Issue that the Global Variable "balance" is not changing
# This is because Global Variables can not be changed in Functions.
# So the printed Blanace shows "0" twice.
# deposit() and withdraw() show no Functionality.
# If we put "Balance" into main(), we will also have an Error.
# Because other Functions can not access main().
