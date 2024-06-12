# Abstract Classes in Python
# An abstract class is a class that cannot be instantiated and is designed to be subclassed. It can include abstract methods that must be implemented by subclasses.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        # Abstract method that must be implemented by subclasses
        pass

    @abstractmethod
    def perimeter(self):
        # Abstract method that must be implemented by subclasses
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Creating an instance of the Rectangle class
rect = Rectangle(10, 5)
print(rect.area())  # Output: 50
print(rect.perimeter())  # Output: 30

# Interfaces in Python
# Python does not have a built-in interface keyword, but interfaces can be implemented using abstract base classes.

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        # Abstract method that must be implemented by subclasses
        pass

class Circle(Drawable):
    def draw(self):
        return "Drawing a circle"

class Square(Drawable):
    def draw(self):
        return "Drawing a square"

# Using the interfaces
shapes = [Circle(), Square()]
for shape in shapes:
    print(shape.draw())
    # Output:
    # Drawing a circle
    # Drawing a square

# Exception Handling in Python
# Exception handling is a way to respond to exceptions (errors) during runtime. It allows you to manage and handle errors gracefully.

try:
    # Code that may raise an exception
    x = 1 / 0
except ZeroDivisionError:
    # This block handles the ZeroDivisionError
    print("Cannot divide by zero")
except Exception as e:
    # This block handles any other exception
    print(f"An error occurred: {e}")
else:
    # This block executes if no exceptions are raised
    print("Division successful")
finally:
    # This block always executes, regardless of whether an exception was raised or not
    print("Execution complete")

# Custom Exception Handling
# You can define your own custom exceptions by subclassing the built-in Exception class.

class CustomError(Exception):
    def __init__(self, message):
        self.message = message

def risky_operation():
    raise CustomError("This is a custom error message")

try:
    risky_operation()
except CustomError as e:
    print(f"Caught custom error: {e.message}")
    # Output: Caught custom error: This is a custom error message
