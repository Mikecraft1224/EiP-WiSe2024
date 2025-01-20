n = 5

l = [[" " for i in range(2*n)] for j in range(2*n)]

for y in range(2*n):
    for x in range(2*n):
        if (y-n) < (x-n) and (y-n) > -(x-n):
            continue
        if (y-n)**2 + (x-n)**2 < n**2:
            l[y][x] = "#"

def times3(e):
    return e*3
# => lambda e: e*3

print("\n".join(["".join(map(lambda e: e*3, sub)) for sub in l]))

for sub in l:
    for e in sub:
        print(e*3, end="")
    print()

