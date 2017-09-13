def is_palindrome(x):
    s = str(x)
    n = len(s) // 2
    if len(s) % 2 == 0:
        return s[:n] == s[n:][::-1]
    else:
        return s[:n+1] == s[n:][::-1]


def is_lychrel(n, max_its=50):
    s = str(n)
    for i in range(max_its):
        n = int(s) + int(s[::-1])
        s = str(n)
        if is_palindrome(s):
            return False
    return True


print(sum(1 for n in range(1, 10000) if is_lychrel(n)))