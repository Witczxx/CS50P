# In Combination with: artists.py & artwork.py

from museum.artwork import get_artworks     # how to make a package
from museum.artists import get_artists      # how to use a package

def main():
    artwork = input("Artwork: ")
    artworks = get_artworks(query=artwork, limit=3)
    for artwork in artworks:
        print(f"* {artwork}")

    artist = input("Artist: ")
    artists = get_artists(query=artist, limit=3)
    for artist in artists:
        print(f"* {artist}")

main()