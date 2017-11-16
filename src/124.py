from sympy.ntheory import factorint
from functools import reduce
from operator import mul


def rad(n):
    factors = set(factorint(n).keys())
    factors.add(1)
    return reduce(mul, factors)

N = 100000
n_rad = ((rad(n), n) for n in range(1, N+1))

print(sorted(n_rad)[10000 - 1])
