import numpy as np  # Import NumPy

arr = np.array([1, 2, 3, 4, 5, 6])  # 1D array
print("Original:", arr)

reshaped = arr.reshape(2, 3)       # Reshape to 2x3
print("Reshaped (2x3):\n", reshaped)

flat = reshaped.flatten()          # Flatten back to 1D
print("Flattened:", flat)
