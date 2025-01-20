import numpy as np

# dtype muss hier auf none gesetzt werden, da sonst das date als float interpretiert wird und somit nan wird
# das encoding muss auf utf8 gesetzt werden, da sonst das datum als byte interpretiert wird und somit aus 2015-10-06 b'2015-10-06' wird
raw = np.genfromtxt("Blatt 09/ethereum.csv", delimiter=",", names=True, dtype=None, encoding="utf8")
date = raw["date"]
price = raw["priceUSD"]

def is_double_top(arr_part, tolerance=0.01):
    return arr_part[0] < arr_part[1] \
            and arr_part[1] > arr_part[2] \
            and arr_part[2] < arr_part[3] \
            and abs(arr_part[1] - arr_part[3]) < tolerance

for i in range(0, len(price) - 3):
    if is_double_top(price[i:i+4]):
        print(f"double top pattern found: {date[i]}")