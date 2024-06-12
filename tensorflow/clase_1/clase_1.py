# Tensors with NumPy
# Tensors are multi-dimensional arrays and are a fundamental data structure used in machine learning and scientific computing.
# NumPy provides a powerful N-dimensional array object called ndarray which can be used to create and manipulate tensors.

import numpy as np

# Creating a 1D tensor (vector)
vector = np.array([1, 2, 3])
print("1D Tensor (Vector):\n", vector)

# Creating a 2D tensor (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Tensor (Matrix):\n", matrix)

# Creating a 3D tensor
tensor_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("3D Tensor:\n", tensor_3d)

# Accessing elements in a tensor
print("Element at position (1, 1) in the 2D tensor:", matrix[1, 1])  # Output: 5
print("Element at position (0, 1, 2) in the 3D tensor:", tensor_3d[0, 1, 2])  # Output: 6

# Basic tensor operations
# Element-wise addition
tensor_a = np.array([[1, 2], [3, 4]])
tensor_b = np.array([[5, 6], [7, 8]])
tensor_sum = tensor_a + tensor_b
print("Element-wise addition:\n", tensor_sum)

# Element-wise multiplication
tensor_product = tensor_a * tensor_b
print("Element-wise multiplication:\n", tensor_product)

# Matrix multiplication with NumPy
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
matrix_mul = np.dot(matrix_a, matrix_b)
print("Matrix multiplication with NumPy:\n", matrix_mul)

# Matmul with Pure Python vs NumPy
# Matrix multiplication is a common operation in linear algebra and can be implemented in both pure Python and using NumPy for efficiency.

# Matrix multiplication with pure Python
def matmul_python(a, b):
    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result

# Creating matrices
matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]

# Matrix multiplication with pure Python
result_python = matmul_python(matrix_a, matrix_b)
print("Matrix multiplication with pure Python:\n", result_python)

# Matrix multiplication with NumPy
matrix_a_np = np.array(matrix_a)
matrix_b_np = np.array(matrix_b)
result_numpy = np.dot(matrix_a_np, matrix_b_np)
print("Matrix multiplication with NumPy:\n", result_numpy)

# Performance comparison
import time

# Timing pure Python matrix multiplication
start_time = time.time()
for _ in range(1000):
    result_python = matmul_python(matrix_a, matrix_b)
end_time = time.time()
print(f"Pure Python matmul time: {end_time - start_time} seconds")

# Timing NumPy matrix multiplication
start_time = time.time()
for _ in range(1000):
    result_numpy = np.dot(matrix_a_np, matrix_b_np)
end_time = time.time()
print(f"NumPy matmul time: {end_time - start_time} seconds")

# Conclusion
# NumPy's implementation of matrix multiplication is significantly faster and more efficient than a pure Python implementation.
# This is due to NumPy's use of optimized C libraries and efficient memory management.
