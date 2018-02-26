"""

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

"""

"""

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

"""

import sympy
from math import log10, ceil
from itertools import combinations
from pprint import pprint

from sympy.ntheory import primerange, isprime


primes = set(primerange(2, 10**4))


def combine(n1, n2):
    d1 = int(ceil(log10(n1)))
    d2 = int(ceil(log10(n2)))
    return 10 ** d2 * n1 + n2, 10 ** d1 * n2 + n1


def concats_prime(iterable):
    for comb in combinations(iterable, 2):
        n1, n2 = combine(*comb)
        if not isprime(n1) or not isprime(n2):
            return False
    return True


def one_more(iterable):
    new = set(tuple(sorted(comb + (p,))) for comb in iterable for p in primes
        if concats_prime(comb + (p,)))
    return new


pairs = set(tuple(sorted(comb)) for comb in combinations(primes, 2)
            if concats_prime(comb))

pairdict = {}
for n1, n2 in pairs:
    pairdict.setdefault(n1, set()).add(n2)
    pairdict.setdefault(n2, set()).add(n1)

left = 3
tripsdict = {}
for k1, k2 in combinations(pairdict, 2):
    union = pairdict[k1] & pairdict[k2]
    new_union = set(val for val in union if concats_prime((k1, k2, val)))
    if len(new_union) >= left:
        tripsdict.setdefault(k1, {}).update({k2: new_union})
        tripsdict.setdefault(k2, {}).update({k1: new_union})

sums = []
for v1, d in tripsdict.items():
    for v2, my_set in d.items():
        pairs = []
        for v3 in my_set:
            union = pairdict[v3] & my_set
            union = set(v for v in union if concats_prime((v1, v2, v3, v)))
            if len(union) == 2:
                if concats_prime(union):
                    sums.append(v1 + v2 + v3 + sum(union))

print(min(sums))
