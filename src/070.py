"""

Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.The number 1 is considered to be relatively prime to every positive number, so φ(1)=1. 
Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.
Find the value of n, 1 &lt; n &lt; 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.

"""

from sympy.ntheory import totient, primerange
from collections import Counter


def is_perm(iter1, iter2):
    return Counter(iter1) == Counter(iter2)

primes = primerange(1, 10**7)

for p in primes:
    if is_perm(str(p), str(p-1)):
        print('{}, {}'.format(p, p - 1))


#phi = totient(i)

