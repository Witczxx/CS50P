def main():
    print(validate(input("What is your E-Mail Adress? ")))


def validate(s):
    valid_letters = "#$%&'*+/=?^_`|~-"

    name = ""
    provider = ""
    address = ""
    identifier = ""

    # Splitting
    try:
        name, provider = s.split("@")
    except ValueError:
        return "Invalid."

    try:
        address, identifier = provider.split(".")
    except ValueError:
        return "Invalid."

    # Editing Provider
    for letter in name:
        if not (letter in valid_letters or letter.isalnum()):
            return "Invalid."

    # Editing Address
    if not (len(address) <= 62 and len(address) >= 1):
        return "Invalid."
    for letter in address:
        if not letter.isalnum():
            return "Invalid."

    # Editing Identifier
    if not (len(identifier) <= 62 and len(identifier) >= 1):
        return "Invalid."
    for letter in identifier:
        if not letter.isalnum():
            return "Invalid."

    # Evaluation Complete!
    return "Valid."


if __name__ == "__main__":
    main()
