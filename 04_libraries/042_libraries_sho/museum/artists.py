# In Combination with: search.py & artwork.py

import requests

def get_artists(query, limit):
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artists/search", {"q": query}
        )
        response.raise_for_status()
    except HTTPError:
        return []
    
    content = response.json()
    return [artist["title"] for artist in content["data"]]