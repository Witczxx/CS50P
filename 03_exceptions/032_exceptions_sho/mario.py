def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        # print(i, end="") [Bugfix] is a good solution to check - what is the variable doing ?
        print("#" * (i + 1))

if __name__ == "__main__":              # Making the file safe while being imported
    main()