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