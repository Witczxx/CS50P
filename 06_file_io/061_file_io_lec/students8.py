# Completeley New

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students5.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"home": home, "name": name})
    # switching name and home is now problem, because the program is stable this way


# Writer quotes automatically so no mistakes happen
