import re

email = input("What's your email? ").strip()

# making the .cs50.edu adding into the email optional
# Question Mark ? is saying: 0 or 1 repitition is both ok!

if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")



# Official Email Regular Expression:
#    ^[a-zA-Z0-9. !#$%&'*+\/=?^
#    {|}~-]+@[a-zA-Z0-9](?:[a-zA
#    -Z0-9-]{0,61} [a-zA-Z0-9])?(
#    ?: \.[a-zA-Z0-9](?:[a-zA-Z0-
#    9-1{0,61} [a-zA-Z0-9])?)*$
