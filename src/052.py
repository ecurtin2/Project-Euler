"""

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

"""

"""

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

"""

import collections
import itertools as it


def all_equal(iterable):
    "Returns True if all the elements are equal to each other"
    g = it.groupby(iterable)
    return next(g, True) and not next(g, False)


for Ndigits in range(3, 7):
    min_x = int('1' + '0' * (Ndigits - 1))
    max_x = int('9' * Ndigits) // 6
    vals = [2, 3, 4, 5, 6]

    for i in range(min_x, max_x):
        counters = [collections.Counter(char for char in str(i * v)) for v in vals]
        if all_equal(counters):
            print(i)
            break