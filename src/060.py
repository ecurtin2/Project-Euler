import sympy

primes = sympy.ntheory.primerange(1, 10**4)

for p in primes:
    digsum = sum(int(i) for i in str(p))
    if ((digsum + 3) % 3 != 0) and ((digsum + 7) % 3 != 0):
        print(p)