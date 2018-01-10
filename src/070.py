from sympy.ntheory import totient, primerange
from collections import Counter


def is_perm(iter1, iter2):
    return Counter(iter1) == Counter(iter2)

primes = primerange(1, 10**7)

for p in primes:
    if is_perm(str(p), str(p-1)):
        print('{}, {}'.format(p, p - 1))


#phi = totient(i)

