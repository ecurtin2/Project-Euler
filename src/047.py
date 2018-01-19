"""

The first two consecutive numbers to have two distinct prime factors are:
14 = 2 × 715 = 3 × 5
The first three consecutive numbers to have three distinct prime factors are:
644 = 2² × 7 × 23645 = 3 × 5 × 43646 = 2 × 17 × 19.
Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

"""

import sys
sys.path.append('../customlib')
import custom_itertools as cit
import sympy


def all_unique(x):
    """https://stackoverflow.com/questions/5278122/checking-if-all-elements-in-a-list-are-unique"""
    seen = set()
    return not any(i in seen or seen.add(i) for i in x)


N = 4
factor = sympy.ntheory.factorint
for i in cit.rolling_window(range(2, 10**6), N):
    factors = tuple(tuple(factor(v).keys()) for v in i)
    if all_unique(factors) and all(len(f) == N for f in factors):
        print(i)
        break

