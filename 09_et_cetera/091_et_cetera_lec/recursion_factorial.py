def factorial(n):
    # Base Case
    if n == 1:
        return 1

    # Recursive Call
    return n * factorial(n - 1)


result = factorial(3)

