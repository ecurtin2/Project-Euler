digits = set(range(1, 10))


def concat_prod(integer, n):
    return ''.join(str(integer * i) for i in range(1, n + 1))


def is_pandigital(n):
    n = str(n)
    return len(n) == 9 and set(int(i) for i in n) == digits

vals = {}
for i in range(10**4): # max digits is 4 since will have > 1 pieces
    ndigits = len(str(i))
    max_n = 9 // ndigits
    for n in range(2, ndigits + 1):
        c = concat_prod(i, n)
        if is_pandigital(c):
            vals[(i, n)] = int(c)

max_k = max(vals, key=lambda x: vals[x])
print(max_k, vals[max_k])