# Completeley New

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students4.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])


# Writer quotes automatically so no mistakes happen
