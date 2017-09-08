import itertools
from string import ascii_uppercase


with open('42.dat', 'r') as f:
    s = f.read().replace('"', '')
    words = [i.upper() for i in s.split(',')]

alpha = list(ascii_uppercase)


def let_2_num(char):
    return alpha.index(char) + 1


def word_2_num(word):
    return sum(let_2_num(c) for c in word.upper())


word_vals = [word_2_num(word) for word in words]
max_val = max(word_vals)
tri_gen = ((n * (n + 1)) // 2 for n in itertools.count(1))
triangles = set(itertools.takewhile(lambda x: x <= max_val, tri_gen))

print(sum(1 for val in word_vals if val in triangles))