def greet(input):
    if "hello" in input:
        return "hello there!"
    else:
        return "I don't know what you mean."


greeting = greet("hello computer")
print("Hm, " + greeting)

# While using the print function immediately, we have less variability
# A return falue saves the result instead of directly using it
# This allows us "saving" to do much more modification later - like here "Hm, ""