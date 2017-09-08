import itertools
import collections


def rolling_window(iterable, n, start=0, stop=None):
    """Return iterator over windows of size n across iterable.

    ex:
    rolling_window[range(4), 2] = (0, 1), (1, 2), (2, 3)
    """

    it1, it2 = itertools.tee(iterable, 2)
    window = tuple(itertools.islice(it1, start, start+n))
    yield window
    for nxt in itertools.islice(it2, start+n, stop):
        window = window[1:] + (nxt,)
        yield window


def outer_join(list1, list2):
    """Return all elements in both lists that aren't in both.

    Duplicate entries are considered, such that the number of duplicate
    entries returned is equal to the absolute value of the difference
    of their multiplicity difference from list1 to list2 ie:

        outer_join([1, 1, 1, 2], [1, 1, 3]) = [1, 2, 3]
    """
    c1 = collections.Counter(list1)
    c2 = collections.Counter(list2)
    d = {k: abs(c1[k] - c2[k]) for k in c1.keys() | c2.keys()}
    return [thing for k, v in d.items() for thing in [k]*v]


def inner_join(list1, list2):
    """Return all elements two iterables have in common.

    Duplicate entries are returned with the multiplicity
    of the iterable containing lower multiplicity between the two.
    """
    c1 = collections.Counter(list1)
    c2 = collections.Counter(list2)
    d = {k: min(c1[k], c2[k]) for k in c1.keys() & c2.keys()}
    return [thing for k, v in d.items() for thing in [k]*v]


def cyclic_permutations(iterable):
    """Generate tuples of cyclic permutations of iterable"""
    deque = collections.deque(iterable)
    for _ in range(len(deque)):
        yield tuple(deque)
        deque.rotate(-1)


def main():
    l1 = list(range(10))
    l2 = list(range(8, 15))
    print("l1 = {}".format(l1))
    print("l2 = {}".format(l2))
    print("outer joined = {}".format(outer_join(l1, l2)))
    print("inner joined = {}".format(inner_join(l1, l2)))
    print("Windowed iterable: ")
    print("original = {}".format(l1))
    l = list(range(5))
    l2 = list(cyclic_permutations(l))
    print("Cyclic perms of {} = {}".format(l, l2))
    for i in rolling_window(l1, 2, start=5, stop=9):
        print(i)


if __name__ == "__main__":
    main()