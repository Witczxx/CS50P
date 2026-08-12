# Classes can help us to keep information without having to worry too much about keeping consistency about an order
# like here in this example where you have to be so careful: packages = ["Package 1: Alice to Bob, 10kg", "Package 2: Bob to Charlie, 5kg"]

class Package:
    def __init__(self, number, sender, recipient, weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight



def main():
    packages = [
        Package(number=1, sender="Alice", recipient="Bob", weight=10),
        Package(number=2, sender="Bob", recipient="Alice", weight=5)
    ]
    print(packages)

main()
