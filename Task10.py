import numpy as np
x = np.array([ 6,  9, 16,  1, 13,  6,  7, 12,  2, 14])
y = np.array([16,  7,  8, 16,  9, 14, 10,  5, 14, 19])
z = np.intersect1d(x, y)
print(z)