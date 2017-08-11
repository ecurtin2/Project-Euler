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
