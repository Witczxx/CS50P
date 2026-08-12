import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = '\"https?://www.youtube.com/embed/([a-zA-Z0-9]+)\"'
    match = re.search(pattern, s)
    if match:
        return f"https://youtu.be/{match.group(1)}"
    else:
        return None


if __name__ == "__main__":
    main()

# Expect that any such URL will be in one of the formats below.
# Assume that the value of src will be surrounded by double quotes.
# And assume that the input will contain no more than one such URL.
# If the input does not contain any such URL at all, return None.
#
# http://www.youtube.com/embed/xvFZjo5PgG0
# https://www.youtube.com/embed/xvFZjo5PgG0
# https://cs50.harvard.edu/python
