from sympy import factorint
from sympy.ntheory import primerange
from collections import Counter


N = 10**2 + 1

#print(set(primes))

def s(n):
    factors = factorint(n)
    val = max(factors)
    return val * factors[val]


def factorial_factors(n):
    print(sum(Counter(factorint(i)) for i in range(2, N)))


def S(n):
    primes = set(primerange(2, n + 1))
    return sum(s(i) for i in range(2, n + 1))

print(factorial_factors(10))