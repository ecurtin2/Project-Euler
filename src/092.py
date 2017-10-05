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
