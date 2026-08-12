import sys

if len(sys.argv[1]) < 2:
    sys.exit("Too few arguments")


# sys.argv can be used in "for loops"
for arg in sys.argv[1:]:                # called "slicing" / "slice"
    print("Hello, my name is", arg)     # [1:-1] is possible! D:

