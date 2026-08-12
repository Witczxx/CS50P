distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}


def main():
    for diztance in distances.values():
        print(f"{diztance} AU is {convert(diztance)} m")

def convert(au):
    return au *  149597870700


main()

"""
def main():
    for name in distances.keys():
        print(f"{name} is {distances[name]} AU from earth")
"""

