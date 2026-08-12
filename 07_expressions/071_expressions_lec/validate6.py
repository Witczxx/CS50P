import re

email = input("What's your email? ").strip()

# \w is like the shortcut for a-zA-Z0-9_
# NEW: adding flags (e.g. to make .edu case-insensitive)
# NEW2: Grouping variables to allow multiple dots in Mail-Name: xyz@cs50.edu.cn


if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
