import itertools
import functools
import math
import time

import primes


class Factorize(object):

    def __init__(self, max_val=10e5):
        self.max_val = 0
        self.primes = []
        self.prime_set = set(self.primes)
        self.prime_gen = primes.eratosthenes()
        self.update_primes(max_val)
        print(self.primes)
        print(self.prime_set)

    def update_primes(self, new_max):
        if self.max_val < new_max:
            self.max_val = new_max
            primes = list(itertools.takewhile(lambda x: x <= self.max_val, self.prime_gen))
            prime_set = set(primes)
            self.primes += primes
            self.prime_set = self.prime_set | prime_set

    #@functools.lru_cache()
    def __call__(self, n):
        """Generate the prime factors of integer n."""
        self.update_primes(new_max=n)
        if n < 0:
            yield -1
            n *= -1
        elif n in self.prime_set:
            yield n
            raise StopIteration

        elif n > 2:
            idx = 0
            div = self.primes[idx]
            while n % div != 0 and div <= int(math.floor(math.sqrt(n))):
                idx += 1
                div = self.primes[idx]

            yield div
            yield from self.__call__(n // div)
        elif n == 2:
            yield n
            yield 1
        elif n == 1:
            yield 1


def divisors(N):
    assert(N >= 1)
    divisors = [1, N]
    sqrt_N = int(math.floor(math.sqrt(N))) + 1
    for i in range(2, sqrt_N):
        if N % i == 0:
            divisors.append(i)
            divisors.append(N // i)
    return sorted(list(set(divisors)))


def main():
    N = 28
    max_val = 10
    f = Factorize(max_val=max_val)
    t = time.time()
    for i in range(2, max_val):
        x = list(f(i))
        print(i, x)
    print(time.time() - t)
    print("Divisors of {} are {}.".format(N, divisors(N)))

if __name__ == "__main__":
    main()