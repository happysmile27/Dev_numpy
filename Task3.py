import numpy as np
z = np.random.randint(10, 100, size=15)
print(z[-10:])
print(np.average(z[-10:]))