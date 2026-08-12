import sys

file = []


def main():
    script = read_input()
    edit_input(script)  # puts it into file
    print(len(file))


def read_input():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit()
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit()
    elif sys.argv[1][-3:] != ".py":
        print("Not a python file")
        sys.exit()
    else:
        try:
            with open(f"{sys.argv[1]}", "r") as script:
                script = script.readlines()
                return script
        except FileNotFoundError:
            print("File does not exist.")
            sys.exit()


def edit_input(s):
    for line in s:
        line = line.replace("\n", "")
        line = line.replace(" ", "")
        if line == "":
            continue
        elif line[0] == "#":
            continue
        else:
            file.append(line)


if __name__ == "__main__":
    main()
