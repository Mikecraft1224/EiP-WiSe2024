import numpy as np

table = np.loadtxt("Blatt 07\muenchen_flughafen.txt")
rr = table[:, -2][::-1]

minimum, maximum = np.min(rr), np.max(rr)
# 6 Werte im linearen Abstand zwischen minimum und maximum um 5 Abschnitte zu erhalten
binValues = np.linspace(minimum, maximum, 6)

# Für Einfachheit setze ich den letzten Wert auf einen Wert, der sicher größer als der größte Wert ist
binValues[-1] = maximum + 1

bins = np.zeros(5)

for i, bin in enumerate(binValues[:-1]):
    # Zähle alle Werte, die größer gleich dem aktuellen bin-Wert sind und kleiner als der nächste bin-Wert
    bins[i] = np.sum(np.logical_and(rr >= bin, rr < binValues[i + 1]))

print(bins)