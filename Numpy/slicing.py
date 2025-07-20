import numpy as np  # Import NumPy

arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])  # 3x3 array
print("Array:\n", arr)

print("Element at (1,2):", arr[1, 2])        # Access element at row 1, col 2
print("First row:", arr[0])                 # First row
print("Second column:", arr[:, 1])          # Second column
print("Subarray (2x2):\n", arr[0:2, 0:2])    # Slice 2x2 block from top-left
