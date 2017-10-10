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