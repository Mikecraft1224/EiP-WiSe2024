import numpy as np

a = np.arange(42, 420)

summed = np.sum(a)
print(summed)

# Gibt 0 zurück, da es hierbei zu einem Overflow kommt => das Ergebnis ist zu groß für den Datentyp
mult = np.prod(a)
print(mult)