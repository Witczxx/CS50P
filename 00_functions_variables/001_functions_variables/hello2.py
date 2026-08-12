### how to define a parameter
### variable "name" was copied to "to"
def hello(to="world"):
    print("hello,", to)

### no variable - "world" is used
hello()

### output with variable
name = input("What's your name? ")
hello(name)
