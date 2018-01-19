"""

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
What 12-digit number do you form by concatenating the three terms in this sequence?

"""

import collections
import itertools
import pprint
import numpy as np
import sympy


def is_arithemtic(seq):
    return np.all(np.diff(seq) == np.diff(seq)[0])


primes = set(sympy.sieve.primerange(10**3 + 1, 10**4))
C = collections.Counter(tuple(sorted(str(i))) for i in primes)
possible = [k for k, v in C.items() if v >= 3]

found = []
for p in possible:
    perms = (int(''.join(perm)) for perm in itertools.permutations(p))
    prime_perms = (p for p in perms if p in primes)
    sort = sorted(set(prime_perms))
    if len(sort) == 3 and is_arithemtic(sort):
        found.append(sort)
    elif len(sort) > 3:
        for comb in itertools.combinations(sort, 3):
            if is_arithemtic(comb):
                found.append(comb)

as_str = [''.join(str(i) for i in f) for f in found]
print(as_str)