# Syntax in Python
# Python uses indentation to define blocks of code. This is different from many other programming languages that use braces {} or keywords.

def greet(name):
    # This is a function that takes one parameter, 'name'
    print("Hello, " + name + "!")  # This line prints a greeting message

# Calling the function
greet("Alice")

# Proper indentation is crucial in Python
if True:
    # This block is executed because the condition is True
    print("This is true")
else:
    # This block is not executed
    print("This is false")

# Data Types in Python
# Python supports various data types including integers, floats, strings, booleans, and complex numbers.

# Integer
a = 10  # This is an integer
print(type(a))  # Output: <class 'int'>

# Float
b = 20.5  # This is a float
print(type(b))  # Output: <class 'float'>

# String
c = "Hello, World!"  # This is a string
print(type(c))  # Output: <class 'str'>

# Boolean
d = True  # This is a boolean
print(type(d))  # Output: <class 'bool'>

# Complex Number
e = 1 + 2j  # This is a complex number
print(type(e))  # Output: <class 'complex'>

# Lists in Python
# A list is a collection which is ordered and changeable. Allows duplicate members.

fruits = ["apple", "banana", "cherry"]  # This is a list of strings
print(fruits[1])  # Output: banana

# Adding an item to the list
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

# Removing an item from the list
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry', 'orange']

# Accessing items by index
print(fruits[0])  # Output: apple
print(fruits[-1])  # Output: orange

# Slicing the list
print(fruits[1:3])  # Output: ['cherry', 'orange']

# Dictionaries in Python
# A dictionary is a collection which is unordered, changeable, and indexed. No duplicate members.

student = {
    "name": "John",
    "age": 21,
    "major": "Computer Science"
}

print(student["name"])  # Output: John

# Adding a new key-value pair
student["graduation_year"] = 2024
print(student)  # Output: {'name': 'John', 'age': 21, 'major': 'Computer Science', 'graduation_year': 2024}

# Removing a key-value pair
del student["age"]
print(student)  # Output: {'name': 'John', 'major': 'Computer Science', 'graduation_year': 2024}

# Accessing all keys and values
print(student.keys())  # Output: dict_keys(['name', 'major', 'graduation_year'])
print(student.values())  # Output: dict_values(['John', 'Computer Science', 2024])

# Iterating through a dictionary
for key, value in student.items():
    print(key, ":", value)
    # Output:
    # name : John
    # major : Computer Science
    # graduation_year : 2024

# Nesting in Dictionaries
# Dictionaries can contain other dictionaries, which is useful for storing complex data.

university = {
    "name": "MIT",
    "location": "Cambridge",
    "departments": {
        "Engineering": {
            "number_of_students": 5000,
            "head": "Dr. Smith"
        },
        "Humanities": {
            "number_of_students": 2000,
            "head": "Dr. Jones"
        }
    }
}

print(university["departments"]["Engineering"]["head"])  # Output: Dr. Smith
