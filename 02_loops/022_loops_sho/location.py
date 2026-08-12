import sys
def main():
    coordinate_tuple = (42.376, -71.115)                # only adv - safe data - use if you know - you won't change
    coordinate_list = [42.376, -71.115]
    print(f"{sys.getsizeof(coordinate_tuple)} bytes")   # takes 56 bytes
    print(f"{sys.getsizeof(coordinate_list)} bytes")    # takes 72 bytes
main()

"""
def main():
    coordinates = (42.376, -71.115)
    coordinates[0] = -42.376           # Error - Values can't be changed!

main()
"""
"""
def main():
    coordinates = (42.376, -71.115)         # 2 Values in 1 Variable is called "Tuple"
    latitude, longitude = coordinates
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
main()
"""
"""
def main():
    coordinates = (42.376, -71.115)         # 2 Values in 1 Variable is called "Tuple"
    print(f"Latitude: {coordinates[0]}")
    print(f"Longitude: {coordinates[1]}")
main()
"""