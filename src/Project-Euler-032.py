from itertools import permutations
digits = tuple(str(i) for i in range(1, 10))


n = len(digits)
found = set()
for n1 in range(1, n - 1):
    for n2 in range(1, n - n1):
        n3 = n - n1 - n2
        for num1 in permutations(digits, n1):
            dig2 = tuple(sorted(set(digits) - set(num1)))
            for num2 in permutations(dig2, n2):
                dig3 = set(dig2) - set(num2)
                s1 = ''.join(num1)
                s2 = ''.join(num2)
                int1 = int(s1)
                int2 = int(s2)
                int3 = int1 * int2
                s3 = str(int3)
                concat = ''.join((s1, s2, s3))
                if len(concat) == 9 and set(s3) == dig3:
                    found.add(int3)
print(found)
print(sum(found))