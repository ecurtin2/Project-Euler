import sys
sys.path.append('../customlib')

import itertools as it

from number import Number
import sympy

primes = set(sympy.ntheory.primerange(10**5, 10**6 - 1))

vals = {}
for p in primes:
    n = Number(p)
    max_count = 0
    for mask in it.combinations(range(0, len(str(p)) - 1), 3):
        family = []
        for v in range(10):
            val = n.replace_indices(mask, v).val
            if val in primes:
                family.append(val)
        if len(family) > max_count:
            vals[p] = (mask, family)
            max_count = len(family)

k = max(vals, key=lambda k: len(vals[k][1]))
print(k, vals[k])
print(min(vals[k][1]))