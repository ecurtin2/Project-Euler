@functools.lru_cache()
def factorize(n):
"""Generate the prime factors of integer n."""
    if n < 0:
        yield -1
        n *= -1
    elif n > 2:
        i = 2
        while n % i != 0 and i <= n:
            i += 1
                
        yield i
        yield from factorize(n // i)        
    else:
        yield n
