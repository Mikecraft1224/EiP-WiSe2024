def eratosthenesSieve(n: int) -> list[int]:
    def rm_multiples(primes, nbr, current):
        if current >= len(primes):
            return primes
        
        primes[current] = False

        return rm_multiples(primes, nbr, current+nbr)

    def get_primes(primes, current):
        if current*current >= len(primes):
            return primes
        
        if primes[current]:
            primes = rm_multiples(primes, current, current*current)

        return get_primes(primes, current+1)
    
    if n < 2:
        return []
    
    primes = get_primes([True]*n, 2)
    return [i for i in range(2, n) if primes[i]]

print(eratosthenesSieve(12))
print(eratosthenesSieve(100))