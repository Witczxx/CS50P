import csv
import sys

from tabulate import tabulate

table_list = []


def main():
    check_input()
    print(tabulate(table_list[1:], table_list[0], tablefmt="grid"))


def check_input():
    if len(sys.argv) < 2:
        print("Too few command-line arguments.")
        sys.exit()
    elif len(sys.argv) > 2:
        print("too many command-line arguments.")
        sys.exit()
    elif sys.argv[1][-4:] != ".csv":
        print("Not a CSV file.")
        sys.exit()
    else:
        try:
            with open(f"{sys.argv[1]}", "r") as sicilian:
                read_sicilian = csv.reader(sicilian)
                for row in read_sicilian:
                    table_list.append(row)
        except FileNotFoundError:
            print("File does not exist.")
            sys.exit()


if __name__ == "__main__":
    main()
