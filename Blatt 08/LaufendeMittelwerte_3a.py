import numpy as np

def movingAverage(data):
    movingAverages = np.zeros(len(data))
    for i in range(len(data)):
        movingAverages[i] = np.mean(data[i-1:i+2])
    return movingAverages

# Daten einlesen
table = np.loadtxt('Blatt 08/muenchen_flughafen.txt')
tx = table[:, 6][::-1]

movingAverages = movingAverage(tx)

print(movingAverages)