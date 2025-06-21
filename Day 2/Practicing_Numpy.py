import numpy as np
# 1. Create a NumPy array of numbers from 10 to 20.

# arr = np.arange(10, 21)
# print(arr)

# 2. Create a 2D array with shape (3, 4) filled with ones.

# arr = np.ones((3,4), dtype = int)
# print(arr)


# 3. Find the shape, size, and data type of the following array:
# arr = np.array([[1, 2, 3], [4, 5, 6]])

# arr = np.array([[1, 2, 3], [4, 5, 6]])

# print("Shape of Array: ", arr.shape)
# print("Size of Array: ", arr.size)
# print("Dtype of Array is: ", arr.dtype)


# 4. Reshape a 1D array of 9 elements into a 3x3 matrix.

# arr =  np.arange(1, 10)
# matrix = arr.reshape((3,3))
# print(matrix)
# print(matrix.shape)


# 5. Generate an array of 5 equally spaced numbers between 0 and 1.

# arr =  np.linspace(0, 1, 5)
# print(arr)


# 6. Replace all odd numbers in an array with -1.
# Example: [1, 2, 3, 4] → [-1, 2, -1, 4]

arr = np.arange(0, 10, dtype = int)
# print(arr)
for i in arr:
    # print(i)
    if i % 2 == 1:
        arr[i] = -1

print(arr)