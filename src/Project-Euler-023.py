import sys
sys.path.append('./lib')

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


for i in range(30):
    print(i, classify(i))