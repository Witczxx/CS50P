import sys

# Check for Errors
if len(sys.argv[1]) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv[1]) > 2:
    sys.exit("Too many arguments") # skipping the print function on bottom, exiting program

# Print Name Tags
print("Hello, my name is", sys.argv[1]) 