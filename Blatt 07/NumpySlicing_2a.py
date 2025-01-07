import numpy as np
import random

apy = [
    [random.randint(0, 10) for _ in range(30)]
    for _ in range(20)
]
a = np.random.randint(0, 11, (20, 30))

count = np.sum(a[:, :2] >= 2)
# a[1, 2] <=> a[1][2]
print(count)