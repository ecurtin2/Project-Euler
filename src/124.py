"""

The radical of n, rad(n), is the product of the distinct prime factors of n. For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.
If we calculate rad(n) for 1 ≤ n ≤ 10, then sort them on rad(n), and sorting on n if the radical values are equal, we get:
Unsorted
 
Sorted
n
rad(n)

n
rad(n)
k
11
 
111
22
 
222
33
 
423
42
 
824
55
 
335
66
 
936
77
 
557
82
 
668
93
 
779
1010
 
101010
Let E(k) be the kth element in the sorted n column; for example, E(4) = 8 and E(6) = 9.
If rad(n) is sorted for 1 ≤ n ≤ 100000, find E(10000).

"""

"""

The radical of n, rad(n), is the product of the distinct prime factors of n. For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.
If we calculate rad(n) for 1 ≤ n ≤ 10, then sort them on rad(n), and sorting on n if the radical values are equal, we get:
Unsorted
 
Sorted
n
rad(n)

n
rad(n)
k
11
 
111
22
 
222
33
 
423
42
 
824
55
 
335
66
 
936
77
 
557
82
 
668
93
 
779
1010
 
101010
Let E(k) be the kth element in the sorted n column; for example, E(4) = 8 and E(6) = 9.
If rad(n) is sorted for 1 ≤ n ≤ 100000, find E(10000).

"""

from sympy.ntheory import factorint
from functools import reduce
from operator import mul


def rad(n):
    factors = set(factorint(n).keys())
    factors.add(1)
    return reduce(mul, factors)

N = 100000
n_rad = ((rad(n), n) for n in range(1, N+1))

print(sorted(n_rad)[10000 - 1])
