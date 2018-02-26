"""

Consider the fraction, n/d, where n and d are positive integers. If n&lt;d and HCF(n,d)=1, it is called a reduced proper fraction.
If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
It can be seen that 2/5 is the fraction immediately to the left of 3/7.
By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.

"""

"""

Consider the fraction, n/d, where n and d are positive integers. If n&lt;d and HCF(n,d)=1, it is called a reduced proper fraction.
If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
It can be seen that 2/5 is the fraction immediately to the left of 3/7.
By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.

"""

from math import floor

from sympy.core.numbers import igcd

d = 10**6

dens = (i for i in range(1, d) if i != 7)
fracs = ((floor(den * 3 / 7), den) for den in dens)
proper = (f for f in fracs if igcd(*f) == 1)

frac = min(proper, key=lambda x: abs(x[0] / x[1] - 3.0 / 7.0))

print("Fraction closest to 3/7 found = {}/{} with difference = {}".format(
    frac[0], frac[1], abs(frac[0] / frac[1] - 3.0 / 7.0)
))