#in Matlab, we can extend a matrix by simply tacking on another dimension, 
#This works on Matlab because it's arrays uses pass-by-value semantics. 
#So the slice operation actually copies parts of the array ad needed.

#By contrast, numpy uses pass-by-reference semantics so that slice
#operations are views into the array without implicit copying. 
#In numpy, slicing creates views, no copying, and advacned indexing ceates copies. 

import numpy as np 

x = np.ones((3, 3))
print("array is: ", x)
print("duplicated last dimension: ", x[:, [0, 1, 2, 2]])

#advanced indexing - gives y a new memory space with the same data. (COPIES)
y = x[:, [0, 1, 2, 2]]
print("new array y (copied) is: ", y)

#Now, we can update the array x and still have data saved in array y
x[0, 0] = 999
print("first array updated is: ", x)
print("the second array remains the same: ", y)

#If we construct the second array, y, by slicing (which makes it a view)
#then changes affect y beacuse it is a window to same meory
x = np.ones((3, 3))
y = x[:2, :2]
x[0, 0] = 999
print("first array is: ", x)
print("second array is: ", y)

#another way to copy without indexing manipulations
x = np.arange(5)
#creates an array
print("the first array now is: ", x)
y = x[[0, 1, 2]]
print("the second array now is: ", y)
#slice creates view
#note that y and z have the same entries
z = x[:3]
print("the sliced array (array z) is", z)
x[0] = 999
print("the first array had been updated to: ", x)
print("note that the second array is uaffected: ", y)
print("but z has been affected, since it was a view: ", z)

