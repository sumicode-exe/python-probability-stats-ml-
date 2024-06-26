from numpy.lib.stride_tricks import as_strided
import numpy as np

x = np.ones((3, 3))
print("array is: ", x)
print("duplicated last dimension: ", x[:, [0, 1, 2, 2]])

# advanced indexing - gives y a new memory space with the same data. (COPIES)
y = x[:, [0, 1, 2, 2]]
print("new array y (copied) is: ", y)

# Now, we can update the array x and still have data saved in array y
x[0, 0] = 999
print("first array updated is: ", x)
print("the second array remains the same: ", y)

# If we construct the second array, y, by slicing (which makes it a view)
# then changes affect y beacuse it is a window to same meory
x = np.ones((3, 3))
y = x[:2, :2]
x[0, 0] = 999
print("first array is: ", x)
print("second array is: ", y)

# another way to copy without indexing manipulations
x = np.arange(5)
# creates an array
print("the first array now is: ", x)
y = x[[0, 1, 2]]
print("the second array now is: ", y)
# slice creates view
# note that y and z have the same entries
z = x[:3]
print("the sliced array (array z) is", z)
x[0] = 999
print("the first array had been updated to: ", x)
print("note that the second array is uaffected: ", y)
print("but z has been affected, since it was a view: ", z)

# using numpy to create overlapping blocks that do
# not consume additional memory
x = np.arange(16, dtype=np.int64)
y = as_strided(x, (7, 4), (16, 8))
print("array after overlapped entries is: ", y)
# The above code created a range of integers and then
# overlaps the entries to create a numpy array.
# as_strided creates a view into the array given the
# exact strides and shape. This means it manipulates
# the internal data structure of ndarray
x[::2] = 99
print("value of x is:", x)
print("value of y is:", y)

# To expilicity control the dimensions
n = 8
x = np.arange(n)
k = 5
y = as_strided(x, (k, n-k+1), (x.itemsize, ) * 2)
print("after explicit dimension manippulation is:", y)

# multiplication of matrices
A = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
x = np.matrix([[1], [0], [0]])
print("the first matrix is: ", A)
print("the second matrix is: ", x)
product = A * x
print("The product of the matrices is:", product)

# multiplication of arrays
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
x = np.array([[1], [0], [0]])
print("the first matrix is: ", A)
print("the second matrix is: ", x)
product = A.dot(x)

# Num-arrays suppoers element wise multiplication
# It does not support row-column multiplication
print("The product of the matrices is:", product)
newSymforMul = A@x
print("New symbol product is: ", newSymforMul)
