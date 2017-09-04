def is_palindrome(x):
    s = str(x)
    n = len(s) // 2
    if len(s) % 2 == 0:
        return s[:n] == s[n:][::-1]
    else:
        return s[:n+1] == s[n:][::-1]

total = 0
for i in range(10**6):
    bin = "{0:b}".format(i)
    if is_palindrome(i) and is_palindrome(bin):
        total += i

print(total)