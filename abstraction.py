from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        """Abstract method to define sound of the animal."""
        pass

# Derived class: Dog
class Dog(Animal):
    def sound(self):
        return "Bark"

# Derived class: Cat
class Cat(Animal):
    def sound(self):
        return "Meow"

# Using the classes
dog = Dog()
print("Dog sound:", dog.sound())

cat = Cat()
print("Cat sound:", cat.sound())
