"""

It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.
12 cm: (3,4,5)24 cm: (6,8,10)30 cm: (5,12,13)36 cm: (9,12,15)40 cm: (8,15,17)48 cm: (12,16,20)
In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.
120 cm: (30,40,50), (20,48,52), (24,45,51)
Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?

"""
from math import sqrt, ceil
import numba
import numpy as np
from time import time


N = 1500000


@numba.jit(nopython=True, cache=True)
def gcd(a: int, b: int) -> int:
    if b:
        return gcd(b, a % b)
    else:
        return a


@numba.jit(numba.int32[:, :](numba.int32), nopython=True, cache=True)
def pythagorean_triples(max_perimeter):
    max_m = int(sqrt(max_perimeter / 2))
    triples = np.zeros((10 * max_m ** 2, 3), dtype=np.int32)
    count = 0
    for m in range(2, max_m):
        for n in range(1, m):
            if ((n + m) % 2 == 1) and (gcd(n, m) == 1):
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2

                for k in range(1, int(ceil(max_perimeter / (a + b + c)))):
                    if (k*a + k*b + k*c) <= max_perimeter:
                        triples[count] = np.array((k*a, k*b, k*c))
                        count += 1
    triples = triples[:count]
    return triples


t = time()
trips = pythagorean_triples(N)
unique, counts = np.unique(np.sum(trips, axis=1), return_counts=True)
answer = np.sum(counts == 1)
t = time() - t
print("Answer {} computed in {} seconds.".format(answer, t))

