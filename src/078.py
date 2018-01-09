import itertools as it


def pentagonals(n_max=None, n_min=0):
    if n_max is None:
        gen = it.count(n_min)
    else:
        gen = range(n_min, n_max)

    for m in gen:
        if (m % 2) == 0:
            k = m // 2 + 1
        else:
            k = - (m // 2) - 1
        yield (k * (3 * k - 1)) // 2

partitions = [1]
for n in it.count(1):
    p = 0
    signs = it.cycle((1, 1, -1, -1))
    pents_below = it.takewhile(lambda x: x <= n, pentagonals())
    for pent in pents_below:
        p += next(signs) * partitions[n - pent]
        p %= 1000000
    if p == 0:
        break
    else:
        partitions.append(p)

print(n)