import numpy as np
A = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
x = np.matrix([[1], [0], [1]])
print("the first matrix is: ", A)
print("the second matrix is: ", x)
product = A * x
print("The product of the matrices is:", product)