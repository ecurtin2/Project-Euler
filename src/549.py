"""


The smallest number m such that 10 divides m! is m=5.
The smallest number m such that 25 divides m! is m=10.

Let s(n) be the smallest number m such that n divides m!.
So s(10)=5 and s(25)=10.
Let S(n) be ∑s(i) for 2 ≤ i ≤ n.
S(100)=2012.


Find S(108).


"""

"""


The smallest number m such that 10 divides m! is m=5.
The smallest number m such that 25 divides m! is m=10.

Let s(n) be the smallest number m such that n divides m!.
So s(10)=5 and s(25)=10.
Let S(n) be ∑s(i) for 2 ≤ i ≤ n.
S(100)=2012.


Find S(108).


"""

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