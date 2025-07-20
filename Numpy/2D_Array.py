import numpy as np  # Import NumPy

arr = np.array([[1, 2], [3, 4]])  # Create 2D array
print("2D Array:\n", arr)

print("Shape:", arr.shape)        # Rows and columns
print("Size:", arr.size)          # Total elements
print("Transpose:\n", arr.T)      # Transpose of array

print("Sum of rows:", np.sum(arr, axis=1))  # Row-wise sum
print("Sum of cols:", np.sum(arr, axis=0))  # Column-wise sum
