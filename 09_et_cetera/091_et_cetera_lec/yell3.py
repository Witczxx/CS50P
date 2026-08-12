def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)

if __name__ == "__main__":
    main()


# Using map() is perfectly fine, but we should still know the alternatives
# Very popular in Python - called "List Comprehension"

