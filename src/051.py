"""

By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.
Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

"""

"""

By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.
Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

"""

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