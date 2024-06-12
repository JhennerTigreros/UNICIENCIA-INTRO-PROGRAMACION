# Creating Your First Test with pytest
# pytest is a popular testing framework for Python that makes it easy to write simple and scalable test cases.

# First, you need to install pytest if you haven't already:
# pip install pytest

# Create a new file called test_sample.py and add the following code:

# test_sample.py
def add(x, y):
    # This function returns the sum of x and y
    return x + y

def test_add():
    # This is a test function that tests the add function
    assert add(2, 3) == 5  # The test will pass if the add function returns 5 when called with 2 and 3
    assert add(-1, 1) == 0  # The test will pass if the add function returns 0 when called with -1 and 1
    assert add(0, 0) == 0  # The test will pass if the add function returns 0 when called with 0 and 0

# To run the test, use the following command in the terminal:
# pytest test_sample.py

# Intermediate Topics Related to Tests
# 1. Using fixtures
# Fixtures are a way to provide a fixed baseline for tests. They are used to setup some preconditions and cleanup afterward.

import pytest

@pytest.fixture
def sample_data():
    # This fixture returns a dictionary with sample data
    return {"name": "Alice", "age": 30, "city": "Wonderland"}

def test_sample_data(sample_data):
    # This test function uses the sample_data fixture
    assert sample_data["name"] == "Alice"
    assert sample_data["age"] == 30
    assert sample_data["city"] == "Wonderland"

# 2. Parametrized tests
# Parametrization allows you to run a test function multiple times with different arguments.

@pytest.mark.parametrize("x, y, result", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (10, 5, 15)
])
def test_add_parametrized(x, y, result):
    # This test function will run multiple times with different sets of arguments
    assert add(x, y) == result
    

# 3. Grouping tests with classes
# You can group related tests into a class to organize them better.

class TestMathOperations:
    def test_add(self):
        assert add(1, 2) == 3
        assert add(-1, -1) == -2
    
    def test_add_with_floats(self):
        assert add(1.5, 2.5) == 4.0

# 4. Mocking
# Mocking is used to replace parts of your system under test and make assertions about how they have been used.

from unittest.mock import Mock

def fetch_data_from_api(api_url):
    # This function simulates fetching data from an API
    pass

def test_fetch_data_from_api():
    mock_api = Mock()
    mock_api.get.return_value = {"data": "sample_data"}
    
    fetch_data_from_api(mock_api)
    mock_api.get.assert_called_once()  # This checks that the get method was called exactly once

# These examples demonstrate basic and intermediate testing concepts with pytest. Testing is crucial for ensuring your code works as expected and helps prevent bugs.
