import matplotlib.pyplot as plt
import numpy as np

table = np.loadtxt("Blatt 07\muenchen_flughafen.txt")
rr = table[:, -2][::-1]

plt.title("Niederschlag in München")
plt.hist(rr, bins=5)
plt.xlabel("Niederschlag in mm")
plt.ylabel("Anzahl Tage")

plt.show()