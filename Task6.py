import numpy as np
z = np.random.randint(0, 20, size=20)
print(z[np.nonzero(z)])
