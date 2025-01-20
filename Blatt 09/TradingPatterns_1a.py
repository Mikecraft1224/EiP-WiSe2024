import numpy as np

raw = np.genfromtxt("Blatt 09/ethereum.csv", delimiter=",", dtype=None, names=True, encoding="utf-8")
price = raw["priceUSD"]

# Ohne names
# raw = np.genfromtxt("Blatt 09/ethereum.csv", delimiter=",")
# price = raw[:, 5]

print(price)