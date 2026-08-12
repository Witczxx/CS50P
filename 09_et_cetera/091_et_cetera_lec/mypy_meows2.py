def meow(n: int) -> None:
    for _ in range(n):
        print("meow")


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")

# ERROR - CODE IS NOT WORKING HERE

# Check how in Line 1 we have "-> None"
# This is a "hint", where we can write the expected Outcome
# MyPy can use "->" for further Analysis
# And indeed: He found a mistake here
# MyPy sees that the Outcome is None
# But it is treated as a ": str". 
# This does not work together.
