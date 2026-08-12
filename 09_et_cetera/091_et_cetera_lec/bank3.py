class Account:
    def __init__(self):
        self._balance = 0

    # A Setter without a Getter is a Protector
    # Now we can not do inside of main() things like account.balance = 100 anymore.
    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n


def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("balance:", account.balance)


if __name__ == "__main__":
    main()

