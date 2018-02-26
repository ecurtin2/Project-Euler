"""

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12
It turns out that the conjecture was false.
What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

"""

"""

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12
It turns out that the conjecture was false.
What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

"""

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