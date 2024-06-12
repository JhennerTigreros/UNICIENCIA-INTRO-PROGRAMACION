

# mathlib/setup.py
from setuptools import setup, find_packages

setup(
    name="mathlib",
    version="0.1",
    packages=find_packages(),
    description="A simple math library for basic operations.",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/mathlib",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

# Instructions to set up and use the library:

# 1. Navigate to the directory containing the setup.py file.
# 2. Run the following command to install the library:
#    pip install .

# 3. You can now use the library in your Python scripts as follows:
#    from mathlib import add, subtract, multiply, divide

#    result = add(10, 5)
#    print(result)  # Output: 15
