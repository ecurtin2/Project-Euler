import math

with open('099.dat') as f:
    pairs = f.read().splitlines()


def logvals():
    for i, pair in enumerate(pairs):
        base, exp = (int(i) for i in pair.split(','))
        yield i + 1, exp * math.log(base)


print(max(logvals(), key=lambda x: x[1]))
