# 1a)
print("1) Roman numerals")
def getRoman(i: int) -> str:
    romans = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
    return romans[i-1] if 0 < i <= 10 else "Invalid number"

for i in range(1, 11):
    print(getRoman(i))

# 1b)
def sumRoman(x: int, y: int) -> str:
    if not(0 < x <= 10 and 0 < y <= 10):
        print("Numbers must be between 1 and 10")
        return

    print(roman := getRoman(x + y))
    return roman

sumRoman(2, 4)
sumRoman(12, 3)

# 2)
print("\n2) Tribunacci")

def trib(n: int) -> int:
    # if n <= 0:
    #     return 0

    if n == 1 or n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        return trib(n-1) + trib(n-2) + trib(n-3)
    
print(trib(1))
print(trib(2))
print(trib(3))
print(trib(4))
print(trib(5))


# 3)
print("\n3) Maximum recursive")

def searchMax(l: list[int]) -> int:
    if len(l) == 1:
        return l[0]
    
    maxRight = searchMax(l[1:])
    return l[0] if l[0] > maxRight else maxRight

print(searchMax([1, 2, 3, 4, 5]))
print(searchMax([4, 3, 2, 1]))
print(searchMax([1, 3, 2, -1]))