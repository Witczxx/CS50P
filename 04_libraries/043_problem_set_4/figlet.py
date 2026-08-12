import random
import subprocess  # new - allows to put sys.argv into script
import sys

import pyfiglet  # pip3 install pyfiglet

# Capture A List with All Fonts For Randomization in def font_input()
fonts_captured = subprocess.run(
    ["pyfiglet", "-l"], capture_output=True, text=True
).stdout
fonts_database = fonts_captured.split("\n")


def main():
    font_style = font_input()
    raw_text = input("Input: ")
    converted_text = pyfiglet.figlet_format(raw_text, font=font_style)
    print(converted_text)


def font_input():
    if len(sys.argv) == 1:
        return random.choice(fonts_database)  # From Captured font lit
    elif sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in fonts_database:
            return sys.argv[2]
        else:
            sys.exit("Font not in Database")
    else:
        sys.exit("System-Argument not recognized.")


main()
