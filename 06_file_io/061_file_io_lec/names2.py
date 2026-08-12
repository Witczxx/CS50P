name = input("What's your name? ")

with open("names.txt", "a") as file:  # Best Practice
    file.write(f"{name}\n")


# "w" = write / overwrite - resetting the file
# "a" = append - adds and adds and adds
# if file does not exist, a new one will be created

# file = open("names.txt", "a") ///// file.close()
# not always smart - opening/closing automatically is better
# making you easily forget to close a file
# there are better practices
