"""

Take the number 192 and multiply it by each of 1, 2, and 3:
192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n &gt; 1?

"""

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