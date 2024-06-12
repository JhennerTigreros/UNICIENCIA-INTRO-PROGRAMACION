# Object-Oriented Programming (OOP)
# OOP is a programming paradigm based on the concept of "objects", which are data structures that contain data and methods.

# Classes in Python
# A class is a blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class can use.

class Dog:
    # This is a class named Dog
    
    # Initializer / Instance Attributes
    def __init__(self, name, age):
        # These are properties of the class
        self.name = name
        self.age = age
    
    # Method to get the description of the dog
    def description(self):
        return f"{self.name} is {self.age} years old."
    
    # Method to get the sound of the dog
    def speak(self, sound):
        return f"{self.name} says {sound}"

# Creating an instance of the Dog class
my_dog = Dog("Buddy", 3)

# Accessing properties
print(my_dog.name)  # Output: Buddy
print(my_dog.age)  # Output: 3

# Calling methods
print(my_dog.description())  # Output: Buddy is 3 years old.
print(my_dog.speak("Woof"))  # Output: Buddy says Woof

# Properties of a Class
# Properties allow you to add logic to getting and setting attribute values. You use properties to make attribute access more flexible.

class Circle:
    def __init__(self, radius):
        self._radius = radius  # Using a leading underscore to indicate this is a private attribute

    # Getter for radius
    @property
    def radius(self):
        return self._radius

    # Setter for radius
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    # Method to calculate area
    def area(self):
        import math
        return math.pi * (self._radius ** 2)

# Creating an instance of the Circle class
my_circle = Circle(5)
print(my_circle.radius)  # Output: 5
print(my_circle.area())  # Output: 78.53981633974483

# Changing the radius using the setter
my_circle.radius = 10
print(my_circle.radius)  # Output: 10
print(my_circle.area())  # Output: 314.1592653589793

# Class Functions (Methods)
# These are functions defined inside a class and are used to perform operations on objects of that class.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Method to get the description of the car
    def description(self):
        return f"{self.year} {self.make} {self.model}"
    
    # Method to start the car
    def start(self):
        return f"{self.make} {self.model} is starting."

# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla", 2020)
print(my_car.description())  # Output: 2020 Toyota Corolla
print(my_car.start())  # Output: Toyota Corolla is starting.

# Primitive Functions
# These are built-in functions in Python that are available without needing to import any module.

# Some examples of primitive functions include:
print(len("Hello, World!"))  # Output: 13
print(max(10, 20, 30))  # Output: 30
print(abs(-7.5))  # Output: 7.5

# Primitive functions can also be used with user-defined objects by defining special methods (magic methods) in the class.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    # Defining the __str__ method to use with print()
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    # Defining the __len__ method to use with len()
    def __len__(self):
        return len(self.title)

# Creating an instance of the Book class
my_book = Book("1984", "George Orwell")
print(my_book)  # Output: '1984' by George Orwell
print(len(my_book))  # Output: 4
