import numpy as np  # Import NumPy

arr = np.array([1, 2, 3, 4, 5])  # Create 1D array
print("Original Array:", arr)

print("Shape:", arr.shape)      # Array shape
print("Data Type:", arr.dtype)  # Data type

print("Array + 2:", arr + 2)    # Add 2 to each element
print("Array * 3:", arr * 3)    # Multiply each element by 3

print("Mean:", np.mean(arr))    # Average value
print("Max:", np.max(arr))      # Maximum value
print("Sum:", np.sum(arr))      # Sum of all elements
