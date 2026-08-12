# Further Improvements on how to use .groups()
# Special New Feature - if + variable defining at the same time
# By using the := Symbol

import re

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
