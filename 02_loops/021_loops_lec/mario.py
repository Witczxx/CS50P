def main():                                             ###  Print Vertical
    print_column(3)

def print_column(height):
    for _ in range(height):                             # Alternative: print("#\n") * height, end="")
        print("#")

main()


"""
for _ in range(3):
    print("#")
"""
"""
print("#")
print("#")
print("#")
"""