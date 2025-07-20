import numpy as np  # Import NumPy

arr = np.array([10, 20, 30, 40, 50])  # 1D array
print("Original:", arr)

cond = arr > 25            # Condition: elements > 25
print("Condition:", cond)

filtered = arr[cond]       # Apply condition
print("Filtered:", filtered)
