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

@timedef
def checkAllSubsets():
    best_subset = []

    def checkSubsets(subset:list=[], idx=0):
        if sum(subset) <= max_weight and sum(subset) > sum(best_subset):
            best_subset[:] = subset[:]
        if idx >= len(weights):
            return
        
        for b in [True, False]:
            if b:
                subset.append(weights[idx])
            checkSubsets(subset, idx+1)
            if b:
                subset.pop()

    checkSubsets()
    return best_subset

print(checkAllSubsets())