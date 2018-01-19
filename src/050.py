"""

The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.
The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
Which prime, below one-million, can be written as the sum of the most consecutive primes?

"""

import itertools as it
import math


import sympy


def gen_solutions(N):
    primes = list(sympy.ntheory.generate.sieve.primerange(2, N))
    prime_set = set(primes)
    M = len(primes)
    max_start = int(math.floor(math.sqrt(M)))
    for start in range(max_start):
        windowed_accumulate = it.accumulate(it.islice(primes, start, M))
        max_from_start = max((idx+1, v) for idx, v in enumerate(windowed_accumulate) if v in prime_set)
        yield max_from_start


Ns = [10**2, 10**3, 10**6]
for N in Ns:
    nterms, val = max(gen_solutions(N), key=lambda x: x[0])
    print(("The number below {} that can be written as the most consecutive"
          + " primes contains {} terms, and is {}.").format(N, nterms, val))
