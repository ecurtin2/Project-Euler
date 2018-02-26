"""

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
For which value of p ≤ 1000, is the number of solutions maximised?

"""

"""

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
For which value of p ≤ 1000, is the number of solutions maximised?

"""

import itertools
import math


def pythagorean_triples(max_sum=120):
    for a in range(1, max_sum):
        for b in range(1, a + 1):
            c = math.sqrt(a**2 + b**2)
            if c.is_integer():
                c = int(c)
                if a + b + c <= max_sum:
                    yield (a, b, c)


s = sorted(pythagorean_triples(max_sum=1000), key=lambda x: sum(x))
d = {}
for k, g in itertools.groupby(s, key=lambda x: sum(x)):
    d[k] = len((tuple(g)))

print(max(d, key=lambda k: d[k]))