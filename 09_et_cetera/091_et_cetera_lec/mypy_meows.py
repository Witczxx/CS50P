def meow(n: int):
    for _ in range(n):
        print("meow")


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)

# Here we are using "mypy" in the Terminal.
# It can help us to find out more about TypeErrors :)
# By adding ": type" behind Variables - We can help MyPy to help us
# So that it can better find out what the Problem is.

