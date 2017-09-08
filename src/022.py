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