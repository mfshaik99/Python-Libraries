import numpy as np  # Import NumPy

a = np.array([[1, 2], [3, 4]])  # First matrix
b = np.array([[5, 6], [7, 8]])  # Second matrix

print("Matrix A:\n", a)
print("Matrix B:\n", b)

print("A + B:\n", a + b)             # Matrix addition
print("A - B:\n", a - b)             # Matrix subtraction
print("A * B:\n", a * b)             # Element-wise multiplication
print("A dot B:\n", np.dot(a, b))    # Matrix multiplication
