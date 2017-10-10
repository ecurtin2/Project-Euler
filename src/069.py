import itertools as it
import operator


from sympy.ntheory.generate import sieve


prime_products = it.accumulate(it.islice(sieve, 1, 10), operator.mul)

for i in it.takewhile(lambda x: x <= 10**6, prime_products):
    val = i
print(val)