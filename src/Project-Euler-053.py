from math import factorial


def C(n, r):
    assert(r <= n)
    return int(factorial(n) / (factorial(r) * factorial(n - r)))

N = sum(1 for n in range(23, 101) for r in range(n) if C(n, r) > 10**6)
print(N)