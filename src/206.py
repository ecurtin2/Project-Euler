"""

Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0, where each “_” is a single digit.

"""

from math import floor, ceil, sqrt


def int_floor(val, to=1):
    return int(floor(float(val) / float(to))) * int(to)


form = '1_2_3_4_5_6_7_8_900'


def has_form(val):
    s = str(val)
    return s[::2] + s[-1] == '12345678900'

max_n = int_floor(sqrt(int(form.replace('_', '9'))), 10)
min_n = int_floor(sqrt(int(form.replace('_', '0'))), 10)

found = None
for n in range(min_n, max_n, 10):
    if has_form(n**2):
        found = n
        break

print(found)