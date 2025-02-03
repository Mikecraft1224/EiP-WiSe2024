elements = [1, 2, 3]

perms = [[]]
for i in range(len(elements)):
    toAdd = []
    for perm in perms:
        for element in elements:
            new = list(set(perm + [element]))
            if element not in perm and new not in toAdd and new not in perms:
                toAdd.append(new)
    perms += toAdd

print(perms)