import time

arr = [i for i in range(10_000_000)]
num = -1

# 1.
def allGreater(arr, num):
    for n in arr:
        if n <= num:
            return False
    
    return True

# 2.
# Diese Version berechnet für jede Zahl, ob diese größer ist, 
# und kombiniert diese dann mit dem all Operator, ob dies für alle gilt.
# Jedoch ist der traditionelle Weg schneller, da dieser abbricht, 
# sobald eine Zahl kleiner oder gleich der gegebenen Zahl ist 
# und all zusätzliche Laufzeit benötigt.
allGreaterV2 = lambda arr, num: all(n > num for n in arr)


start = time.time()
print(allGreater(arr, num))
end = time.time()
print("Laufzeit: ", end - start)

start = time.time()
print(allGreaterV2(arr, num))
end = time.time()
print("Laufzeit: ", end - start)