import itertools

import sys
sys.path.append('../customlib')
import custom_itertools as cit


def all_equal(iterable):
    "Returns True if all the elements are equal to each other"
    g = itertools.groupby(iterable)
    return next(g, True) and not next(g, False)


def main():
    tri = (n * (n + 1) // 2 for n in itertools.count(1))
    pent = (n * (3 * n - 1) // 2 for n in itertools.count(1))
    hex = (n * (2 * n - 1) for n in itertools.count(1))

    sim = cit.SimultaneousIterator((tri, pent, hex), keyfunc=min)
    window = cit.rolling_window(sim, 3)

    for i in itertools.islice(window, 10**6):
        if all_equal(i):
            print(i[0])

if __name__ == '__main__':
    main()




