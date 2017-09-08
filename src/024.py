import itertools

nums = range(10)
M = 1000000

count = 1
for val in itertools.permutations(nums):
    if count == M:
        break
    count += 1
print(''.join(str(i) for i in val))