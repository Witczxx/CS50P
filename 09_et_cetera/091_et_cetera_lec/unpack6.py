def f(*args, **kwargs):
    print("Named:", kwargs)


f(galleons=100, sickles=50, knuts=25)


# No matter how you change the tuple, the required input in f()
# is not completely variable
