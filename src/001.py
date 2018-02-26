"""

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

"""

"""

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

"""

import numpy as np
import argparse

def main():
    p = argparse.ArgumentParser(
        description="Solve Project Euler Problem 1 for input N.")
    p.add_argument('integer', metavar='N', type=int, 
        help='The upper bound (exclusive) of the natural numbers considered.')
    
    variables = vars(p.parse_args())

    N = variables['integer']

    nums = np.arange(N)
    print(np.sum(nums * np.logical_or(nums % 3 == 0, nums % 5 == 0)))

if __name__ == "__main__":
    main()
