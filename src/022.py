"""

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
What is the total of all the name scores in the file?

"""

import string

with open('22.dat') as f:
    names = sorted(f.read().replace('"', '').split(','))

LETTER_SCORES = {s: val + 1 for val, s in enumerate(string.ascii_uppercase)}
Alphabetical_position = {s: i + 1 for i, s in enumerate(names)}


def alphabetical_value(str):
    vals = (LETTER_SCORES[char] for char in str)
    return sum(vals)


def name_score(str):
    return alphabetical_value(str) * Alphabetical_position[str]

print("Alphabetical value of COLIN = {}".format(alphabetical_value("COLIN")))
print("Score COLIN = {}".format(name_score("COLIN")))

total = sum((name_score(name) for name in names))
print("Sum of all names = {}".format(total))