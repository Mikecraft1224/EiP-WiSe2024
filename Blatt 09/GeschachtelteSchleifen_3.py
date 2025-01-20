A = [[x for x in range(y, 200 + y)] for y in range(200)]

def diagonalSum(A):
    acc = 0

    for i in range(len(A)):
        acc += A[i][i]

    return acc

print(diagonalSum(A))