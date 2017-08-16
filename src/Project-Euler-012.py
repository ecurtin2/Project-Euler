import sys
sys.path.append('./lib')
import factorize
import itertools

def triangle_numbers():
    for i in itertools.count(1):
        yield (i * (i + 1)) // 2

n_divisors = ((n, len(factorize.divisors(n))) for n in triangle_numbers())
it = (n for n in n_divisors if n[1] >= 500)
print(next(it))

