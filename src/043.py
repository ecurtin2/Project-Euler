import itertools


def has_property(n):
    s = str(n)
    dens = [2, 3, 5, 7, 11, 13, 17]

    for idx, i in enumerate(range(1, 8)):
        num = int(s[i:i+3])
        if num % dens[idx] != 0:
            return False
    return True

digits = (str(i) for i in range(10))
perms = (i for i in itertools.permutations(digits))
nums = (int(''.join(perm)) for perm in perms)
print(sum(i for i in nums if has_property(i)))
