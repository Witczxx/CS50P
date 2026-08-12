def main():
    camelcase = input("camelCase: ")
    snakecase = convert(camelcase)
    print(f"snake_case: {snakecase}")

def convert(case):
    smallalpha = "abcdefghijklmnopqrstuvwxyz"
    bigalpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for letter in range(len(smallalpha)):
        convertcase = case.replace(bigalpha[letter], "_" + smallalpha[letter])
        case = convertcase
    
    return case

main()
