#multiplication of matrices
import numpy as np
A = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
x = np.matrix([[1], [0], [0]])
print("the first matrix is: ", A)
print("the second matrix is: ", x)
product = A * x
print("The product of the matrices is:", product)

#multiplication of arrays
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
x = np.array([[1], [0], [0]])
print("the first matrix is: ", A)
print("the second matrix is: ", x)
product = A.dot(x)

#Num-arrays suppoers element wise multiplication
#It does not support row-column multiplication
print("The product of the matrices is:", product)
newSymforMul = A@x
print("New symbol product is: ", newSymforMul)