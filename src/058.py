import itertools as it


from sympy import isprime


# bottom-right diags are never prime, since they are always square numbers

nprimes = 0
for i in it.count(1, 2):
    diags = range(i**2 + i + 1, (i + 2)**2, i + 1)
    nprimes += sum(isprime(n) for n in diags)
    nrows = i + 2
    ndiags = 2 * nrows - 1
    percent = 100 * nprimes / ndiags

    if percent < 10.0:
        print(nrows)
        break
