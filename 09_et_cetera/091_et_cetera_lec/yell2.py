def main():
    yell("This", "is", "CS50")



def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)

if __name__ == "__main__":
    main()



# map is cool because it can automatically go through all words
# and apply this change.Remember that it needs a function in a class
