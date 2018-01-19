"""

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?

"""

import operator
from collections import Counter
from math import factorial
import functools

def n_permutations(l):
    num = factorial(len(l))
    mults = Counter(l).values()
    den = functools.reduce(operator.mul, (factorial(v) for v in mults), 1)
    return num // den


N = 20
l = [1] * N + [0] * N
npermutations(l)