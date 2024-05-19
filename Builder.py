# Builder Interface
from abc import ABCMeta, abstractmethod

class IBuilder(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def build_part_a():
        "Build part a"

    @staticmethod
    @abstractmethod
    def build_part_b():
        "Build part b"

    @staticmethod
    @abstractmethod
    def build_part_c():
        "Build part c"

    @staticmethod
    @abstractmethod
    def get_result():
        "Return the final product"

# Concrete Builder
class Builder(IBuilder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        # Building part a
        self.product.parts.append('a')
        return self

    def build_part_b(self):
        # Building part b
        self.product.parts.append('b')
        return self

    def build_part_c(self):
        # Building part c
        self.product.parts.append('c')
        return self

    def get_result(self):
        # Getting the final product
        return self.product

# Product
class Product:
    def __init__(self):
        self.parts = []

# Director
class Director:
    @staticmethod
    def construct():
        # Constructing and returning the final product
        return Builder()\
            .build_part_a()\
            .build_part_b()\
            .build_part_c()\
            .get_result()

# Client
# Constructing the final product
PRODUCT = Director.construct()
print(PRODUCT.parts)
