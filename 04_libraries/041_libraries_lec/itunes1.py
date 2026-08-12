import requests             # Can pretend to be a Webbrowser 
import json                 # comes with python ; allows to illustrate json pretty
import sys

if len(sys.argv) != 2:
    sys.exit()

# sys.argv[1] lets us input the artist
# request.get prompts for the URL
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

# this URL is the search URL for itunes, giving back JSON files
# this JSOn file is adding return bars every second string it recognizes
print(json.dumps(response.json(), indent=2))