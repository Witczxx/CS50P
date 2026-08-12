import re


# strip() only removes border whitespaces
email = input("What's your email? ").strip()

# . says - there must be any character before and after
# + says - it must appear at least once
# Alternative: using "..*"

if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

# The * is consuming one character less than the +
# So it seems like using .* is here the more efficient practice
