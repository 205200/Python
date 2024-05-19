# Singleton Class
import copy

class Singleton:
    "The Singleton Class"
    value = []  # Static variable

    def __new__(cls):
        # Override the __new__ method to return a reference to itself
        return cls

    @staticmethod
    def static_method():
        "Use @staticmethod if no inner variables required"

    @classmethod
    def class_method(cls):
        "Use @classmethod to access class-level variables"
        print(cls.value)

# Client
# All uses of the singleton point to the same memory address (id)
print(f"id(Singleton)\t= {id(Singleton)}")

# Creating instances of the singleton
OBJECT1 = Singleton()
print(f"id(OBJECT1)\t= {id(OBJECT1)}")

# Deep copying OBJECT1
OBJECT2 = copy.deepcopy(OBJECT1)
print(f"id(OBJECT2)\t= {id(OBJECT2)}")

# Creating another instance of the singleton
OBJECT3 = Singleton()
print(f"id(OBJECT3)\t= {id(OBJECT3)}")
