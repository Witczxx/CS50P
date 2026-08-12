### def allows us to write code regardless of definition order.
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return(n * n)

main()