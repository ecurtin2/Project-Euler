"""

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

"""

import itertools
import argparse


def is_palindrome(x):
    s = str(x)
    n = len(s) // 2
    if len(s) % 2 == 0:
        return s[:n] == s[n:][::-1]
    else:
        return s[:n+1] == s[n:][::-1]

def main():
    p = argparse.ArgumentParser(
        description="Solve Project Euler Problem 4 for input N.")
    p.add_argument('--N', type=int, default=3,
        help='The largest palindrome made from the product of 2 N-digit numbers.')
    
    variables = vars(p.parse_args())

    N = variables['N']

    max_palindrome = 0
    digits = [str(i) for i in range(10)]
    for str_1 in itertools.product(digits, repeat=N):
        for str_2 in itertools.product(digits, repeat=N):
            int_1 = int(''.join(str_1))
            int_2 = int(''.join(str_2))
            val = int_1 * int_2
            if is_palindrome(val) and val > max_palindrome:
                max_palindrome = val

    print("The largest palindrome from the product of two {N}".format(N=N)
        + " digit numbers is {val}".format(val=max_palindrome))
    

if __name__ == "__main__":
    main()
