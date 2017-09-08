import sys
sys.path.append('./lib')

import factorize


def d(n):
    """defined in the problem"""
    return sum(factorize.divisors(n)[:-1])

print("d(220) = {}".format(d(220)))

N = 10000
dlist = ((a, d(a)) for a in range(1, N))

amicable_nums = set()
for a, da in dlist:
    b = da
    db = d(b)
    if db == a and a != b:
        amicable_nums.add(a)
        amicable_nums.add(b)

print(sum(amicable_nums))