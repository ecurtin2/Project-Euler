"""

The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
1! + 4! + 5! = 1 + 24 + 120 = 145
Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:
169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872
It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,
69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)
Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.
How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

"""

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
