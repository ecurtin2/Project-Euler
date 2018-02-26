"""

Euler discovered the remarkable quadratic formula:
$n^2 + n + 41$
It turns out that the formula will produce 40 primes for the consecutive integer values $0 \le n \le 39$. However, when $n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41$ is divisible by 41, and certainly when $n = 41, 41^2 + 41 + 41$ is clearly divisible by 41.
The incredible formula $n^2 - 79n + 1601$ was discovered, which produces 80 primes for the consecutive values $0 \le n \le 79$. The product of the coefficients, −79 and 1601, is −126479.
Considering quadratics of the form:

$n^2 + an + b$, where $|a| &lt; 1000$ and $|b| \le 1000$where $|n|$ is the modulus/absolute value of $n$e.g. $|11| = 11$ and $|-4| = 4$

Find the product of the coefficients, $a$ and $b$, for the quadratic expression that produces the maximum number of primes for consecutive values of $n$, starting with $n = 0$.

"""

"""

Euler discovered the remarkable quadratic formula:
$n^2 + n + 41$
It turns out that the formula will produce 40 primes for the consecutive integer values $0 \le n \le 39$. However, when $n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41$ is divisible by 41, and certainly when $n = 41, 41^2 + 41 + 41$ is clearly divisible by 41.
The incredible formula $n^2 - 79n + 1601$ was discovered, which produces 80 primes for the consecutive values $0 \le n \le 79$. The product of the coefficients, −79 and 1601, is −126479.
Considering quadratics of the form:

$n^2 + an + b$, where $|a| &lt; 1000$ and $|b| \le 1000$where $|n|$ is the modulus/absolute value of $n$e.g. $|11| = 11$ and $|-4| = 4$

Find the product of the coefficients, $a$ and $b$, for the quadratic expression that produces the maximum number of primes for consecutive values of $n$, starting with $n = 0$.

"""

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

