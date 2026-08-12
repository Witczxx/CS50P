# If we do not add any specific symbol behind the parenthesis
# It indicates that we use the parenthesis as "capturing mode" for our variable

import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    last, first = matches.groups()
    name = f"{first} {last}"
print(f"hello, {name}")
