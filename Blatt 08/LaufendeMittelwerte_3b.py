import numpy as np
import matplotlib.pyplot as plt

def movingAverage(data, left=1, right=1):
    movingAverages = np.zeros(len(data))
    for i in range(len(data)):
        lower = i-left if i-left >= 0 else 0
        upper = i+right+1 if i+right+1 <= (lst := len(data) - 1) else lst
        movingAverages[i] = np.mean(data[lower:upper])
    return movingAverages

# Daten einlesen
table = np.loadtxt('Blatt 08/muenchen_flughafen.txt')
tx = table[:, 6][::-1]

# Laufenden Mittelwert berechnen
movingAverages = movingAverage(tx)
plt.plot(movingAverages, color="orange", linestyle="-")

plt.title("Temperatur in München")
plt.ylabel("Temperatur")
plt.xlabel("Tage")

plt.show()