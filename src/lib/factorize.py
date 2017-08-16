import functools
import math

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


def divisors(N):
    assert(N >= 1, "N must be greater than 1.")
    divisors = [1, N]
    sqrt_N = int(math.floor(math.sqrt(N))) + 1
    for i in range(2, sqrt_N):
        if N % i == 0:
            divisors.append(i)
            divisors.append(N // i)
    return sorted(list(set(divisors)))


def main():
    N = 28
    print("Prime factors of {} are {}.".format(N, list(factorize(N))))
    print("Divisors of {} are {}.".format(N, divisors(N)))

if __name__ == "__main__":
    main()