import numpy as np  # Import NumPy

a = np.array([[1, 2], [3, 4]])  # First 2x2 array
b = np.array([[5, 6], [7, 8]])  # Second 2x2 array

print("Vertical Stack:\n", np.vstack((a, b)))   # Stack rows
print("Horizontal Stack:\n", np.hstack((a, b))) # Stack columns
