"""

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

"""

import itertools as it
import sys
sys.path.append('./lib')
import primes

N = 2e6
val = sum(it.takewhile(lambda x: x < N, primes.eratosthenes()))
print(val)