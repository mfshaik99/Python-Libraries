import numpy as np  # Import NumPy

arr = np.random.rand(2, 3)     # 2x3 array with random floats (0 to 1)
print("Random Float Array:\n", arr)

ints = np.random.randint(1, 10, size=(3, 2))  # Random ints 1–9 in 3x2 array
print("Random Int Array:\n", ints)

np.random.seed(42)  # Set seed for reproducibility
print("Same Random Number:", np.random.rand())
