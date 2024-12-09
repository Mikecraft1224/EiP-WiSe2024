from Mittelwert_1 import advanced_mean

import time

test_list = [7,20,5,-1,3,11,32,17,42]

def simple_variance(l):
    mean = advanced_mean(l)
    summed = 0

    for i in l:
        summed += (i - mean)**2

    return summed / len(l)

def advanced_variance(l):
    mean = advanced_mean(l)

    return sum((i - mean)**2 for i in l) / len(l)

if __name__ == '__main__':
    print(f"Einfache Varianz: {simple_variance(test_list)}")
    print(f"Fortgeschrittene Varianz: {advanced_variance(test_list)}\n")

    # Achtung!
    # List comprehension ist hier langsamer, da zuerst eine Liste erstellt wird, die dann wieder durchgegangen wird
    start = time.time()
    print(f"Einfache Varianz: {simple_variance([i for i in range(10_000_000)])}")
    print(f"Time: {time.time() - start}")

    start = time.time()
    print(f"Fortgeschrittene Varianz: {advanced_variance([i for i in range(10000000)])}")
    print(f"Time: {time.time() - start}")