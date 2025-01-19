import numpy as np
import matplotlib.pyplot as plt

def stepwiseMovingAverage(data, n):
    intervals = np.linspace(len(data)//(2*n), ((2*n-1)*len(data))//(2*n), n, dtype=int)
    y = np.zeros(len(intervals))
    for i in range(len(intervals)):
        y[i] = np.mean(data[intervals[i]-len(data)//(2*n):intervals[i]+len(data)//(2*n)])
    print(intervals, y)
    return intervals, y

# Daten einlesen
table = np.loadtxt('Blatt 08/muenchen_flughafen.txt')
tx = table[:, 6][::-1]

plt.plot(tx, color="blue", linestyle=" ", marker=".")

# Stückweiser laufender Mittelwerte berechnen
plt.plot(*stepwiseMovingAverage(tx, 3), color="red", linestyle="-", marker="")

plt.title("Temperatur in München")
plt.ylabel("Temperatur")
plt.xlabel("Tage")

plt.show()