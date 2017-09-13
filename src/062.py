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