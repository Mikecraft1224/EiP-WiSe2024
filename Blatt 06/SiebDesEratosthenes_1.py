def eratosthenesSieve(n: int) -> list[int]:
    if n < 2:
        return []
    
    primes = [True] * n
    primes[0] = primes[1] = False
    
    for i in range(2, int(n**0.5)+1):
        if not primes[i]:
            continue
    
        for j in range(i*i, n, i):
            primes[j] = False
    
    return [i for i in range(n) if primes[i]]

print(eratosthenesSieve(12))
print(eratosthenesSieve(100))