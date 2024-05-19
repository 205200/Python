# Liskov Substitution Principle (LSP)
# Subclasses should be substitutable for their superclasses without causing errors.

class Animal:
    def leg_count(self):
        pass

class Lion(Animal):
    def leg_count(self):
        return 4

class Mouse(Animal):
    def leg_count(self):
        return 4

class Pigeon(Animal):
    def leg_count(self):
        return 2

animals = [
    Lion(),
    Mouse(),
    Pigeon()
]

def animal_leg_count(animals: list):
    for animal in animals:
        print(animal.leg_count())

animal_leg_count(animals)

# The animal_leg_count function now conforms to the LSP principle.
# It works with any Animal type and doesn't need to check the type of each animal.
