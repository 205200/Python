# Classes implementing the IProduct interface
class ConcreteProductA:
    def __init__(self):
        self.name = "ConcreteProductA"

class ConcreteProductB:
    def __init__(self):
        self.name = "ConcreteProductB"

class ConcreteProductC:
    def __init__(self):
        self.name = "ConcreteProductC"

# The Factory Class
class Creator:
    # Static method to create a concrete product based on some property
    @staticmethod
    def create_object(some_property):
        if some_property == 'a':
            return ConcreteProductA()
        if some_property == 'b':
            return ConcreteProductB()
        if some_property == 'c':
            return ConcreteProductC()
        return None

# The Client
# Creating a concrete product 'b' using the factory method
PRODUCT = Creator.create_object('b')
print(PRODUCT.name)
