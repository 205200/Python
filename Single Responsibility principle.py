# Single Responsibility Principle (SRP)
# A class should have only one responsibility.

class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass

    def save(self, animal: Animal):
        pass


# The Animal class violates SRP by handling both properties and database management.

class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        pass


class AnimalDB:
    def get_animal(self) -> Animal:
        pass

    def save(self, animal: Animal):
        pass

# Separate classes for animal properties and database management to conform to SRP.
