"""

The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
Find the smallest cube for which exactly five permutations of its digits are cube.

"""

"""

The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
Find the smallest cube for which exactly five permutations of its digits are cube.

"""

import collections
import itertools as it


N = 1000
cubes = (i**3 for i in it.count(1))
counter = collections.defaultdict(tuple)

found = None
for i in cubes:
    key = tuple(sorted(str(i)))
    counter[key] += (i,)
    if len(counter[key]) == 5:
        found = key
        break

print(min(counter[found]))