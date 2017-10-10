import sys
sys.path.append('../customlib')
import custom_itertools as cit
import itertools as it


def take_between(predicate, iterable):
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

allvals = set(v for vals in polys.values() for v in vals)

reduced = {}
for k, s in polys.items():
    others = (key for key, v in polys.items() if key != k)
    reduced[k] = s.difference(*others)
    print(k, sorted(reduced[k]))