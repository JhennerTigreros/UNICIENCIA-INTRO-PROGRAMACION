# Polymorphism in Python
# Polymorphism allows methods to be used interchangeably between different classes that share a common base class or interface.

class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Polymorphic function
def animal_sound(animal):
    # This function can take any object that implements the speak method
    print(animal.speak())

# Using polymorphism
my_dog = Dog()
my_cat = Cat()

animal_sound(my_dog)  # Output: Woof!
animal_sound(my_cat)  # Output: Meow!


# Reusing Code
# Reusing code involves creating reusable functions, classes, or modules to avoid redundancy and improve maintainability.

# Example of a reusable function
def calculate_area(shape, **dimensions):
    if shape == "rectangle":
        return dimensions.get("length") * dimensions.get("width")
    elif shape == "circle":
        import math
        return math.pi * (dimensions.get("radius") ** 2)
    else:
        raise ValueError("Unsupported shape")

# Using the reusable function
area_rectangle = calculate_area("rectangle", length=5, width=3)
area_circle = calculate_area("circle", radius=4)

print(area_rectangle)  # Output: 15
print(area_circle)  # Output: 50.26548245743669

# Example of a reusable class
class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r') as file:
            return file.read()

    def write(self, content):
        with open(self.filename, 'w') as file:
            file.write(content)

# Using the reusable class
file_handler = FileHandler("example.txt")
file_handler.write("Hello, World!")
content = file_handler.read()
print(content)  # Output: Hello, World!

# Reusing code with modules
# You can organize your reusable code into modules (separate files) and import them when needed.

# example_module.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# main.py
# from example_module import add, subtract

result_add = add(10, 5)
result_subtract = subtract(10, 5)

print(result_add)  # Output: 15
print(result_subtract)  # Output: 5

# Enums in Python
# Enums (Enumerations) are a way to define a set of named values. Enums are used to represent fixed sets of constants.

from enum import Enum, auto

class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

print(Color.RED)  # Output: Color.RED
print(Color.GREEN)  # Output: Color.GREEN
print(Color.BLUE)  # Output: Color.BLUE

# Accessing enum members and their values
print(Color.RED.name)  # Output: RED
print(Color.RED.value)  # Output: 1 (auto assigns an integer value starting from 1)

# Iterating through an enum
for color in Color:
    print(color)
