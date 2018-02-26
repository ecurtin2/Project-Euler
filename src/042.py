"""

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

"""

"""

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

"""

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