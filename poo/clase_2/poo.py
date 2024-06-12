# Inheritance in Python
# Inheritance is a feature in object-oriented programming that allows a class to inherit attributes and methods from another class. The class that inherits is called a subclass or derived class, and the class being inherited from is called a superclass or base class.

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        # This is a method that can be overridden by subclasses
        raise NotImplementedError("Subclass must implement abstract method")

# Subclass
class Dog(Animal):
    def speak(self):
        # This method overrides the speak method in the base class
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        # This method overrides the speak method in the base class
        return f"{self.name} says Meow!"

# Creating instances of subclasses
my_dog = Dog("Buddy")
my_cat = Cat("Whiskers")

print(my_dog.speak())  # Output: Buddy says Woof!
print(my_cat.speak())  # Output: Whiskers says Meow!

# Multiple Inheritance
# Python supports multiple inheritance, where a class can inherit from more than one base class.

class Canine:
    def has_tail(self):
        return True

class Labrador(Dog, Canine):
    def breed(self):
        return "Labrador"

# Creating an instance of the subclass with multiple inheritance
my_labrador = Labrador("Max")

print(my_labrador.speak())  # Output: Max says Woof!
print(my_labrador.has_tail())  # Output: True
print(my_labrador.breed())  # Output: Labrador

# The super() Function
# The super() function is used to give access to methods and properties of a parent or sibling class. It returns a temporary object of the superclass that allows you to call its methods.

class Bird(Animal):
    def __init__(self, name, can_fly):
        # Initialize the base class using super()
        super().__init__(name)
        self.can_fly = can_fly

    def speak(self):
        return f"{self.name} says Tweet!"

    def fly(self):
        if self.can_fly:
            return f"{self.name} can fly."
        else:
            return f"{self.name} cannot fly."

# Creating an instance of the Bird subclass
my_bird = Bird("Tweety", True)

print(my_bird.speak())  # Output: Tweety says Tweet!
print(my_bird.fly())  # Output: Tweety can fly.

# Overriding Methods
# Subclasses can override methods from the base class to provide specific implementations.

class Fish(Animal):
    def speak(self):
        # Overriding the speak method
        return f"{self.name} does not make a sound."

    def swim(self):
        return f"{self.name} is swimming."

# Creating an instance of the Fish subclass
my_fish = Fish("Goldie")

print(my_fish.speak())  # Output: Goldie does not make a sound.
print(my_fish.swim())  # Output: Goldie is swimming.

# The isinstance() Function
# The isinstance() function is used to check if an object is an instance of a specific class or a tuple of classes.

print(isinstance(my_dog, Dog))  # Output: True
print(isinstance(my_dog, Animal))  # Output: True
print(isinstance(my_dog, Cat))  # Output: False

# The issubclass() Function
# The issubclass() function is used to check if a class is a subclass of another class or a tuple of classes.

print(issubclass(Dog, Animal))  # Output: True
print(issubclass(Labrador, Dog))  # Output: True
print(issubclass(Cat, Dog))  # Output: False
