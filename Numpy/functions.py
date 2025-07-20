import numpy as np  # Import NumPy

arr = np.array([5, 10, 5, 20, 10, 5])

print("Original:", arr)

print("Unique Elements:", np.unique(arr))         # Unique values
print("Positions of 10:", np.where(arr == 10))    # Indices of 10
print("Even Numbers:", arr[np.where(arr % 2 == 0)])  # Filter even
