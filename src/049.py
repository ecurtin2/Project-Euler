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