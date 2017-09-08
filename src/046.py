import itertools
import math

import sys
sys.path.append('../customlib')
import primes


primes = list(primes.eratosthenes(max_val=10**4))
odd_composites = (i for i in itertools.count(start=3, step=2) if i not in primes)

for v in odd_composites:
    cond = False
    for p in itertools.takewhile(lambda x: x < v, primes):
        squared = (v - p) // 2
        if math.sqrt(squared).is_integer():
            cond = True
    if not cond:
        print(v)
        break