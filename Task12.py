import numpy as np
x = np.array([[34,43,73],[82,22,12],[53,94,66]])
max_row = np.amax(x, 0)
min_column = np.amin(x, 1)
print(min_column)
print(max_row)