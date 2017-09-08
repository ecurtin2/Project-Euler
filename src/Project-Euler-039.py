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