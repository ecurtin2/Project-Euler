import itertools


class SimultaneousIterator(object):
    """Iterate through multiple iterators, using a condition to choose which is to be advanced."""

    def __init__(self, iterables, keyfunc=None):
        """Create with iterables, the keyfunc determines which iterable to be used next.

        If func is none, equivalent to
          (v for it in itertools.zip_longest(*self.iterables) for v in it if v is not None)"""

        self.iterables = list(iter(i) for i in iterables)

        if keyfunc is not None:
            self.keyfunc = keyfunc
            self.generator = self._gen_with_func()
        else:
            self.generator = (v for it in itertools.zip_longest(*self.iterables) for v in it if v is not None)

    def _gen_with_func(self):
        val_cache = [next(i) for i in self.iterables]
        while val_cache:
            val = self.keyfunc(val_cache)
            idx = val_cache.index(val)
            yield val
            try:
                val_cache[idx] = next(self.iterables[idx])
            except StopIteration:
                val_cache.pop(idx)
                self.iterables.pop(idx)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.generator)


def main():
    tri = (n * (n + 1) // 2 for n in itertools.count(1))
    pent = (n * (3 * n - 1) // 2 for n in itertools.count(1))
    hex = (n * (2 * n - 1) for n in itertools.count(1))

    for i in itertools.islice(SimultaneousIterator((tri, pent, hex), keyfunc=min), 10):
        print(i)

if __name__ == '__main__':
    main()




