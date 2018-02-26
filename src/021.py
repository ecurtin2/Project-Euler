"""

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.

"""

"""

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.

"""

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