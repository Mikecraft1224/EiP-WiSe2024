import numpy as np

a = np.random.randint(0, 10, (20, 30))

a[np.random.randint(0, a.shape[0]), -1] = -2

print(a)