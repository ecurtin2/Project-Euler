import itertools as it
from sympy import isprime

# Cannot be a 9 digit pandigital since sum(1..9) = 45 making it divisible by 3
# same for 8 and 6, 5, 3, 2. We also know a 4 digit exists from the problem.

# The numbers ending in 2, 4, 6 and 5 are automatically not prime by being even or divisible by 5


def largest_pandigital_prime(ndigits):
    digits = ''.join(str(i) for i in range(ndigits, 0, -1))
    for perm in it.permutations(digits):  # permute in descending order - max will be first found
        num = int(''.join(perm))
        if isprime(num):
            return num

found = largest_pandigital_prime(7)
if found is not None:
    print(found)
else:
    print(largest_pandigital_prime(4))
