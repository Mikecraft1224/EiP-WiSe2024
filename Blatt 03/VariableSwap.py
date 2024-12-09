# 1)

# Das gegebene Programm kann nicht die beiden Variablen vertauschen,
# da x mit y überschrieben wird und somit der Wert von x verloren geht.
# Somit wird am Ende x = 15 und y = 15 sein.


# 2)

x = 5
y = 15

# Vertauschen der Werte
tmp = x
x = y
y = tmp

# Tuple unpacking
x, y = y, x  # Pythonic
