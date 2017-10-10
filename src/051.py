import itertools as it

# primes won't happen for sum(digits) = multiple of 3
# find a number where sum(digits) + n * (range(0, 10) has fewest multiples of 3

import sympy

ndigits = 5

cases = []
for n_replace in range(1, ndigits):
    n_left = ndigits - n_replace
    for mysum in range(n_left, 9 * n_left):
        count = 0
        for i in range(10):
            newsum = mysum + n_replace * i
            if newsum % 3 != 0:
                count += 1
        if count >= 8:
            cases.append((n_replace, mysum))

for nr, mys in cases:
    for d1 in range(1, mys):
        d2 = mys - d1
        if (d1 < 10) and (d2 < 10):
            print(d1, d2)
print(cases)