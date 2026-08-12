class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        self.size += n
        return self

    def withdraw(self, n):
        self.size -= n
        return self

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity or size < 0:
            raise ValueError("Size exceeded upper/lower limit")
        self._size = size


def main():
    jar = Jar(capacity=int(input("Capacity: ")))
    jar.deposit(3)
    jar.withdraw(1)
    print(jar)


if __name__ == "__main__":
    main()

