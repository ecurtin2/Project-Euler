from math import factorial
import itertools as it


factorials = {i: factorial(i) for i in range(10)}
digits = tuple(str(i) for i in range(10))

sum_digits = set()
for comb in it.combinations_with_replacement(digits, 6):
    num = int(''.join(comb))
    sum_digits.add(num)


cache = {}
def n_repeats(n):
    seen = []
    count = 0
    while n not in seen:
        if n in cache.keys():
            count += cache[n]
            break
        count += 1
        seen.append(n)
        n = sum(factorials[int(digit)] for digit in str(n))
    return count


for val in sum_digits:
    cache[val] = n_repeats(val)


print(sum(1 for i in range(10**6) if n_repeats(i) == 60))
