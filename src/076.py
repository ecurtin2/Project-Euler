"""

It is possible to write five as a sum in exactly six different ways:
4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1
How many different ways can one hundred be written as a sum of at least two positive integers?

"""

from scipy.misc import comb
import functools

@functools.lru_cache()
def nsums(n):
    if n == 1 or n == 2:
        return 1
    pairs = list((i, n - i) for i in range(1, n//2 + 1))
    return len(pairs) + nsums(pairs[0][0]) + nsums(pairs[-1][1])

print(nsums(100))
