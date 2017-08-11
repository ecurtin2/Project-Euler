import argparse
import functools
import itertools

@functools.lru_cache()
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2) 

def fibonacci_under(n):
    i = 0
    val = fibonacci(0)
    while val < n:
        val = fibonacci(i)
        yield val
        i += 1
 
def main():
    p = argparse.ArgumentParser(
        description="Solve Project Euler Problem 2 for input N.")
    p.add_argument('integer', metavar='N', type=int, 
        help='The upper bound (inclusive) of the fibonacci sequence considered.')
    
    variables = vars(p.parse_args())

    N = variables['integer']

    fibs = fibonacci_under(N)
    even_fibs = itertools.filterfalse(lambda x: x%2, fibs)
    print(sum(even_fibs))
    

if __name__ == "__main__":
    main()
