balance = 0


def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)

def deposit(n):
    global balance
    balance =+ n

def withdraw(n):
    global balance
    balance =- n

if __name__ == "__main__":
    main()

# Adding "global" at the Beginning of the Function solved the Problem.
# Now, the "balance" can be edited inside the Function.

# Don't create Local Variables with the same Name in a Function.
# They will shadow the Global Variable and create Bugs.
