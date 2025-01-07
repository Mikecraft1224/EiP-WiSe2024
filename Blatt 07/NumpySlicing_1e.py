import numpy as np

apy = [x for x in range(42, 420)]
a = np.arange(42, 420)

even = a[a % 2 == 0]
print(even)

odd = a[a % 2 == 1]
print(odd)