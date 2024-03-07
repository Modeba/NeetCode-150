from math import sqrt

def countPrimes(n):
    if n < 2:
       return 0

    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(sqrt(n)) + 2):
        for e in range(i ** 2, n, i):
            primes[e] = False
    
    res = []
    for i in range(len(primes)):
        if primes[i]:
           res.append(i)
    
    return res, len(res)

print(countPrimes(6))