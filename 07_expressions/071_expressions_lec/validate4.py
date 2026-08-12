import re

email = input("What's your email? ").strip()

# [^@] = any character is ok excluding the @ sign
# ^ and $ make sure that only one string is accepted - nothing before and nothing behind

if re.search(r"^[^@]+@[^@]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
