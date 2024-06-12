# Control Structures in Python
# Control structures allow you to direct the flow of execution in your code.

# if statement
x = 10
if x > 5:
    # This block executes if the condition is True
    print("x is greater than 5")
elif x == 5:
    # This block executes if the previous condition is False and this condition is True
    print("x is equal to 5")
else:
    # This block executes if all previous conditions are False
    print("x is less than 5")

# for loops
# A for loop is used to iterate over a sequence (list, tuple, dictionary, set, or string).

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    # This block executes for each item in the list
    print(fruit)

# while loops
# A while loop executes as long as the condition is True.

i = 0
while i < 5:
    # This block executes while i is less than 5
    print(i)
    i += 1  # Increment i by 1 on each iteration

# Functions in Python
# Functions are reusable blocks of code that perform a specific task.

def greet(name):
    # This function takes one parameter 'name' and prints a greeting
    print("Hello, " + name + "!")

# Calling the function
greet("Carlos")

# Function with return value
def add(a, b):
    # This function takes two parameters and returns their sum
    return a + b

# Calling the function and storing the result
result = add(3, 5)
print(result)  # Output: 8

# Tuples in Python
# A tuple is an ordered and immutable collection. It allows duplicate members.

my_tuple = ("apple", "banana", "cherry")
print(my_tuple[1])  # Output: banana

# Tuples are immutable, they cannot be changed after their creation
# However, they can be used to store data that should not change

# Iterators and Comprehensions in Python
# Iterators are objects that contain a countable number of values, which can be iterated over one by one.

my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list)

# Using next() to get the elements
print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 2

# List comprehensions
# List comprehensions provide a concise way to create lists.

squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Dictionary comprehensions
# Similarly, dictionary comprehensions provide a concise way to create dictionaries.

evens = {x: x**2 for x in range(10) if x % 2 == 0}
print(evens)  # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Set comprehensions
# Set comprehensions create sets with unique elements.

my_set = {x for x in "abracadabra" if x not in "abc"}
print(my_set)  # Output: {'d', 'r'}

# Generator comprehensions
# Generators are a special type of iterator created using a generator expression.

my_generator = (x**2 for x in range(10))
for value in my_generator:
    print(value)
    # Output: 0, 1, 4, 9, 16, 25, 36, 49, 64, 81 (on separate lines)
