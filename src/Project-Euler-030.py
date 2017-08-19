import itertools


def satisfies(n, power):
    s = str(n)
    return sum(int(i)**power for i in s) == n


def gen(ndigits, power):
    vals = []
    for comb in itertools.product(range(10), repeat=ndigits):
        val = sum(v ** power for v in comb)
        s = str(val)
        digits = tuple(int(i) for i in s)
        if len(s) == ndigits:
            if digits == comb:
                vals.append(val)
    return vals


def find_max_digits(power):
    current_max = 0
    for ndigits in range(999):
        max_val = ndigits * 9 ** power
        if len(str(max_val)) < ndigits:
            return current_max
        current_max = ndigits


def get_all_nums(power):
    nums = []
    ndigits = find_max_digits(power)
    for i in range(1, ndigits + 1):
        for num in gen(i, power):
            if num != 0 and num != 1:
                nums.append(num)
    return nums

pow4 = get_all_nums(4)
print(pow4)
print(sum(pow4))
pow5 = get_all_nums(5)
print(pow5)
print(sum(pow5))