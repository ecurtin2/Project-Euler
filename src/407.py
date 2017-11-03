import sympy

def M(n):
    if sympy.isprime(n):
        return 1
    for a in range(n, 1, -1):
        if pow(a, 2, n) == a:
            return a
    return 0


print(sum(M(n) for n in range(1, 10**7)))