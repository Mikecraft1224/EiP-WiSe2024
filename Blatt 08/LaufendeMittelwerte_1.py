import numpy as np
import matplotlib.pyplot as plt

# Daten einlesen
table = np.loadtxt('Blatt 08/muenchen_flughafen.txt')
tx = table[:, 6][::-1]

# Mittelwert berechnen
plt.plot(tx, color="blue", linestyle=" ", marker=".")
plt.hlines(np.mean(tx), 0, len(tx), color="orange")
plt.title("Temperatur in München")
plt.ylabel("Temperatur")
plt.xlabel("Tage")

plt.show()