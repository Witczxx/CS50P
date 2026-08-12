def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    flock = []
    for i in range(n):
        flock.append("Sheep" * i)
    return flock


if __name__ == "__main__":
    main()

# This solution is also good working but
# For 10,000 Sheeps this is starting to become slow
# There might be Solutions with better Performance.
