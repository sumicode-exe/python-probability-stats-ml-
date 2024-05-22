#recommended attribute to call numpy
import numpy as np

#using numpy to create and array and find its size
x = np.array([1, 2, 3], dtype = np.float32)
print("the array is", x)
print("the size of the array is:", x.itemsize)

#numpy to find the sine of data in an array
sineNumpy = np.sin(x)
print("The sine of the values in the array is:", sineNumpy)

#NUMPY IS BETTER SINCE WE DO NOT HAVE TO USE THE FOLLOING LOOP:
from math import sin
sineMath = [sin(i) for i in [1, 2, 3]]
print("The sine of the values in the array is:", sineMath)

#NUMPY USES COMMON SENSE CASTING RULES TO RESOLVE THE OUTPUT TYPES. 

#array dimension, row and column detemination
y = np.array([[1, 2, 3], [4, 5, 6,]])
print("the dimension of the array is", y.shape)
print("y - 0th column:", y[:, 0])
print("y - 1st column:", y[:, 1])
print("y - 0th row:", y[0, :])
print("y - 1st row:", y[0, :])

#array slicing to select elements
print("all rows, 1st through last column:", y[:, 1:])
print("all rows, every other column:", y[:, ::2])
print("reverse order of the columns", y[:, ::-1])

