import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
    print("Username: ", matches.group(1))

# compared to re.sub(), nothing gets printed, when twitter.com is not found
# because re.search() makes sure that something needs to be found
# unless you use (?...), the group(1) place will be occupied by www.
# and it doesn't matter if www. exists or not, it will be reserved
