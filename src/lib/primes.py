import itertools
import time


def eratosthenes(max_val=None):
    '''Yields the sequence of prime numbers via the Sieve of Eratosthenes.'''
    D = {}  # map each composite integer to its first-found prime factor
    if max_val is None:
        iterable = itertools.count(2)
    else:
        iterable = range(2, max_val + 1)
    for q in iterable:     # q gets 2, 3, 4, 5, ... ad infinitum
        p = D.pop(q, None)
        if p is None:
            # q not a key in D, so q is prime, therefore, yield it
            yield q
            # mark q squared as not-prime (with q as first-found prime factor)
            D[q*q] = q
        else:
            # let x <- smallest (N*p)+q which wasn't yet known to be composite
            # we just learned x is composite, with p first-found prime factor,
            # since p is the first-found prime factor of q -- find and mark it
            x = p + q
            while x in D:
                x += p
            D[x] = p


def main():
    t = time.time()
    l = list(eratosthenes(max_val=100))
    print(l)
    print(time.time() -  t)
    t = time.time()
    s = set(l)
    print(time.time() - t)


if __name__ == '__main__':
    main()