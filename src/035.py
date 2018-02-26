"""

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?

"""

"""

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?

"""

import sys
sys.path.append("./lib")

import primes
import custom_itertools as cit


N = 10**2
primes = set(primes.eratosthenes(max_val=N))
nums = (str(i) for i in range(N))
found = set()
for num in nums:
    perms_are_prime = (int(''.join(perm)) in primes for perm in cit.cyclic_permutations(num))
    if all(perms_are_prime):
        found.add(int(''.join(num)))

print(len(found))
