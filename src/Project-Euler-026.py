import decimal
import itertools

decimal.getcontext().prec = 500


def chunks(l, size):
    n = len(l) // size
    return [l[(i * size):(i+1) *size] for i in range(n)]


def find_recurring_subset(iterable):
    if len(set(iterable)) == 1:
        return iterable[0]

    for i in range(2, len(iterable)//2):
        c = chunks(iterable, i)
        if len(c) < 3:
            return None
        if len(set(c)) == 1:
            return c[0]


def recurring_cycle(n):
    s = str(n)
    if len(s) < decimal.getcontext().prec + 2:
        return None
    s = s.replace('0.', '')[:-1]
    # Trim leading elements up to 3/4 lenth of string
    for i in range(1, int(round(0.75*len(s)))):
        recurring = find_recurring_subset(s[i:])
        if recurring is not None:
            return recurring
    return None

N = 1000


def recurring_in_reciprocal(n):
    return recurring_cycle(decimal.Decimal(1) / decimal.Decimal(n))

r = ((val, recurring_in_reciprocal(val)) for val in range(1, N))
r = ((val, rec, len(rec)) for val, rec in r if rec is not None)

print(max(r, key=lambda x: x[2]))