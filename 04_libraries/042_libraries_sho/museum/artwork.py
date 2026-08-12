# In Combination with: search.py & artists.py

import requests

def get_artworks(query, limit):
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search", {"q": query}
        )
        response.raise_for_status()
    except HTTPError:
        return []
    
    content = response.json()
    return [artwork["title"] for artwork in content["data"]]