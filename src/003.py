"""

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

"""

import argparse
import itertools

def factorize(n):
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
        description="Solve Project Euler Problem 2 for input N.")
    p.add_argument('--N', type=int, default=600851475143,
        help='The upper bound (inclusive) of the fibonacci sequence considered.')
    
    variables = vars(p.parse_args())

    N = variables['N']

    factors = list(factorize(N))
    max_factor = max(factors)
    print("The highest prime factor of {N} is {val}".format(N=N, val=max_factor))
    print("All prime factors are {}.".format(factors))
    

if __name__ == "__main__":
    main()
