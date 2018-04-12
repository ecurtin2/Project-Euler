"""

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

import argparse
import collections
import functools
import operator

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


def main():
    p = argparse.ArgumentParser(
        description="Solve Project Euler Problem 5 for input N.")
    p.add_argument('--N', type=int, default=10,
        help='The smallest number divisible by all digits below N.')
    
    variables = vars(p.parse_args())

    N = variables['N']

    counts = [collections.Counter(factorize(i)) for i in range(1, N + 1)]
    allkeys = {k for count in counts for k in count.keys()}
    max_count = {k: max(count[k] for count in counts) for k in allkeys}
    gen = (k ** v for k, v in max_count.items())
    val = functools.reduce(operator.mul, gen)

    print("The smallest number evenly divisible by  {N}".format(N=N)
        + " is {val}".format(val=val))
    

if __name__ == "__main__":
    main()
