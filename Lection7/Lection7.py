import numpy as np

#6. Create a null vector of size 10 but the fifth value which is 1
z = np.zeros(10)
z[4] = 1

#8. Reverse a vector (first element becomes last)
z = z[::-1]

#9. Create a 3x3 matrix with values ranging from 0 to 8
z = np.arange(9)
z = z.reshape(3, 3)

#19. Create a 8x8 matrix and fill it with a checkerboard pattern
z = np.zeros((8, 8))
z[1::2, ::2] = 1
z[::2, 1::2] = 1

#44. Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates
z = np.random.random((10, 2))
x = z[:, 0]
y = z[:, 1]
r = np.sqrt(x * x + y * y)
phi = np.arctan2(y, x)

