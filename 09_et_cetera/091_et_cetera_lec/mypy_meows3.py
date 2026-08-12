def meow(n: int) -> str:
    '''
    Meow n times.

    :param n: Number of times to mew
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    '''
    return "meow\n" * n


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)

# Let's do some adjustments here
# To Eliminate our previous Error
# Because before we had no return in our def()
# So the Outcome was not a str()

# Get used to use '''xyz''' for Function Documentation.
# Later there are tools which allow you to create automatic Documentations
# Based on all things you wrote down using '''xyz'''
