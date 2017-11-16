from math import gcd


def f(d):
    total = 0
    for d in range(4, d + 1):
        n_min = d // 3 + 1
        n_max = d // 2

        for n in range(n_min, n_max + 1):
            if gcd(n, d) == 1:
                total += 1
    return total

print(f(12000))


