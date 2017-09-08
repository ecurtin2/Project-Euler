import sys
sys.path.append('./lib')
import itertools
import primes


PRIME_SET = set(v for v in itertools.islice(primes.eratosthenes(), 1000))


def func_gen(a, b):
    assert(abs(a) < 1000 and abs(b) <= 1000)

    def f(n):
        return n**2 + a * n + b
    return f


def n_consecutive_primes(f):
    gen = (f(i) for i in itertools.count())
    gen = itertools.takewhile(lambda x: x in PRIME_SET, gen)
    return len(list(gen))


max_found = (0, 0, 0)
for a in range(-999, 1000):
    for b in range(-1000, 1000):
        f = func_gen(a, b)
        n = n_consecutive_primes(f)
        if n > max_found[2]:
            max_found = (a, b, n)

print("Best function = n^2 + {a}n + {b}".format(a=max_found[0], b=max_found[1]))
print("Product of an and b =", max_found[0] * max_found[1])

