from math import factorial
import collections
import itertools


for i in range(1, 15):
    if factorial(9) * i < factorial(i):
        max_digits = i
        break

total = 0
for ndigits in range(2, max_digits + 1):
    for comb in itertools.combinations_with_replacement(range(10), ndigits):
        mysum = str(sum(factorial(i) for i in comb))
        if len(mysum) == ndigits:
            cmysum = collections.Counter(mysum)
            num = ''.join(str(i) for i in comb)
            cnum = collections.Counter(num)
            if cnum == cmysum:
                print(mysum)
                total += int(mysum)
print(total)