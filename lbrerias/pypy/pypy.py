# PyPy
# PyPy is an alternative implementation of the Python programming language, which often runs faster than the standard implementation of Python, CPython.
# It includes a Just-In-Time (JIT) compiler which can greatly speed up the execution of Python code.

# Installing PyPy
# To use PyPy, you need to install it. You can download it from the PyPy website or install it using a package manager like Homebrew on macOS:
# brew install pypy3

# Running Python code with PyPy
# Once installed, you can run your Python scripts with PyPy by using the `pypy` command instead of `python`.

# Example of running a script with PyPy
# Save your Python script to a file, e.g., myscript.py, and then run:
# pypy myscript.py

# Performance Comparison
# Below is an example to compare the performance of CPython and PyPy.

import time

def calculate_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total

# Measuring time with CPython
start_time = time.time()
print(calculate_sum(10**7))
end_time = time.time()
print(f"CPython Time: {end_time - start_time} seconds")

# To measure time with PyPy, run the same script with pypy:
# pypy myscript.py

# Benefits of PyPy
# 1. Speed: PyPy can execute code faster due to its JIT compiler.
# 2. Memory Usage: PyPy can be more memory efficient for certain workloads.
# 3. Compatibility: PyPy aims to be fully compatible with existing Python code and libraries.

# Limitations of PyPy
# 1. Compatibility: Although PyPy aims for full compatibility, there may be some libraries or C extensions that do not work as expected with PyPy.
# 2. Warm-up Time: PyPy's JIT compiler may have a warm-up time, meaning that for short-running scripts, the performance improvement may not be noticeable.

# Example Code to Illustrate PyPy Usage
# The following example demonstrates a simple computation and can be run with both CPython and PyPy to compare performance.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Measuring time for the Fibonacci calculation
start_time = time.time()
print(fibonacci(30))
end_time = time.time()
print(f"CPython Time for Fibonacci: {end_time - start_time} seconds")

# To compare, run this with PyPy:
# pypy myscript.py

# Conclusion
# PyPy is a powerful alternative to CPython that can offer significant performance improvements for many applications.
# By leveraging its JIT compiler, PyPy can execute Python code more efficiently, making it a great choice for performance-critical applications.
