import time

def timedef(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter_ns()
        result = func(*args, **kwargs)
        end = (time.perf_counter_ns() - start) / 1000000000
        print(f"Function {func.__name__} took {end:f} seconds")
        return result
    return wrapper

weights = [8,15,1,14,77,13,15,21,13]
max_weight = 96

n = len(weights)
table = [[0 for _ in range(max_weight+1)] for _ in range(n+1)]

@timedef
def checkSubsetsDynamic():
    for i in range(1, max_weight + 1):
        for j in range(1, n + 1):
            if weights[j-1] > i:
                table[j][i] = table[j-1][i]
            else:
                table[j][i] = max(table[j-1][i], table[j-1][i-weights[j-1]] + weights[j-1])

    return table[n][max_weight]

print(checkSubsetsDynamic())