import sympy as sy
import functools
import itertools as it


class CoinCounter(object):
    """Count the number of unique ways that a value can be created by summing subsets
    of a set. In other words, given list S, how many sublists s can be generated such that sum(s) == N
    Values are allowed to repeat.

    Example:
        Given coins of values 1, 2, 5, 10, 25, cents how many unique combinations of coins can be made that add up to
        $1.78?

        CC = CoinCounter((1, 2, 5, 10, 25))
        print(CC(178))
    """

    def __init__(self, iterable):
        """"""
        self._coins = sorted(list(set(iterable)))

    def count_combinations(self, n):
        k = len(set(c for c in self._coins if c <= n)) - 1
        return self._count_combs(n, k)

    @functools.lru_cache()
    def _count_combs(self, n, k):
        if n < 0 or k < 0:
            return 0
        if n == 0:
            return 1
        return self._count_combs(n, k - 1) + self._count_combs(n - self._coins[k], k)


primes = list(sy.primerange(2, 100))
C = CoinCounter(primes)
for N in it.count(2):
    if C.count_combinations(N) > 5000:
        break
print(N)

