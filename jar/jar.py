class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if (n+self.size) > self.capacity:
            raise ValueError("Size Exceeds Capacity")
        else:
            self.size = n+self.size

    def withdraw(self, n):
        if (self.size-n) < 0:
            raise ValueError("Not many cookies!")
        else:
            self.size = self.size-n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Invalid Capacity")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity or size < 0:
            raise ValueError("Invalid size")
        else:
            self._size = size

def main():
    jar=Jar()
    jar.deposit(2)
    jar.withdraw(1)
    print(jar)

if __name__ == "__main__":
    main()