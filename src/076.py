from scipy.misc import comb
import functools

@functools.lru_cache()
def nsums(n):
    if n == 1 or n == 2:
        return 1
    pairs = list((i, n - i) for i in range(1, n//2 + 1))
    return len(pairs) + nsums(pairs[0][0]) + nsums(pairs[-1][1])

print(nsums(100))
