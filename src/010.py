"""

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

"""

from sympy import sieve

N = 2e6
print(sum(sieve.primerange(0, N)))
