"""

A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.
The text file, keylog.txt, contains fifty successful login attempts.
Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.

"""

from collections import defaultdict

with open("079.dat", 'r') as f:
    attempts = [line.strip() for line in f.readlines()]


rules = defaultdict(set)
for attempt in attempts:
    for i in range(len(attempt)):
        for char in attempt[i+1:]:
            rules[attempt[i]].add(char)

reverse = []
sort = sorted(rules, key=lambda k: len(rules[k]))
for k in sort:
    for i in rules[k]:
        if i not in reverse:
            reverse.append(i)


reverse.append(sort[-1])
print(''.join(reversed(reverse)))

