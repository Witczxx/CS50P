MEOWS = 3

for _ in range(MEOWS):
    print("meow")


# ----------------------------------------------


class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

cat = Cat()
cat.meow()

# 2 different Possibilities of how to make better Syntax
# Don't just randomly do for _ in range(3)
# Because later it might be messy and not understandable, where the 3 comes from
