"""


If we calculate a2 mod 6 for 0 ≤ a ≤ 5 we get: 0,1,4,3,4,1.


The largest value of a such that a2 ≡ a mod 6 is 4.
Let's call M(n) the largest value of a &lt; n such that a2 ≡ a (mod n).
So M(6) = 4.


Find ∑M(n) for 1 ≤ n ≤ 107.


"""

import sympy

def M(n):
    if sympy.isprime(n):
        return 1
    for a in range(n, 1, -1):
        if pow(a, 2, n) == a:
            return a
    return 0


print(sum(M(n) for n in range(1, 10**7)))