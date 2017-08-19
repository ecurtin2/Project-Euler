import functools
import time


class CoinCounter(object):

    def __init__(self, coins={1, 2, 5, 10, 20, 50, 100, 200}):
        self._coins = sorted(list(set(coins)))

    def __call__(self, n):
        k = len(set(c for c in self._coins if c <= n)) - 1
        return self.count_combs(n, k)

    @functools.lru_cache()
    def count_combs(self, n, k):
        if n < 0 or k < 0:
            return 0
        if n == 0:
            return 1
        return self.count_combs(n, k - 1) + self.count_combs(n - self._coins[k], k)

C = CoinCounter()
t = time.time()
c = C(200)
t = time.time() - t
print("Counted {} combinations for n = {} in {} seconds".format(c, 200, t))