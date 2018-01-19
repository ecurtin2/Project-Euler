"""

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

"""

import sympy

primes = sympy.ntheory.primerange(1, 10**4)

for p in primes:
    digsum = sum(int(i) for i in str(p))
    if ((digsum + 3) % 3 != 0) and ((digsum + 7) % 3 != 0):
        print(p)