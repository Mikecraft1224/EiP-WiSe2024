def eratosthenesSieve(n: int) -> list[int]:
    def get_primes(primes, current):
        # current*current >= len(primes) is the same as current >= sqrt(len(primes))
        #         current >= sqrt(n)  | **2
        # current*current >= n
        if current*current >= len(primes):
            return primes
        
        if primes[current]:
            for j in range(current*current, len(primes), current):
                primes[j] = False

        return get_primes(primes, current+1)
    
    if n < 2:
        return []
    
    primes = get_primes([True]*n, 2)
    return [i for i in range(2, n) if primes[i]]

print(eratosthenesSieve(12))
print(eratosthenesSieve(100))