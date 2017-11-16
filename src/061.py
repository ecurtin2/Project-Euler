import itertools as it


def take_between(predicate, iterable):
    """Dress iterator starting when first true and stopping thereafter when first false."""
    dropped = it.dropwhile(lambda x: not predicate(x), iterable)
    return it.takewhile(predicate, dropped)

pred = lambda x: len(str(x)) == 4

polys = {
    'triangles': set(take_between(pred, ((n * (n + 1)) // 2 for n in it.count()))),
    'squares': set(take_between(pred, (n ** 2 for n in it.count()))),
    'pents': set(take_between(pred, ((n * (3 * n - 1)) // 2 for n in it.count()))),
    'hexs': set(take_between(pred, (n * (2 * n - 1) for n in it.count()))),
    'hepts': set(take_between(pred, ((n * (5 * n - 3)) // 2 for n in it.count()))),
    'octs': set(take_between(pred, (n * (3 * n - 2) for n in it.count()))),
}

firstdigits = [str(i) for i in range(1, 10)]
seconddigits =[str(i) for i in range(10)]


def gen_cycles(num, ncycles=3):
    A, B, C, D = str(num)
    ABCD = num

    for firsts in it.product(firstdigits, repeat=ncycles-2):
        for second in it.product(seconddigits, repeat=ncycles-2):
            xyAB = int(firsts[0] + second[0] + A + B)
            CDxy = int(C + D + firsts[0] + second[0])
            yield (ABCD, xyAB, CDxy)


def one_to_one(sets, vals):
    """True if each val is in exactly one set and each set contains exactly one value"""
    for s in sets:
        if len(s & set(vals)) != 1:
            return False
    for v in vals:
        if sum(v in s for s in sets) != 1:
            return False
    return True

for tri in polys['triangles']:
    for cycle in gen_cycles(tri):
        if one_to_one(polys.values(), cycle):
            print(cycle)

