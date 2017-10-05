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