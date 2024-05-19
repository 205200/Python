# Open-Closed Principle (OCP)
# Classes should be open for extension but closed for modification.

class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass

    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        return 'roar'


class Mouse(Animal):
    def make_sound(self):
        return 'squeak'


class Snake(Animal):
    def make_sound(self):
        return 'hiss'


animals = [
    Lion('lion'),
    Mouse('mouse'),
    Snake('snake')
]


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animal_sound(animals)


# Now, animal_sound conforms to OCP by using polymorphism.

# Another example:

class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
        return self.price * 0.2


class VIPDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 2


class SuperVIPDiscount(VIPDiscount):
    def get_discount(self):
        return super().get_discount() * 2

# Now, discounts can be extended without modifying existing code.
