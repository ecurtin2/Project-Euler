from sympy.ntheory import sieve
from sympy import isprime, divisors

primes = sieve.primerange(1, 10**8)
candidates = (p - 1 for p in primes)


def condition(n):
    for d in divisors(n):
        v = int(d + n / d)
        if not isprime(v):
            return False
    return True

#print(sum(val for val in candidates if condition(val)))