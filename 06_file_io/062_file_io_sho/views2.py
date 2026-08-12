import csv

import numpy as np
from PIL import Image


def main():
    with open("views.csv", "r") as views, open("analysis.csv", "w") as analysis:
        reader = csv.DictReader(views)
        fieldnames_base = list(reader.fieldnames or [])
        fieldnames_var = fieldnames_base + ["brightness"]
        writer = csv.DictWriter(analysis, fieldnames=fieldnames_var)
        writer.writeheader()
        # give same header as views-file
        for row in reader:
            # Option 2
            row["brightness"] = round(
                calculate_brightness(f"pictures/{row['id']}.jpeg"), 2
            )
            writer.writerow(row)


def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness


main()
