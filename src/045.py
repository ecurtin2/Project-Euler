"""

Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
Triangle
 
Tn=n(n+1)/2
 
1, 3, 6, 10, 15, ...
Pentagonal
 
Pn=n(3n−1)/2
 
1, 5, 12, 22, 35, ...
Hexagonal
 
Hn=n(2n−1)
 
1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.
Find the next triangle number that is also pentagonal and hexagonal.

"""

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




