"""


Consider the divisors of 30: 1,2,3,5,6,10,15,30.
It can be seen that for every divisor d of 30, d+30/d is prime.


Find the sum of all positive integers n not exceeding 100 000 000such that
for every divisor d of n, d+n/d is prime.


"""

"""


Consider the divisors of 30: 1,2,3,5,6,10,15,30.
It can be seen that for every divisor d of 30, d+30/d is prime.


Find the sum of all positive integers n not exceeding 100 000 000such that
for every divisor d of n, d+n/d is prime.


"""

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