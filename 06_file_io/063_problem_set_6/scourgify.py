import csv
import sys


def main():
    csv_input = check_input()
    edited_input = csv_edit(csv_input)
    csv_writing(edited_input)


def check_input():
    if len(sys.argv) < 3:
        sys.exit("Too few command_line arguments.")
    elif len(sys.argv) > 3:
        sys.exit("Too many command_line arguments.")
    else:
        try:
            return csv_read()
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")


def csv_read():
    output = []
    with open(sys.argv[1], "r", newline="", encoding="utf-8") as before:
        raw_data = csv.reader(before)
        for row in raw_data:
            output.append(row)
        return output


def csv_edit(s):
    output = []
    output.append(["First", "Last", "House"])
    for row in s[1:]:
        last_first = row[0].split(",")
        last = last_first[0].strip()
        first = last_first[1].strip()
        house = row[1].strip()
        output.append([first, last, house])
    return output


def csv_writing(d):
    with open(sys.argv[2], "w", newline="", encoding="utf-8") as f:
        output = csv.writer(f)
        for row in d:
            output.writerow(row)


if __name__ == "__main__":
    main()
