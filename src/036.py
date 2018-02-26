"""

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)

"""

"""

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)

"""

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