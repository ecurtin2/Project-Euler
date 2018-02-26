"""

For a number written in Roman numerals to be considered valid there are basic rules which must be followed. Even though the rules allow some numbers to be expressed in more than one way there is always a "best" way of writing a particular number.
For example, it would appear that there are at least six ways of writing the number sixteen:
IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI
However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most efficient, as it uses the least number of numerals.
The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid, but not necessarily minimal, Roman numerals; see About... Roman Numerals for the definitive rules for this problem.
Find the number of characters saved by writing each of these in their minimal form.
Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.

"""

"""

For a number written in Roman numerals to be considered valid there are basic rules which must be followed. Even though the rules allow some numbers to be expressed in more than one way there is always a "best" way of writing a particular number.
For example, it would appear that there are at least six ways of writing the number sixteen:
IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI
However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most efficient, as it uses the least number of numerals.
The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid, but not necessarily minimal, Roman numerals; see About... Roman Numerals for the definitive rules for this problem.
Find the number of characters saved by writing each of these in their minimal form.
Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.

"""

import re


def replace_str_by_dict(dic, mystring):
    """Replace all occurances of keys with corresponding values in string."""
    dic = dict((re.escape(k), v) for k, v in dic.items())
    pattern = re.compile("|".join(dic.keys()))
    mystring = pattern.sub(lambda m: dic[re.escape(m.group(0))], mystring)
    return mystring

replacements = {'VIIII': 'IX', 'IIII': 'IV', 'LXXXX': 'XC', 'XXXX': 'XL', 'DCCCC': 'CM', 'CCCC': 'CD'}
with open('089.dat') as f:
    s = f.read()
    s2 = replace_str_by_dict(replacements, s)
    print(len(s) - len(s2))



'''
Less trolly version

from collections import OrderedDict
import re

with open('089.dat') as f:
    numerals = [line.strip() for line in f.readlines()]

NUMERALS = {
    'I': '1:',
    'V': '5:',
    'X': '10:',
    'L': '50:',
    'C': '100:',
    'D': '500:',
    'M': '1000:',
}
SUBTRACTIVE_PAIRS = {
    'IV': '4:',
    'IX': '9:',
    'XL': '40:',
    'XC': '90:',
    'CD': '400:',
    'CM': '900:',
}
BOTH = OrderedDict()
unsorted = {**NUMERALS, **SUBTRACTIVE_PAIRS}
for k in sorted(unsorted, key=lambda k: int(unsorted[k].replace(':', '')), reverse=True):
    BOTH[k] = int(unsorted[k].replace(':', ''))


def numeral_to_int(numeral):
    nums = replace_str_by_dict(NUMERALS, replace_str_by_dict(SUBTRACTIVE_PAIRS, numeral))
    return sum(int(i) for i in nums.split(':') if i != '')


def highest_numeral_below(n):
    for numeral, val in BOTH.items():
        if val <= n:
            return numeral, val


def int_to_shortest_numeral(n):
    _numerals = []
    while n > 0:
        numeral, val = highest_numeral_below(n)
        _numerals.append(numeral)
        n -= val
    return ''.join(_numerals)


total_saved = 0
for n in numerals:
    val = numeral_to_int(n)
    short = int_to_shortest_numeral(val)
    total_saved += len(n) - len(short)
print(total_saved)
'''