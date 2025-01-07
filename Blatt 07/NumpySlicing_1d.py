import numpy as np

a = np.arange(42, 420)

summedLast18 = np.sum(a[-18:])
print(summedLast18)


# [0 1 2 3 4 5 6 7  8  9]
#             .... -2 -1