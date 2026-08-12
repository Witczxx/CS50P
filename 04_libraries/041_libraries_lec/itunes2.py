import sys

import requests

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]
)  # Song-Limit in URL

# He recognized the JSON structure
# having a dictionary with "results" as a key - linked to a list
# inside this list there is ""are multiple dictionares"" with the key "trackname"
# We just limited to 1 song, so it's just 1 dictionary right now, but we can change that
o = response.json()
for result in o["results"]:
    print(result["trackName"])
