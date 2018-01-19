"""

A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.
For example,
44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.
How many starting numbers below ten million will arrive at 89?

"""

import functools


@functools.lru_cache()
def chain(n):
    n = sum(int(i)**2 for i in str(n))
    if n == 1:
        return 1
    elif n == 89:
        return 89
    else:
        return chain(n)

print(sum((chain(i) == 89 for i in range(1, 10**7))))
