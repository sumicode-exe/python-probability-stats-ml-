#numpy's meshgrid creates two-dimensional grids
import numpy as np
X, Y = np.meshgrid(np.arange(2), np.arange(2))
print("array X:", X)
print("array Y:", Y)

#To add X and Y
print("The sum is: ", X+Y)
