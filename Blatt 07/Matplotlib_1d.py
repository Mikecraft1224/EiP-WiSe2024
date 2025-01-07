import matplotlib.pyplot as plt
import numpy as np

table = np.loadtxt("Blatt 07\muenchen_flughafen.txt")
rr = table[:, -2][::-1]
tx = table[:, 6][::-1]

fig, ax1 = plt.subplots()
fig.suptitle("Temperatur und Niederschlag in München")

ax1.plot(tx, color="red")
ax1.set_xlabel("Tage")
ax1.set_ylabel("Temperatur", color="red")
ax1.tick_params(axis="y", labelcolor="red")

# twinx wird verwendet, um eine zweite y-Achse mit dem selben x-Achsenverlauf zu erstellen
ax2 = ax1.twinx()
ax2.scatter(np.arange(0, len(rr)), rr, color="blue", s=rr)
ax2.set_ylabel("Niederschlag", color="blue")
ax2.tick_params(axis="y", labelcolor="blue")

plt.show()