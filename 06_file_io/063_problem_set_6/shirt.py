import sys

from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments.")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments.")
    elif sys.argv[1][-4:].lower() != sys.argv[2][-4:].lower():
        sys.exit("Input and Output have different extensions.")
    elif (
        sys.argv[1][-4:].lower() != ".png"
        and sys.argv[1][-4:].lower() != ".jpg"
        and sys.argv[1][-4:].lower() != ".jpeg"
    ):
        sys.exit("Invalid Input")
    elif (
        sys.argv[2][-4:].lower() != ".png"
        and sys.argv[2][-4:].lower() != ".jpg"
        and sys.argv[2][-4:].lower() != ".jpeg"
    ):
        sys.exit("Invalid Output")
    else:
        try:
            add_shirt()
        except FileNotFoundError:
            sys.exit("Input does not exist.")


def add_shirt():
    shirt = Image.open("shirt.png")
    person = Image.open(sys.argv[1])
    shirt_new_size = ImageOps.fit(shirt, person.size)
    person_with_shirt = person.copy()
    # doubling name below = activating alpha canal
    person_with_shirt.paste(shirt_new_size, shirt_new_size)
    person_with_shirt.save(sys.argv[2])


if __name__ == "__main__":
    main()
