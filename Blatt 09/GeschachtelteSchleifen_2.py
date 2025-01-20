import time

#       1 2 3
#       2 3 4
#       3 4 5
# 1 2 3 x x x
# 2 3 4 x x x
# 3 4 5 x x x

A = [[x for x in range(y, 200 + y)] for y in range(200)]
B = [[x for x in range(y, 200 + y)] for y in range(200)]

# 1.
def matrixMult(A, B):
    C = [[0 for x in range(len(B[0]))] for y in range(len(A))]

    for y in range(len(A)):
        for x in range(len(B[0])):
            for i in range(len(B)):
                C[y][x] += A[y][i] * B[i][x]

    return C

# 2.
# Diese Version ist schneller da sie das Ergebnis erst in einer Variable speichert 
# und dann in die Matrix schreibt.
# Das liegt daran, dass die Variable in einem CPU Register gespeichert wird 
# und somit schneller darauf zugegriffen werden kann.
# Die Matrix hingegen wird im RAM gespeichert und muss somit erst von dort geladen werden 
# und dann wieder zurückgeschrieben werden.
def matrixMult2(A, B):
    C = [[0 for x in range(len(B[0]))] for y in range(len(A))]

    for y in range(len(A)):
        for x in range(len(B[0])):
            acc = 0

            for i in range(len(B)):
                acc += A[y][i] * B[i][x]

            C[y][x] = acc

    return C


start = time.time()
matrixMult(A, B)
end = time.time()
print("matrixMult: ", end - start)

start = time.time()
matrixMult2(A, B)
end = time.time()
print("matrixMult2: ", end - start)