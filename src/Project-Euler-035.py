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
