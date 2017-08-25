import sys
sys.path.append('./lib')
import itertools

import factorize


def classify(n):
    val = sum(factorize.divisors(n)[:-1])
    if val < n:
        return 'deficient'
    elif val > n:
        return 'abundant'
    elif val == n:
        return 'perfect'
    else:
        return 'unknown'


N = 21824
abundants = set([i for i in range(1, N) if classify(i) == 'abundant'])


def is_sum_of_two_abundants(n):
    for val in abundants:
        if n - val in abundants:
            return True
    return False

val = sum(itertools.filterfalse(lambda x: is_sum_of_two_abundants(x), range(1, N)))
print(val)