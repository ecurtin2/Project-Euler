import itertools as it
import re

# primes won't happen for sum(digits) = multiple of 3

import sympy


def replace_str_by_dict(dic, mystring):
    """Replace all occurances of keys with corresponding values in string."""
    dic = dict((re.escape(k), v) for k, v in dic.items())
    pattern = re.compile("|".join(dic.keys()))
    mystring = pattern.sub(lambda m: dic[re.escape(m.group(0))], mystring)
    return mystring


class Number(object):

    def __init__(self, n):
        #  convert from iterable
        try:
            iterable = iter(n)
            self.val = int(''.join(str(i) for i in iterable))
            self.digits = [int(i) for i in str(self.val)]

        except TypeError:
            self.val = int(n)
            self.digits = [int(i) for i in str(self.val)]
        self.ndigits = len(self.digits)

    def replace(self, replace_dict):
        """Return number with digits replaced with replacements 'Mode' = values or 'indices'

        Mode == 'values': Replace all occurances of each key digit with each value digit
        key and val can be anything convertible to str.
        of digits with replacements. ie: Number(12315).replace({1: 6}) = Number(62365)

        Mode == 'indices': Replace digits at indices with values. If only one value is given, it will
        replace each digit at all indices.
        """
        mystr = ''.join(str(i) for i in self.digits)
        dic = {str(k): str(v) for k, v in replace_dict.items()}
        newstr = replace_str_by_dict(dic, mystr)
        return Number(newstr)

    def replace_indices(self, indices, values):
        digits = [str(i) for i in self.digits]
        try:
            iterable = iter(values)
            for idx, val in zip(indices, iterable):
                digits[idx] = val
        except TypeError:
            for idx in indices:
                digits[idx] = values
        return Number(digits)

    def masked(self, mask):
        return Number(it.compress(self.digits, mask))

    def factors(self):
        return sympy.ntheory.factorint(self.val)

    def isprime(self):
        return sympy.isprime(self.val)

    def __str__(self):
        return str(self.val)


def main():
    print("Example of Number class!")

    n = Number([1, 2, 5, 7])
    n = Number([1, 2, 5, 7])
    print('n')
    print(n)
    print('n.masked([0, 1, 1, 0])')
    print(n.masked([0, 1, 1, 0]))
    print('n.isprime()')
    print(n.isprime())
    print('n.factors()')
    print(n.factors())
    print('n.ndigits')
    print(n.ndigits)

    print("n.replace({5: 8, 2: '9'})")
    print(n.replace({5: 8, 2: '9'}))
    print("n.replace_indices([0, 2], 9)")
    print(n.replace_indices([0, 2], 9))
    print("n.replace_indices([0, 2], [8, 3])")
    print(n.replace_indices([0, 2], [8, 3]))


if __name__ == '__main__':
    main()
