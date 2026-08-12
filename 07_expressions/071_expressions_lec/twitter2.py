# re.sub(pattern, repl, string) means substitute
# Recommendation: Don't do everything at once
# Add one RE at a time, do a check-up, and continue, and do another check-up
# And this way even your complicated regular expressions should be 成功

import re

url = input("URL: ").strip()
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")


# re.sub is good, but it doens't exclude completely wrong inputs
# so let's go back to re.search() in the next file
