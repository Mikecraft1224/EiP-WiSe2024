import time

shoe=["vans", "boots", "chucks", "heels"]
shirts=["dotted red shirt", "elegant black shirt", "trashy pink shirt"]
pants=["jeans", "jogging pants", "yoga pants", "shorts"]

# 1.
def allPermutations(shoes, shirts, pants):
    perms = []

    # Würde Duplikate entfernen, falls es welche geben sollte.
    # shoes, shirts, pants = list(set(shoes)), list(set(shirts)), list(set(pants))

    for shoe in shoes:
        for shirt in shirts:
            for pant in pants:
                perms.append([shoe, shirt, pant])
    
    return perms

# 2.
# Auch hier ist die List Comprehension noch ein wenig langsamer als die normale for-Schleife, 
# jedoch nicht so siginifikant, da hierbei die Liste sowieso erstellt werden muss.
# Vor allem bei so kleinen Listen wie hier, ist der Unterschied nicht erkennbar.
def allPermutations2(shoes, shirts, pants):
    return [[shoe, shirt, pant] for shoe in shoes for shirt in shirts for pant in pants]


start = time.time()
perms = allPermutations(shoe, shirts, pants)
end = time.time()
print("Time for allPermutations: ", end - start)

start = time.time()
perms2 = allPermutations2(shoe, shirts, pants)
end = time.time()
print("Time for allPermutations2: ", end - start)