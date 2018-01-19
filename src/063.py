"""

The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.
How many n-digit positive integers exist which are also an nth power?

"""

import itertools as it
from math import floor, ceil

count = 0
for ndigits in it.count(1):
    smallest = 10**(ndigits - 1)
    largest  = 10**(ndigits) - 1

    smallbase = int(ceil(smallest ** (1.0 / ndigits)))
    largebase = int(floor(largest ** (1.0 / ndigits)))
    if largebase == 10:  # 10 can never be a solution
        largebase -= 1
    npows = largebase - smallbase + 1


    for base in range(smallbase, largebase + 1):
        print("{} ^ {} = {}".format(base, ndigits, base ** ndigits))

    count += npows
    if npows == 0:
        break

print(count)