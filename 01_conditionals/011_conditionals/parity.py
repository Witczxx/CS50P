def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return n % 2 == 0

"""
def is_even(n):
    return True if n % 2 == 0 else False

main()
"""

"""
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()
"""

# a boolean value can only be true or false - capitalized T or F.

"""
x = int(input("What's x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")
"""

"""
So % is saying, if something is even or not.
If it is even, the result is 0.
If it is odd, the result is 1.
"""