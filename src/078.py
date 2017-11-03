from math import exp, pi, sqrt, exp


def n_partitions(n):
    return 1 / (4 * n * sqrt(3)) * exp(pi * sqrt(2*n / 3))


for i in range(1, 1000):
    p = n_partitions(i)
    div = p / 10**6
    if p >= (10**6 - 1.0):
        err = abs(div - round(div))

        if err < 1e-10:
            print(i, err, div)