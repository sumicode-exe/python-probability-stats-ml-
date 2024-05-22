# numpy's meshgrid creates two-dimensional grids
import numpy as np
X, Y = np.meshgrid(np.arange(2), np.arange(2))
print("array X:", X)
print("array Y:", Y)

# To add X and Y
print("The sum is: ", X+Y)

# We can skip a step, not bother with the meshgrid
# We can implicitly obtain the vertex coordinates
# by using broadcasting
x = np.array([0, 1])
y = np.array([0, 1])
print("array x: ", x)
print("array y: ", y)
# this adds a broadcasting dimension
sum = x+y[:, None]
print("sum is: ", sum)
