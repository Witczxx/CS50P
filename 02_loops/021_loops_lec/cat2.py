while True:                                # "accidental" infinite loop
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")


"""
for _ in range(100):
    print("meow")
"""

# print("meow\n" * 3, end="")

"""
for _ in [0, 1, 2]:
    print("meow")
"""