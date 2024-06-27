"""Exercise 5

Write a class that will represent the magazine.
Storage capacity (float value reflecting cubic meters) is defined by the constructor.
Create a class that will reflect the product.
The product volume is defined by the constructor.
The magazine will have a method "add", which will take a Product object as its argument
and return the remaining free space, or -1 if you can't add a new item
since it won't fit in the warehouse anymore.

Use fixture to prepare a set of products that flow into warehouses every month and create tests
that will check whether warehouses respond correctly to adding more products.
Accuracy should be implemented to two decimal places.
"""


class Product:
    __volume = None

    def __init__(self, volume):
        self.volume = volume

    def __repr__(self):
        return f"Product(volume={self.volume})"

    def __str__(self):
        return f"product with volume: {self.volume}"

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        if volume <= 0:
            raise ValueError
        self.__volume = volume


class Magazine:
    __capacity = None
    __products = []

    def __init__(self, capacity):
        self.capacity = capacity
        self.__products = []

    def __repr__(self):
        return f"Magazine(capacity={self.capacity})"

    def __str__(self):
        return f"magazine with capacity: {self.capacity}"

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity <= 0:
            raise ValueError
        self.__capacity = capacity

    def add(self, product):
        self.__products.append(product)
        total_volume = sum([product.volume for product in self.__products])
        if self.capacity >= total_volume:
            return round(self.capacity - total_volume, 2)
        return -1

