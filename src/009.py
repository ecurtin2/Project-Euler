"""

A Pythagorean triplet is a set of three natural numbers, a &lt; b &lt; c, for which,
 a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.Find the product abc.

"""

N = 1000
for b in range(N):
    for a in range(b):
        c = N - a - b
        if (a < b < c) and (a**2 + b**2 == c**2):
            print("Triplet = {}, {}, {}, product = {}".format(
                a, b, c, a * b * c))