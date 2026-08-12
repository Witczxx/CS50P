distances = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80 AU",
    "New Horizons": "58",
    "Pioneer 11": "44 AU"
}

def main():
    spacecraft = input("Enter a spacecraft: ")
    try:                                            # Also good for debugging
        au = float(distances[spacecraft])
    except ValueError:
        print(f"Can't convert '{distances[spacecraft]}' to a float")
        return
    except KeyError:
        print(f"Spacecraft '{spacecraft}' not in dictionary.")
        return

    m = convert(au)
    print(f"{m} m away")

def convert(au):
    return au * 14959870700

main()

