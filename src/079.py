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

