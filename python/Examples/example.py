from abc import ABC, abstractmethod

# Common types in Python

# Integer
my_int = 10
print(f"Integer: {my_int}")

# Float
my_float = 10.5
print(f"Float: {my_float}")

# String
my_string = "Hello, world!"
print(f"String: {my_string}")

# Boolean
my_bool = True
print(f"Boolean: {my_bool}")

# List
my_list = [1, 2, 3, 4, 5]
print(f"List: {my_list}")

# Tuple
my_tuple = (1, 2, 3, 4, 5)
print(f"Tuple: {my_tuple}")

# Set
my_set = {1, 2, 3, 4, 5}
print(f"Set: {my_set}")

# Dictionary
my_dict = {"name": "Alice", "age": 25}
print(f"Dictionary: {my_dict}")

# NoneType
my_none = None
print(f"NoneType: {my_none}")

# Class in Python

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return f"{self.name} says hello!"

# Creating an instance of the class
my_animal = Animal("Buddy", "Dog")
print(f"Animal: {my_animal.name}, Species: {my_animal.species}, Speak: {my_animal.speak()}")

# Interface using an abstract base class
class AnimalInterface(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass

# Inheritance with interface implementation
class Dog(Animal, AnimalInterface):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    # Additional constructor using @classmethod
    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['breed'])

    def speak(self):
        return f"{self.name} says woof!"

    def move(self):
        return f"{self.name} runs quickly!"

    def bark(self):
        return f"{self.name} barks!"

# Creating an instance of the subclass
my_dog = Dog("Buddy", "Golden Retriever")
print(f"Dog: {my_dog.name}, Breed: {my_dog.breed}, Speak: {my_dog.speak()}, Bark: {my_dog.bark()}, Move: {my_dog.move()}")

# Creating an instance of Dog using the additional constructor
dog_data = {'name': 'Max', 'breed': 'Labrador'}
my_other_dog = Dog.from_dict(dog_data)
print(f"Dog: {my_other_dog.name}, Breed: {my_other_dog.breed}, Speak: {my_other_dog.speak()}, Bark: {my_other_dog.bark()}, Move: {my_other_dog.move()}")

# Another class implementing the interface
class Bird(AnimalInterface):
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return f"{self.name} says tweet!"

    def move(self):
        return f"{self.name} flies high!"

# Creating instances of Bird
my_bird = Bird("Tweety", "Canary")
print(f"Bird: {my_bird.name}, Species: {my_bird.species}, Speak: {my_bird.speak()}, Move: {my_bird.move()}")

# Class with a class method
class MathOperations:
    @classmethod
    def add(cls, a, b):
        return a + b

# Using the class method
result = MathOperations.add(5, 3)
print(f"Addition result: {result}")

# Class with a static method
class Utility:
    @staticmethod
    def is_even(number):
        return number % 2 == 0

# Using the static method
print(f"Is 4 even? {Utility.is_even(4)}")
print(f"Is 7 even? {Utility.is_even(7)}")
