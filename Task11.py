import numpy as np
x = np.array([[34,43,73],[82,22,12],[53,94,66]])
new_col = np.array([[10,10,10]])
x = np.delete(x, 1, 0)
x = np.insert(x, 1, new_col, 0)
print(x)