def f(*args, **kwargs):
    print("Positional:", args)



f(100, 50, 25, 5)


# No matter how you change the tuple, the required input in f()
# is not completely variable
