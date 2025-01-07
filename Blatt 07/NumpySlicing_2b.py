import numpy as np

a = np.random.randint(0, 10, (20, 30))

a[0, :] = -1 # a[0] <=> a[0, :]
a[-1, :] = -1 # a[-1] <=> a[-1, :]
a[:, 0] = -1
a[:, -1] = -1

# Alternative:
# a[:, [0, -1]] = -1
# a[[0, -1], :] = -1

print(a)