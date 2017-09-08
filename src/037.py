import itertools
import pprint

import sys
sys.path.append('./lib')
import primes

p = primes.eratosthenes(max_val=10**6)
dleft = {}
dright = {}
d = {}
for k, g in itertools.groupby(p, key=lambda x: len(str(x))):
    l = list(str(i) for i in g)
    if k == 1:
        dleft[k] = set(l)
        dright[k] = set(l)
    else:
        lprev = dleft[k - 1]
        rprev = dright[k - 1]
        dleft[k] = set(i for i in l if i[1:] in lprev)
        dright[k] = set(i for i in l if i[:-1] in rprev)
        d[k] = dleft[k] & dright[k]
pprint.pprint(d)
val = sum(int(i) for v in d.values() for i in v)
print("Total =", val)
